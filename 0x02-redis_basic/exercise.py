#!/usr/bin/env python3
"""using redis to store and retrieve values"""
import redis
import uuid
from typing import Union, Any


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
