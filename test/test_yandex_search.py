from selene import browser, be, have


def test_yandex_search(browser_screen_resolution):
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.wait_until(2)
    browser.element('.DistributionSplashScreenModal-CloseButtonOuter[type="button"]').click()
    browser.element('[id=search-result]').should(have.text(
        'User-oriented Web UI browser tests in Python.'))
