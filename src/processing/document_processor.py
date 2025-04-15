from typing import Dict, Any
from pathlib import Path
from ..core.document import Document
from ..ocr.processor import OCRProcessor

class DocumentProcessor:
    """Processes different types of documents and extracts structured data."""
    
    def __init__(self, ocr_processor: OCRProcessor):
        self.ocr_processor = ocr_processor
        
    def process_document(self, file_path: str, document_type: str) -> Document:
        """
        Process a document based on its type and extract relevant information.
        
        Args:
            file_path: Path to the document
            document_type: Type of document (e.g., 'invoice', 'receipt', 'contract')
            
        Returns:
            Processed Document object
        """
        document = Document(file_path, document_type)
        
        # Extract text using OCR for image-based documents
        if self._is_image_document(file_path):
            text = self.ocr_processor.extract_text(file_path)
            document.set_extracted_text(text)
            
        # Process based on document type
        if document_type == 'invoice':
            self._process_invoice(document)
        elif document_type == 'receipt':
            self._process_receipt(document)
        elif document_type == 'contract':
            self._process_contract(document)
            
        return document
        
    def _is_image_document(self, file_path: str) -> bool:
        """Check if the document is an image file."""
        image_extensions = {'.jpg', '.jpeg', '.png', '.tiff', '.bmp'}
        return Path(file_path).suffix.lower() in image_extensions
        
    def _process_invoice(self, document: Document) -> None:
        """Process invoice documents and extract relevant fields."""
        # Add invoice-specific processing logic here
        document.add_metadata('document_category', 'financial')
        # Extract invoice number, date, amount, etc.
        
    def _process_receipt(self, document: Document) -> None:
        """Process receipt documents and extract relevant fields."""
        # Add receipt-specific processing logic here
        document.add_metadata('document_category', 'financial')
        # Extract merchant, date, items, total amount, etc.
        
    def _process_contract(self, document: Document) -> None:
        """Process contract documents and extract relevant fields."""
        # Add contract-specific processing logic here
        document.add_metadata('document_category', 'legal')
        # Extract parties, dates, terms, etc. 