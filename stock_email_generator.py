import waveassist
waveassist.init()

# import pandas as pd

# Fetch the stock data DataFrame from the previous node
stock_data = waveassist.fetch_data("stock_dataframe")

# Convert to HTML table with styling
html_table = stock_data.to_html(
    index=False,
    escape=False,
    table_id="stock-table",
    classes="stock-data"
)

# Create styled HTML email content
html_content = f"""
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        .stock-data {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        .stock-data th, .stock-data td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        .stock-data th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        .stock-data tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .positive {{
            color: #008000;
        }}
        .negative {{
            color: #ff0000;
        }}
        h2 {{
            color: #333;
        }}
    </style>
</head>
<body>
    <h2>📈 StockPulse - Market Snapshot</h2>
    <p>Here's your daily market pulse for your tickers:</p>
    {html_table}
    <p><small>Data provided by Yahoo Finance via yfinance</small></p>
</body>
</html>
"""

# Send the email
waveassist.send_email(
    subject="📊 StockPulse - Market Snapshot",
    html_content=html_content
)

waveassist.store_data("email_sent", True)
print("✅ Stock email sent successfully.")