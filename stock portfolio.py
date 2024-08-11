class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        current_price = self.get_mock_stock_price(ticker)
        if ticker in self.portfolio:
            self.portfolio[ticker]['shares'] += shares
        else:
            self.portfolio[ticker] = {
                'shares': shares,
                'purchase_price': current_price,
                'history': []
            }
        self.portfolio[ticker]['history'].append({
            'action': 'buy',
            'shares': shares,
            'price': current_price,
            'total_value': shares * current_price
        })
        print(f"Added {shares} shares of {ticker} at {current_price:.2f} per share.")

    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio and self.portfolio[ticker]['shares'] >= shares:
            current_price = self.get_mock_stock_price(ticker)
            self.portfolio[ticker]['shares'] -= shares
            self.portfolio[ticker]['history'].append({
                'action': 'sell',
                'shares': shares,
                'price': current_price,
                'total_value': shares * current_price
            })
            print(f"Sold {shares} shares of {ticker} at {current_price:.2f} per share.")
            if self.portfolio[ticker]['shares'] == 0:
                del self.portfolio[ticker]
        else:
            print(f"Insufficient shares to sell or {ticker} not found in portfolio.")

    def get_mock_stock_price(self, ticker):
        # Mock stock prices for demonstration purposes
        mock_prices = {
            "AAPL": 150.00,
            "GOOGL": 2800.00,
            "MSFT": 300.00,
            "AMZN": 3500.00,
            "TSLA": 700.00
        }
        return mock_prices.get(ticker.upper(), 100.00)

    def display_portfolio(self):
        for ticker, details in self.portfolio.items():
            current_price = self.get_mock_stock_price(ticker)
            total_value = details['shares'] * current_price
            print(f"{ticker}: {details['shares']} shares, Purchase Price: {details['purchase_price']:.2f}, Current Price: {current_price:.2f}, Total Value: {total_value:.2f}")

    def track_performance(self):
        total_initial_value = 0
        total_current_value = 0
        for ticker, details in self.portfolio.items():
            purchase_value = details['shares'] * details['purchase_price']
            current_value = details['shares'] * self.get_mock_stock_price(ticker)
            total_initial_value += purchase_value
            total_current_value += current_value
            performance = ((current_value - purchase_value) / purchase_value) * 100
            print(f"{ticker}: Initial Value: {purchase_value:.2f}, Current Value: {current_value:.2f}, Performance: {performance:.2f}%")

        portfolio_performance = ((total_current_value - total_initial_value) / total_initial_value) * 100
        print(f"Total Portfolio: Initial Value: {total_initial_value:.2f}, Current Value: {total_current_value:.2f}, Performance: {portfolio_performance:.2f}%")

if __name__ == "__main__":
    portfolio = StockPortfolio()

    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter the ticker symbol: ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter the ticker symbol: ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            portfolio.track_performance()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
