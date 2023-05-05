import json
import os
import re

class Container:
    _username: str
    _storage: set[str] = set()
    _filename: str

