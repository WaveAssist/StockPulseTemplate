import waveassist
waveassist.init()
import yfinance as yf

tickers_str = waveassist.fetch_data("tickers")
tickers = [t.strip() for t in tickers_str.split(",")]

ticker_data = yf.Tickers(" ".join(tickers))

data_to_store = {}
for ticker in tickers:
    try:
        t = ticker_data.tickers[ticker]
        data_to_store[ticker] = {
            "info": t.info,
        }
    except Exception as e:
        data_to_store[ticker] = {"error": str(e)}

waveassist.store_data("ticker_data", data_to_store)
