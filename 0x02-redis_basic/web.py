#!/usr/bin/env python3
"""A module with tools for request caching and tracking."""

import redis
import requests
from functools import wraps
from typing import Callable


# Initialize Redis connection
redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Caches the output of fetched data and tracks request count."""

    @wraps(method)
    def invoker(url: str) -> str:
        """The wrapper function for caching the output."""
        # Increment access count for this URL
        redis_store.incr(f"count:{url}")

        # Try to get cached result
        result = redis_store.get(f"result:{url}")
        if result:
            return result.decode("utf-8")

        # Fetch from URL if not cached
        try:
            result = method(url)
            # Cache the result with a 10-second expiration
            redis_store.setex(f"result:{url}", 10, result)
            return result
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return ""  # Return empty string or handle error differently

    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Fetches and returns the HTML content of the URL, with caching and tracking."""
    return requests.get(url).text
