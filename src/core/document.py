from typing import Dict, Any, Optional
from pathlib import Path

class Document:
    """Core document class that represents a document and its metadata."""
    
    def __init__(self, file_path: str, document_type: str):
        self.file_path = Path(file_path)
        self.document_type = document_type
        self.metadata: Dict[str, Any] = {}
        self.extracted_text: Optional[str] = None
        self.structured_data: Dict[str, Any] = {}
        
    def add_metadata(self, key: str, value: Any) -> None:
        """Add metadata to the document."""
        self.metadata[key] = value
        
    def set_extracted_text(self, text: str) -> None:
        """Set the extracted text from OCR processing."""
        self.extracted_text = text
        
    def add_structured_data(self, key: str, value: Any) -> None:
        """Add structured data extracted from the document."""
        self.structured_data[key] = value
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert document to dictionary format."""
        return {
            "file_path": str(self.file_path),
            "document_type": self.document_type,
            "metadata": self.metadata,
            "extracted_text": self.extracted_text,
            "structured_data": self.structured_data
        } 