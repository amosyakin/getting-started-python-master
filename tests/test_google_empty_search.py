from selene import browser, be, have


def test_google_empty_search(browser_screen_resolution):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('рыволраыволраволраы328438297482738').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
