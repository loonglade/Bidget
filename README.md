# Bidget (macOS only)

Bitcoin price in your menu bar!

Price updates every 10 seconds with the BTC/USDT pair using the Binance API.

<img src="https://github.com/loonglade/Bidget/blob/main/assets/screenshot1.png?raw=true">

# Dependencies:
    chardet
    requests
    rumps
    py2app

# Installation:
    git clone https://github.com/loonglade/Bidget
    python3 -m venv venv
    source venv/bin/activate
    pip install chardet requests rumps py2app
    python setup.py py2app

After installation, just run 'btc.app' inside the 'dist' folder.
Include it in your login items (system settings) if you wish to run it automatically when you start your computer.
    
#### <i>Troubleshooting:
###### Q: I get an "API Request Failed" error.
###### A: It's likely you're using a VPN. Changing the location or disabling your VPN should fix this.</i><br></br>
#### <img src="https://www.file-extensions.org/imgs/app-icon/128/10409/bitcoin-core-icon.png" width="20" height="20"> Donations </img>
bitcoin:bc1q6nu6347k3n077sscjntk949namnulrrpshz4j4

