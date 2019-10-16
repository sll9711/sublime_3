"""This module provides persistent global storage for other modules."""

from collections import defaultdict
import threading

from .util import printf
from .settings import Settings


if False:
    from typing import DefaultDict, Dict, List, Set, Tuple, Type
    from mypy_extensions import TypedDict
    import sublime
    import subprocess
    from .linter import Linter

    Bid = sublime.BufferId
    FileName = str
    LinterName = str
    LintError = TypedDict('LintError', {
        'line': int,
        'start': int,
        'end': int,
        'region': sublime.Region,
        'linter': LinterName,
        'error_type': str,
        'code': str,
        'msg': str,
        'filename': FileName,
        'uid': str,
        'priority': int,
        'panel_line': Tuple[int, int]
    }, total=False)


api_ready = False
kill_switch = True

settings = Settings()

errors = defaultdict(list)  # type: DefaultDict[Bid, List[LintError]]
linter_classes = {}  # type: Dict[str, Type[Linter]]
assigned_linters = {}  # type: Dict[Bid, Set[LinterName]]

active_procs = defaultdict(list)  # type: DefaultDict[Bid, List[subprocess.Popen]]
active_procs_lock = threading.Lock()


def debug_mode():
    # type: () -> bool
    """Return whether the "debug" setting is True."""
    return settings.get('debug', False)


def debug(*args):
    # type: (...) -> None
    """Print args to the console if the "debug" setting is True."""
    if debug_mode():
        printf(*args)
