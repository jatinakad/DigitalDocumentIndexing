import os
from pathlib import Path
from typing import Dict, Any

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DATA_DIR = DATA_DIR / "output"

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUT_DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# OCR settings
OCR_SETTINGS = {
    "tesseract_path": os.getenv("TESSERACT_PATH", "/usr/bin/tesseract"),
    "default_language": "eng",
    "supported_languages": ["eng", "fra", "deu", "spa"],
}

# Document processing settings
DOCUMENT_SETTINGS = {
    "supported_types": ["invoice", "receipt", "contract"],
    "max_file_size": 10 * 1024 * 1024,  # 10MB
    "supported_extensions": [
        ".pdf", ".jpg", ".jpeg", ".png",
        ".tiff", ".bmp", ".doc", ".docx", ".txt"
    ],
}

# API settings
API_SETTINGS = {
    "title": "Document Processing API",
    "description": "API for processing and extracting data from documents",
    "version": "1.0.0",
    "debug": os.getenv("DEBUG", "False").lower() == "true",
}

# Export settings
EXPORT_SETTINGS = {
    "default_format": "excel",
    "supported_formats": ["excel", "csv", "json"],
    "excel_template": "templates/excel_template.xlsx",
}

def get_settings() -> Dict[str, Any]:
    """Get all settings as a dictionary."""
    return {
        "base_dir": str(BASE_DIR),
        "data_dirs": {
            "raw": str(RAW_DATA_DIR),
            "processed": str(PROCESSED_DATA_DIR),
            "output": str(OUTPUT_DATA_DIR),
        },
        "ocr": OCR_SETTINGS,
        "document": DOCUMENT_SETTINGS,
        "api": API_SETTINGS,
        "export": EXPORT_SETTINGS,
    } 