from setuptools import setup

APP = ['btc.py']
DATA_FILES = ['btc.icns']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'btc.icns',
    'plist': {
        'CFBundleName': 'BTC',
        'CFBundleDisplayName': 'BTC',
        'CFBundleGetInfoString': "BTC",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'LSUIElement': True,
    },
    'packages': ['rumps', 'requests', 'webbrowser'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)