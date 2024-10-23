#!/usr/bin/env python3
"""using redis to store and retrieve values"""
import redis
import uuid
import functools
from typing import Union, Any, Callable


def count_calls(method: Callable) -> Callable:
    """Decorator that increments a Redis key with the qualified name of the method"""
    @functools.wraps(method) 
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the call count in Redis."""
        key = f"count:{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache():
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float]:
        """get data from redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
    
    def get_str(self, data: bytes) -> str:
        """convert bytes to str"""
        return data.decode('utf-8')
    
    def get_int(self, data: bytes) -> int:
        """convert bytes to int"""
        return int.from_bytes(data, byteorder='big')

   