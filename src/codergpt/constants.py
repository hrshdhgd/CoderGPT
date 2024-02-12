"""All constants used in the package."""

from pathlib import Path

TEST_DIR = Path(__file__).resolve().parents[2] / "tests"
SRC = Path(__file__).resolve().parents[1]
PACKAGE_DIR = SRC / "codergpt"
EXTENSION_MAP_FILE = PACKAGE_DIR / "extensions.yaml"
LANGUAGE_MAP_KEY = "language-map"
INSPECTION_HEADERS = ["File", "Language"]
GPT_3_5_TURBO = "gpt-3.5-turbo"
GPT_4 = "gpt-4"
GPT_4_TURBO = "gpt-4-turbo-preview"
