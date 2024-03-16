import pytest
from selene import browser


@pytest.fixture()
def browser_screen_resolution():
    browser.driver.set_window_size(800, 600)
