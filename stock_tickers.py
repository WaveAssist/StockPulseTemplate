import waveassist
waveassist.init()
import yfinance as yf

tickers = waveassist.fetch_data("tickers")

tickers = yf.Tickers(tickers)
waveassist.store_data("tickers", tickers)