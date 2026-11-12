import json
import os
import tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = os.environ.get('APP_BASE_URL', 'http://127.0.0.1:8765').rstrip('/')
ART = Path('test-artifacts')
ART.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1440, 'height': 1000}, accept_downloads=True)
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.on('dialog', lambda dialog: dialog.accept())
    page.goto(BASE + '/', wait_until='networkidle')
    page.wait_for_url('**/workbench.html')
    page.locator('#nav button').first.wait_for()
    assert page.locator('#nav button').count() == 8, 'Eight modules must be visible in navigation'
    for module in ['overview', 'inventory', 'product', 'cbam', 'library', 'forecast', 'collaboration', 'reporting']:
        page.locator('#nav [data-tab=' + module + ']').click()
        assert page.locator('#' + module).is_visible(), module + ' must open'
    page.locator('#nav [data-tab=inventory]').click()
    assert page.locator('#ghgRows tr').count() == 7
    assert page.locator('#scope3 .bar').count() == 15
    assert '277.4' in page.locator('#totals').inner_text(), 'LB total excludes MB alternative'
    assert '236.6' in page.locator('#totals').inner_text(), 'MB total excludes LB alternative'
    assert page.locator('#ghgRows .warn').count() == 3
    page.locator('#nav [data-tab=product]').click()
    assert '1,360' in page.locator('#productResult').inner_text()
    assert 'Allocation not documented' in page.locator('#productWarnings').inner_text()
    page.locator('#nav [data-tab=library]').click()
    assert '69 matching records' in page.locator('#count').inner_text()
    page.locator('#search').fill('73181520')
    assert page.locator('#libraryRows tr').count() == 1
    assert '731815' in page.locator('#libraryRows').inner_text()
    page.locator('#libraryRows [data-use]').click()
    assert page.locator('#cbam').is_visible()
    assert 'Archived transitional' in page.locator('#cbamResult').inner_text()
    page.locator('[data-group=cbam][data-key=applicability]').select_option('No')
    assert '1.89 tCO2e/t' in page.locator('#cbamResult').inner_text(), 'SEE must not be divided by output'
    page.locator('#nav [data-tab=reporting]').click()
    page.locator('#generate').click()
    assert 'Archived transitional values are not current defaults' in page.locator('#issues').inner_text()
    assert 'submissionReady="false"' in page.locator('#xml').inner_text()
    page.locator('#nav [data-tab=cbam]').click()
    page.locator('[data-step=2]').click()
    page.locator('[data-group=cbam][data-key=direct]').fill('2.21')
    page.locator('[data-group=cbam][data-key=direct]').press('Tab')
    page.locator('#nav [data-tab=forecast]').click()
    row = page.locator('#forecastRows tr').first
    assert '24,240' in row.inner_text(), '300 tonnes * (2.21 - 1.2) * EUR 80'
    assert 'Blocked' in page.locator('#forecastRows tr').nth(1).inner_text(), 'Missing SEFA must not become zero'
    page.locator('#nav [data-tab=collaboration]').click()
    page.locator('#counterparty').fill('Acceptance test supplier')
    page.locator('#request').fill('Provide evidence')
    page.locator('#newRequest').click()
    assert 'Acceptance test supplier' in page.locator('#requests').inner_text()
    with page.expect_download() as download:
        page.locator('#export').click()
    project_path = download.value.path()
    project = json.loads(Path(project_path).read_text())
    assert project['version'] == 2
    page.locator('#reset').click()
    page.locator('#import').set_input_files(project_path)
    assert 'Project imported' in page.locator('#msg').inner_text()
    page.locator('#nav [data-tab=library]').click()
    response = page.request.get(BASE + '/data/CN-Archived-Reference.csv')
    assert response.ok, 'CSV download must be reachable'
    import csv
    import io
    assert len(list(csv.DictReader(io.StringIO(response.text())))) == 69
    page.set_viewport_size({'width': 390, 'height': 844})
    page.locator('#nav [data-tab=inventory]').click()
    assert page.locator('#inventory').is_visible()
    page.screenshot(path=str(ART / 'mobile-inventory.png'), full_page=True)
    page.set_viewport_size({'width': 1440, 'height': 1000})
    page.locator('#nav [data-tab=overview]').click()
    page.screenshot(path=str(ART / 'desktop-overview.png'), full_page=True)
    assert not errors, 'JavaScript errors: ' + repr(errors)
    browser.close()
(ART / 'result.json').write_text(json.dumps({'status': 'passed', 'base': BASE, 'checks': ['root entry', '8 modules', 'GHG totals and evidence', '15 scope3 categories', 'product FU and warnings', '69 CN records and prefix search', 'library transfer', 'per-tonne intensity', 'archive warning in draft', 'forecast arithmetic and blank SEFA', 'collaboration', 'project roundtrip', '69-row CSV', 'mobile navigation', 'no JavaScript errors']}, indent=2))
