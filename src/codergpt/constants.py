"""All constants used in the package."""

from pathlib import Path

SRC = Path(__file__).resolve().parents[1]
PACKAGE_DIR = SRC / "codergpt"
EXTENSION_MAP_FILE = PACKAGE_DIR / "extensions.yaml"
LANGUAGE_MAP_KEY = "language-map"
INSPECTION_HEADERS = ["File", "Language"]
