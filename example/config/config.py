import platform
from pathlib import Path

from clio import Workspace

_current_os = platform.system()


def is_mac() -> bool:
    return _current_os == "Darwin"


def is_win() -> bool:
    return _current_os == "Windows"


def get_database_path() -> Path:
    return Workspace.default_workspace().get_path("cache/db.db")


def get_log_dir() -> Path:
    return Workspace.default_workspace().get_path("cache/log")
