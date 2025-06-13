import waveassist
waveassist.init()
import pandas as pd

tickers_str = waveassist.fetch_data("tickers")
tickers = [t.strip() for t in tickers_str.split(",")]

ticker_data = waveassist.fetch_data("ticker_data") 

df_list = []
for ticker in tickers:
    data = ticker_data.get(ticker, {})
    info = data.get("info", {})

    current_price = info.get('currentPrice') or info.get('regularMarketPrice')
    previous_close = info.get('previousClose') or info.get('regularMarketPreviousClose')

    if current_price and previous_close:
        day_change_pct = ((current_price - previous_close) / previous_close) * 100
    else:
        day_change_pct = 0

    premarket_price = info.get('preMarketPrice')
    premarket_change_pct = 0
    if premarket_price and previous_close:
        premarket_change_pct = ((premarket_price - previous_close) / previous_close) * 100

    df_list.append({
        'Ticker': ticker,
        'Current Price': current_price or 0,
        'Day Change %': round(day_change_pct, 2),
        'Pre-Market Change %': round(premarket_change_pct, 2)
    })

df = pd.DataFrame(df_list)
waveassist.store_data("stock_dataframe", df)
