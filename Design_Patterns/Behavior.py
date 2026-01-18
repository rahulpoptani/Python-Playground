from Common.Tags import BEHAVIORAL_OBSERVER

import time
import threading
import random

# ---------------- Observer Pattern ----------------

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclass must implement update()")


class Subject:
    def __init__(self):
        self._observers = set()
    
    def subscribe(self, observer: Observer):
        self._observers.add(observer)
    
    def unsubscribe(self, observer: Observer):
        self._observers.discard(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# ---------------- Example with "WebSocket" ----------------

class WebSocketFeed(Subject):
    """Simulated Binance-like WebSocket feed"""
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        self._running = False
    
    def start_stream(self):
        self._running = True
        threading.Thread(target=self._generate_messages, daemon=True).start()
    
    def _generate_messages(self):
        while self._running:
            # Fake trade message
            price = round(random.uniform(20000, 30000), 2)
            message = {"symbol": self.symbol, "price": price}
            self.notify(message)
            time.sleep(1)  # simulate new tick every second


class TradingBot(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"[{self.name}] received update: {message}")


# ---------------- Demo ----------------
if __name__ == "__main__":
    btc_feed = WebSocketFeed("BTCUSDT")

    bot1 = TradingBot("ScalperBot")
    bot2 = TradingBot("ChartUpdater")

    # subscribe both bots to the BTC feed
    btc_feed.subscribe(bot1)
    btc_feed.subscribe(bot2)

    btc_feed.start_stream()

    time.sleep(5)  # run for a while before exiting
