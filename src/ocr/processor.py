import pytesseract
from PIL import Image
from typing import Optional

class OCRProcessor:
    """Handles OCR processing of document images."""
    
    def __init__(self, tesseract_path: Optional[str] = None):
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
            
    def extract_text(self, image_path: str) -> str:
        """
        Extract text from an image using Tesseract OCR.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Extracted text as string
        """
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            raise Exception(f"OCR processing failed: {str(e)}")
            
    def extract_text_with_confidence(self, image_path: str) -> tuple[str, float]:
        """
        Extract text from an image with confidence scores.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Tuple of (extracted text, average confidence)
        """
        try:
            image = Image.open(image_path)
            data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
            
            # Calculate average confidence
            confidences = [float(conf) for conf in data['conf'] if conf != '-1']
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
            
            return data['text'], avg_confidence
        except Exception as e:
            raise Exception(f"OCR processing with confidence failed: {str(e)}") 