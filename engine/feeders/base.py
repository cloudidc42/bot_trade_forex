"""
Base Feeder Class
Abstract base class for all market data feeders
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from datetime import datetime
import pandas as pd
from loguru import logger


class BaseFeeder(ABC):
    """
    Abstract base class for market data feeders

    All concrete feeders must implement:
    - fetch_ohlcv()
    - get_available_symbols()
    - validate_symbol()
    """

    def __init__(
        self,
        name: str,
        data_dir: str = "data/raw"
    ):
        """
        Initialize base feeder

        Args:
            name: Feeder name (e.g., "yahoo", "ccxt", "mt5")
            data_dir: Directory to store raw data
        """
        self.name = name
        self.data_dir = data_dir
        self._cache = {}
        logger.info(f"Initialized {self.name} feeder")

    @abstractmethod
    def fetch_ohlcv(
        self,
        symbol: str,
        timeframe: str = "1d",
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        limit: Optional[int] = None
    ) -> pd.DataFrame:
        """
        Fetch OHLCV data for a symbol

        Args:
            symbol: Trading symbol (e.g., "AAPL", "BTC/USDT")
            timeframe: Timeframe (e.g., "1m", "5m", "1h", "1d")
            start_date: Start date
            end_date: End date
            limit: Maximum number of candles

        Returns:
            DataFrame with columns: timestamp, open, high, low, close, volume
        """
        pass

    @abstractmethod
    def get_available_symbols(self) -> List[str]:
        """
        Get list of available symbols

        Returns:
            List of symbol strings
        """
        pass

    @abstractmethod
    def validate_symbol(self, symbol: str) -> bool:
        """
        Validate if symbol exists

        Args:
            symbol: Symbol to validate

        Returns:
            True if valid, False otherwise
        """
        pass

    def normalize_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize DataFrame to standard format

        Standard columns: timestamp, open, high, low, close, volume

        Args:
            df: Raw DataFrame

        Returns:
            Normalized DataFrame
        """
        if df is None or df.empty:
            return pd.DataFrame()

        # Ensure index is datetime
        if not isinstance(df.index, pd.DatetimeIndex):
            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df.set_index('timestamp', inplace=True)
            elif 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                df.set_index('date', inplace=True)

        # Lowercase column names
        df.columns = [col.lower() for col in df.columns]

        # Rename common variations
        rename_map = {
            'o': 'open',
            'h': 'high',
            'l': 'low',
            'c': 'close',
            'v': 'volume',
            'vol': 'volume'
        }
        df.rename(columns=rename_map, inplace=True)

        # Select only OHLCV columns
        required_cols = ['open', 'high', 'low', 'close', 'volume']
        available_cols = [col for col in required_cols if col in df.columns]
        df = df[available_cols].copy()

        # Sort by timestamp
        df.sort_index(inplace=True)

        # Remove duplicates
        df = df[~df.index.duplicated(keep='first')]

        return df

    def get_cache_key(self, symbol: str, timeframe: str) -> str:
        """Generate cache key"""
        return f"{self.name}_{symbol}_{timeframe}"

    def cache_data(self, key: str, data: pd.DataFrame):
        """Cache data in memory"""
        self._cache[key] = data
        logger.debug(f"Cached data for key: {key}")

    def get_cached_data(self, key: str) -> Optional[pd.DataFrame]:
        """Retrieve cached data"""
        return self._cache.get(key)

    def clear_cache(self):
        """Clear all cached data"""
        self._cache.clear()
        logger.info(f"Cleared cache for {self.name}")

    def get_info(self) -> Dict[str, Any]:
        """Get feeder information"""
        return {
            'name': self.name,
            'data_dir': self.data_dir,
            'cached_items': len(self._cache)
        }

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
