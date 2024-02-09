"""CoderGPT package."""

import importlib_metadata

from codergpt.commenter import CodeCommenter
from codergpt.explainer import CodeExplainer

from .main import CoderGPT

try:
    __version__ = importlib_metadata.version(__name__)
except importlib_metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover


__all__ = ["CoderGPT", "CodeExplainer", "CodeCommenter"]
