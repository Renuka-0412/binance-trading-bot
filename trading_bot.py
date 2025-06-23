from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging

# Setup logging
logging.basicConfig(
    filename='bot_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com'
        logging.info("Bot initialized with testnet: %s", testnet)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            logging.info("Market order placed: %s", order)
            print("✅ Market order placed successfully.")
        except BinanceAPIException as e:
            logging.error("API Error (Market Order): %s", e)
            print("❌ API Error (Market Order):", e)
        except Exception as e:
            logging.error("Unexpected Error (Market Order): %s", e)
            print("❌ Unexpected Error:", e)

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logging.info("Limit order placed: %s", order)
            print("✅ Limit order placed successfully.")
        except BinanceAPIException as e:
            logging.error("API Error (Limit Order): %s", e)
            print("❌ API Error (Limit Order):", e)
        except Exception as e:
            logging.error("Unexpected Error (Limit Order): %s", e)
            print("❌ Unexpected Error:", e)

if __name__ == "__main__":
    print("=== Welcome to Binance Testnet Trading Bot ===")
    api_key = input("🔑 Enter your Binance Testnet API Key: ")
    api_secret = input("🔐 Enter your Binance Testnet API Secret: ")
    bot = BasicBot(api_key, api_secret)
    print(bot.client.ping())

    while True:
        print("\nChoose an order type:")
        print("1. Market Order")
        print("2. Limit Order")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "3":
            print("👋 Exiting bot. Goodbye!")
            break

        symbol = input("📈 Enter trading pair (e.g., BTCUSDT): ").upper()
        side = input("🧾 Enter side (BUY/SELL): ").upper()
        quantity = float(input("📦 Enter quantity: "))

        if choice == "1":
            bot.place_market_order(symbol, side, quantity)
        elif choice == "2":
            price = float(input("💰 Enter limit price: "))
            bot.place_limit_order(symbol, side, quantity, price)
        else:
            print("⚠ Invalid choice. Please try again.")