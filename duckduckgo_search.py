from selene import browser, be, have


browser.open('https://duckduckgo.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="react-layout"]').should(have.text('Releases · yashaka/selene · GitHub'))
