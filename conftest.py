import pytest
from selene.support.shared import browser


@pytest.fixture
def open_browser():
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    browser.open('https://github.com')

