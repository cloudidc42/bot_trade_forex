"""
Yahoo Finance Feeder
Fetch stock, ETF, and commodity data from Yahoo Finance
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional, List
from loguru import logger

from engine.feeders.base import BaseFeeder


class YahooFeeder(BaseFeeder):
    """
    Yahoo Finance data feeder

    Supports:
    - US Stocks (AAPL, TSLA, MSFT, etc.)
    - ETFs (SPY, QQQ, GLD, USO, etc.)
    - Indices (^GSPC, ^DJI, ^IXIC)
    - Forex (EURUSD=X, GBPUSD=X)
    """

    def __init__(self, data_dir: str = "data/raw"):
        super().__init__(name="yahoo", data_dir=data_dir)

        # Common symbols
        self.popular_stocks = [
            'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA',
            'NVDA', 'META', 'BRK-B', 'JPM', 'V'
        ]

        self.popular_etfs = [
            'SPY',   # S&P 500
            'QQQ',   # NASDAQ 100
            'GLD',   # Gold
            'USO',   # Oil
            'SLV',   # Silver
            'TLT',   # 20Y Treasury
            'DIA',   # Dow Jones
            'IWM'    # Russell 2000
        ]

    def fetch_ohlcv(
        self,
        symbol: str,
        timeframe: str = "1d",
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        limit: Optional[int] = None
    ) -> pd.DataFrame:
        """
        Fetch OHLCV data from Yahoo Finance

        Args:
            symbol: Yahoo ticker symbol (e.g., "AAPL", "SPY")
            timeframe: "1m", "5m", "15m", "1h", "1d", "1wk", "1mo"
            start_date: Start date
            end_date: End date
            limit: Number of candles (not used, kept for interface)

        Returns:
            DataFrame with OHLCV data
        """
        try:
            # Check cache first
            cache_key = self.get_cache_key(symbol, timeframe)
            cached = self.get_cached_data(cache_key)
            if cached is not None:
                logger.debug(f"Using cached data for {symbol}")
                return cached

            # Set default dates if not provided
            if end_date is None:
                end_date = datetime.now()
            if start_date is None:
                start_date = end_date - timedelta(days=365*3)  # 3 years

            # Convert timeframe
            interval = self._convert_timeframe(timeframe)

            logger.info(f"Fetching {symbol} from Yahoo Finance...")
            logger.debug(f"Period: {start_date} to {end_date}, Interval: {interval}")

            # Download data
            ticker = yf.Ticker(symbol)
            df = ticker.history(
                start=start_date,
                end=end_date,
                interval=interval,
                auto_adjust=True  # Adjust for splits and dividends
            )

            if df.empty:
                logger.warning(f"No data returned for {symbol}")
                return pd.DataFrame()

            # Normalize
            df = self.normalize_dataframe(df)

            # Cache
            self.cache_data(cache_key, df)

            logger.success(
                f"Fetched {len(df)} candles for {symbol} "
                f"({df.index[0]} to {df.index[-1]})"
            )

            return df

        except Exception as e:
            logger.error(f"Error fetching {symbol}: {e}")
            return pd.DataFrame()

    def _convert_timeframe(self, timeframe: str) -> str:
        """
        Convert standard timeframe to Yahoo Finance interval

        Standard: "1m", "5m", "15m", "1h", "1d"
        Yahoo: "1m", "5m", "15m", "1h", "1d", "1wk", "1mo"
        """
        mapping = {
            '1m': '1m',
            '5m': '5m',
            '15m': '15m',
            '30m': '30m',
            '1h': '1h',
            '1d': '1d',
            '1w': '1wk',
            '1M': '1mo'
        }
        return mapping.get(timeframe, '1d')

    def get_available_symbols(self) -> List[str]:
        """
        Get list of popular symbols

        Returns:
            List of symbol strings
        """
        return self.popular_stocks + self.popular_etfs

    def validate_symbol(self, symbol: str) -> bool:
        """
        Validate if symbol exists on Yahoo Finance

        Args:
            symbol: Symbol to validate

        Returns:
            True if valid, False otherwise
        """
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            return 'regularMarketPrice' in info or 'currentPrice' in info
        except:
            return False

    def get_symbol_info(self, symbol: str) -> dict:
        """
        Get detailed information about a symbol

        Args:
            symbol: Symbol to query

        Returns:
            Dictionary with symbol info
        """
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            return {
                'symbol': symbol,
                'name': info.get('longName', 'N/A'),
                'sector': info.get('sector', 'N/A'),
                'industry': info.get('industry', 'N/A'),
                'market_cap': info.get('marketCap', 0),
                'currency': info.get('currency', 'USD'),
                'exchange': info.get('exchange', 'N/A')
            }
        except Exception as e:
            logger.error(f"Error getting info for {symbol}: {e}")
            return {}

    def fetch_multiple(
        self,
        symbols: List[str],
        **kwargs
    ) -> dict:
        """
        Fetch data for multiple symbols

        Args:
            symbols: List of symbols
            **kwargs: Arguments for fetch_ohlcv()

        Returns:
            Dictionary {symbol: DataFrame}
        """
        results = {}

        for symbol in symbols:
            logger.info(f"Fetching {symbol}...")
            df = self.fetch_ohlcv(symbol, **kwargs)
            if not df.empty:
                results[symbol] = df

        logger.info(f"Fetched {len(results)}/{len(symbols)} symbols successfully")
        return results
