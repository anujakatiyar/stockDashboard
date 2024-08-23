import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.title("Stock Valuation Dashboard")
st.sidebar.header("Stock Selection")

stock_options = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "FB", "NVDA", "NFLX", "BABA", "V", 
    "JPM", "JNJ", "WMT", "PG", "UNH", "MA", "HD", "DIS", "PYPL", "ADBE",
    "PFE", "INTC", "CSCO", "KO", "PEP", "MRK", "XOM", "NKE", "LLY", "T",
    "ABBV", "CRM", "ABT", "CMCSA", "VZ", "MCD", "COST", "ACN", "MDT", "DHR",
    "ORCL", "NEE", "AVGO", "WFC", "TXN", "LIN", "HON", "UPS", "QCOM", "UNP",
    "CVX", "PM", "RTX", "BMY", "IBM", "SBUX", "INTU", "MS", "GILD", "AXP",
    "AMD", "LOW", "CAT", "SCHW", "AMGN", "AMT", "BA", "SPGI", "ISRG", "MMM",
    "TMO", "DE", "ZTS", "GS", "SYK", "ADI", "EL", "PLD", "MO", "MMC",
    "BKNG", "BLK", "LMT", "MDLZ", "CCI", "TJX", "NOW", "FIS", "ICE", "GE",
    "SO", "CME", "CL", "HUM", "C", "ETN", "AON", "FDX", "CI", "WM"
]

search_stock = st.sidebar.text_input("Search for Stock Ticker").upper()
filtered_stocks = [stock for stock in stock_options if stock.startswith(search_stock)]
ticker_input = st.sidebar.selectbox("Select Stock Ticker", filtered_stocks)

start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", datetime.now())

if st.sidebar.button("Submit"):
    @st.cache_data
    def load_data(ticker, start, end):
        stock_data = yf.download(ticker, start=start, end=end)
        return stock_data

    stock_data = load_data(ticker_input, start_date, end_date)

    st.subheader(f"{ticker_input} Valuation Analysis")
    try:
        ticker_info = yf.Ticker(ticker_input)
        pe_ratio = ticker_info.info.get('trailingPE', 'N/A')
        if pe_ratio != "N/A":
            if pe_ratio > 25:
                st.write(f"{ticker_input} might be overvalued with a P/E ratio of {pe_ratio}.")
            elif pe_ratio < 15:
                st.write(f"{ticker_input} might be undervalued with a P/E ratio of {pe_ratio}.")
            else:
                st.write(f"{ticker_input} seems fairly valued with a P/E ratio of {pe_ratio}.")
        else:
            st.write("P/E ratio data not available.")
    except Exception as e:
        st.write(f"Could not retrieve P/E ratio: {e}")

    st.subheader(f"{ticker_input} Stock Data")
    st.write(stock_data.tail())

    stock_data['50_MA'] = stock_data['Adj Close'].rolling(window=50).mean()
    stock_data['200_MA'] = stock_data['Adj Close'].rolling(window=200).mean()

    st.subheader(f"{ticker_input} Closing Price & Moving Averages")
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Adj Close'], label='Closing Price', color='blue')
    plt.plot(stock_data['50_MA'], label='50-Day MA', color='orange')
    plt.plot(stock_data['200_MA'], label='200-Day MA', color='green')
    plt.title(f'{ticker_input} Closing Price & Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(plt)

    def compute_rsi(data, time_window):
        diff = data.diff(1).dropna()
        up_chg = 0 * diff
        down_chg = 0 * diff

        up_chg[diff > 0] = diff[diff > 0]
        down_chg[diff < 0] = -diff[diff < 0]

        up_chg_avg = up_chg.rolling(window=time_window, min_periods=1).mean()
        down_chg_avg = down_chg.rolling(window=time_window, min_periods=1).mean()

        rs = up_chg_avg / down_chg_avg
        rsi = 100 - 100 / (1 + rs)
        return rsi

    st.subheader(f"{ticker_input} Relative Strength Index (RSI)")
    rsi = compute_rsi(stock_data['Adj Close'], 14)
    plt.figure(figsize=(12, 6))
    plt.plot(rsi, label='RSI', color='purple')
    plt.axhline(70, linestyle='--', color='red')
    plt.axhline(30, linestyle='--', color='green')
    plt.title(f'{ticker_input} RSI (14-Day)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    st.pyplot(plt)

    st.subheader("Stock Information")
    st.write(ticker_info.info)
