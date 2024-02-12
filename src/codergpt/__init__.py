"""CoderGPT package."""

import importlib_metadata

from codergpt.commenter import CodeCommenter
from codergpt.documenter import CodeDocumenter
from codergpt.explainer import CodeExplainer
from codergpt.optimizer import CodeOptimizer

# from codergpt.tester import CodeTester
from .main import CoderGPT

try:
    __version__ = importlib_metadata.version(__name__)
except importlib_metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover


__all__ = ["CoderGPT", "CodeExplainer", "CodeCommenter", "CodeOptimizer", "CodeDocumenter"]
