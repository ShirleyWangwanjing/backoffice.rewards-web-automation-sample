__author__ = 'Ragu.Sekaran'


class ConfigZalenium:
    zalenium_command_executor = f'http://localhost:4444/wd/hub'
    chrome_caps = {'browserName': 'chrome', 'goog:chromeOptions': {
        'w3c': False
    }}
    firefox_caps = {'browserName': 'firefox', 'idleTimeout': 1000}
