__author__ = 'Ragu.Sekaran'


class ConfigMobile:
    appium_command_Executor = 'http://127.0.0.1:4723/wd/hub'
    android_desired_capabilities = {'platformName': 'Android', 'platformVersion': '8.1.0', 'deviceName': 'HUAWEI P20',
                                    'browserName': 'chrome'}
    android_nexus6_emulator_desired_capabilities = {'platformName': 'Android', 'platformVersion': '9',
                                                    'deviceName': 'Android SDK built for x86', 'browserName': "chrome"}
    ios_desired_capabilities = {'platformName': 'iOS', 'platformVersion': '11.2', 'deviceName': 'iPad Air',
                                'browserName': "Safari"}

    android_desired_capabilities_app = {'platformName': 'Android', 'platformVersion': '8.1.0',
                                        'deviceName': 'HUAWEI P20', 'appPackage': 'com.iherb.cn',
                                        'appActivity': "com.iherb.other.BeforeSplashActivity"}
    android_nexus_s_emulator_desired_capabilities_app = {'platformName': 'Android', 'platformVersion': '9',
                                                         'deviceName': 'Android SDK built for x86',
                                                         'appPackage': 'com.iherb.cn',
                                                         'appActivity': "com.iherb.other.BeforeSplashActivity"}
    ios_desired_capabilities_app = {'platformName': 'iOS', 'platformVersion': '12.2', 'bundleId': 'bundleId',
                                    'deviceName': 'Tony', 'appPackage': 'com.iherb.cn',
                                    'appActivity': "com.iherb.other.BeforeSplashActivity"}
