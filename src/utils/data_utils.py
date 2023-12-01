import yfinance as yf

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="5m")
    return data.tail(1).to_dict(orient="records")[0] 