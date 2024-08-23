# Stock Valuation Dashboard

This is a Streamlit application that allows users to analyze the valuation of various stocks. The app provides a user-friendly interface to select a stock, view its historical data, and perform valuation analysis based on the Price-to-Earnings (P/E) ratio and other financial metrics.

## Features

- **Stock Selection**: Choose from a list of 100 popular stocks or search for a specific stock ticker.
- **Real-Time Search Filtering**: As you type in the search box, the dropdown list dynamically filters to show stocks starting with the entered characters.
- **Submit Button**: After selecting a stock and date range, click the submit button to retrieve and display the stock data.
- **Valuation Analysis**: The app provides a valuation analysis based on the P/E ratio, identifying whether a stock may be overvalued, undervalued, or fairly valued.
- **Moving Averages**: The dashboard plots the closing price along with the 50-day and 200-day moving averages.
- **Relative Strength Index (RSI)**: The app calculates and displays the RSI to help identify overbought or oversold conditions.
- **Stock Information**: Detailed stock information is provided, including fundamental data.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Usage

1. On the sidebar, start typing the ticker of the stock you want to analyze in the "Search for Stock Ticker" box.
2. The dropdown will show all stocks starting with the entered characters.
3. Select the desired stock from the dropdown.
4. Choose the start and end dates for the data you wish to analyze.
5. Click the "Submit" button.
6. The dashboard will display the stock's valuation analysis, moving averages, RSI, and detailed stock information.

## Dependencies

- `streamlit`: For creating the web app interface.
- `yfinance`: For fetching historical stock data.
- `matplotlib`: For plotting stock prices, moving averages, and RSI.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for making it easy to build and share custom data applications.
- [Yahoo Finance API](https://www.yahoofinanceapi.com/) for providing access to financial data.
