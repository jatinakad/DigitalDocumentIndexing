import pytest
from src.core.document import Document

def test_document_initialization():
    """Test document initialization with basic parameters."""
    doc = Document("test.pdf", "invoice")
    assert doc.file_path.name == "test.pdf"
    assert doc.document_type == "invoice"
    assert doc.metadata == {}
    assert doc.extracted_text is None
    assert doc.structured_data == {}

def test_document_metadata():
    """Test adding metadata to document."""
    doc = Document("test.pdf", "invoice")
    doc.add_metadata("author", "John Doe")
    doc.add_metadata("date", "2023-01-01")
    
    assert doc.metadata["author"] == "John Doe"
    assert doc.metadata["date"] == "2023-01-01"

def test_document_extracted_text():
    """Test setting extracted text."""
    doc = Document("test.pdf", "invoice")
    test_text = "This is a test document."
    doc.set_extracted_text(test_text)
    
    assert doc.extracted_text == test_text

def test_document_structured_data():
    """Test adding structured data."""
    doc = Document("test.pdf", "invoice")
    doc.add_structured_data("invoice_number", "INV-123")
    doc.add_structured_data("total_amount", 100.50)
    
    assert doc.structured_data["invoice_number"] == "INV-123"
    assert doc.structured_data["total_amount"] == 100.50

def test_document_to_dict():
    """Test converting document to dictionary."""
    doc = Document("test.pdf", "invoice")
    doc.add_metadata("author", "John Doe")
    doc.set_extracted_text("Test content")
    doc.add_structured_data("invoice_number", "INV-123")
    
    doc_dict = doc.to_dict()
    
    assert doc_dict["file_path"] == "test.pdf"
    assert doc_dict["document_type"] == "invoice"
    assert doc_dict["metadata"]["author"] == "John Doe"
    assert doc_dict["extracted_text"] == "Test content"
    assert doc_dict["structured_data"]["invoice_number"] == "INV-123" 