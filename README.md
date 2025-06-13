<h1 align="center">StockPulse</h1>

<p align="center">
  <a href="https://waveassist.io/templates/StockPulse">
    <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  </a>
  <img src="https://img.shields.io/badge/StockPulse-AI%20Powered%20Stock%20Updates-blue" alt="StockPulse Badge" />
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## Overview

StockPulse runs on [WaveAssist](https://waveassist.io) to provide instant stock market updates by fetching ticker prices, analyzing daily and pre-market changes, and sending a report by email. Effortlessly automate your daily stock market monitoring using this task.

---

## One-Click Deploy on WaveAssist

<p>
  <a href="https://waveassist.io/templates/StockPulse" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

Deploy StockPulse quickly on [WaveAssist](https://waveassist.io) — a zero-infrastructure automation platform that handles orchestration, scheduling, secrets, and hosting for you.

> 🔐 You may be prompted to log in or create a free WaveAssist account before continuing.

#### How to Use:

1. Click the button above or go to [waveassist.io/templates/StockPulse](https://waveassist.io/templates/StockPulse)
2. Enter the following variables in the Variables tab (customize as needed):
    - **tickers**: Provide a comma-separated list of stock tickers you want to monitor (e.g., `AAPL,GOOGL,MSFT`).
3. Run the starting node:
   - **StockTickers**: Fetches and prepares the list of stock tickers.
4. Click **Deploy** to schedule and automate your stock pulse workflow.

✅ You’re now running StockPulse on autopilot.

---

## Manual Deployment

Clone this repository and run the following scripts in order:

* `stock_tickers.py`
* `ticker_price_analysis.py`
* `stock_email_generator.py`

#### Requirements

Install dependencies:

```
pip install yfinance
```

---

## Features

* **StockTickers** (`stock_tickers`): Fetch and prepare a set of stock tickers for monitoring.
* **TickerPriceAnalysis** (`ticker_price_analysis`): Analyze latest prices, daily changes, and pre-market moves for the defined tickers.
* **StockEmailGenerator** (`stock_email_generator`): Generate and send an HTML email summarizing stock price movements.
* **Processing Variables**: Manage core data using variables like `email_sent`, `tickers`, `price_dataframe`, `ticker_data`, and `stock_dataframe`.

---

Built with ❤️ by the WaveAssist team. Want help or integrations? [Say hello](https://waveassist.io).
