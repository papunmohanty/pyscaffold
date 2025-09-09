from enum import Enum


class PathType(str, Enum):
    FILE = "file"
    ONLINE_JSON = "online_json"
