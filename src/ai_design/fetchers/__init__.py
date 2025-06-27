"""
Data fetchers for trending topics from various sources.
"""

from .base_fetcher import BaseFetcher
from .google_trends_fetcher import GoogleTrendsFetcher
from .reddit_fetcher import RedditFetcher

__all__ = ["BaseFetcher", "GoogleTrendsFetcher", "RedditFetcher"] 