import rumps, requests, json, webbrowser

class CryptoPrice(rumps.App):
    def __init__(self):
        super(CryptoPrice, self).__init__("Loading...", icon="btc.icns")
        self.menu = [
            rumps.MenuItem("Github", callback=self.github_page),
            rumps.MenuItem("Donations", callback=self.donations_page)
        ]

    @rumps.timer(10)
    def update_prices(self, _):
        try:
            response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", timeout=5)
            response.raise_for_status()
            data = response.json()
            btc_price = float(data["price"])
            btc_price = round(btc_price, 2)  # decimal places
            self.title = f" ${btc_price}"

        except requests.exceptions.RequestException as e:
            self.title = "API request failed"
            print(f"API request failed: {e}")

        except KeyError as e:
            self.title = "Unexpected API response"
            print(f"Unexpected API response, missing key: {e}")

        except Exception as e:
            self.title = "An error occurred"
            print(f"An error occurred: {e}")

    def github_page(self, _):
        webbrowser.open('https://github.com/loonglade/Bidget/')

    def donations_page(self, _):
        webbrowser.open('https://bitcoinexplorer.org/address/bc1q6nu6347k3n077sscjntk949namnulrrpshz4j4')

if __name__ == "__main__":
    app = CryptoPrice()
    app.run()
