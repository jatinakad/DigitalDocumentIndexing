from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
import os
from ..core.document import Document
from ..processing.document_processor import DocumentProcessor
from ..ocr.processor import OCRProcessor
from ..utils.file_utils import ensure_directory_exists, generate_output_filename

app = FastAPI(title="Document Processing API")

# Initialize processors
ocr_processor = OCRProcessor()
document_processor = DocumentProcessor(ocr_processor)

@app.post("/process-document")
async def process_document(
    file: UploadFile = File(...),
    document_type: str = "invoice"
) -> dict:
    """
    Process a single document and extract structured data.
    
    Args:
        file: Uploaded document file
        document_type: Type of document (invoice, receipt, contract)
        
    Returns:
        Processed document data
    """
    try:
        # Save uploaded file temporarily
        temp_dir = "data/temp"
        ensure_directory_exists(temp_dir)
        file_path = os.path.join(temp_dir, file.filename)
        
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
            
        # Process document
        document = document_processor.process_document(file_path, document_type)
        
        # Clean up temporary file
        os.remove(file_path)
        
        return document.to_dict()
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch-process")
async def batch_process(
    files: List[UploadFile] = File(...),
    document_type: str = "invoice"
) -> List[dict]:
    """
    Process multiple documents in batch.
    
    Args:
        files: List of uploaded document files
        document_type: Type of documents
        
    Returns:
        List of processed document data
    """
    results = []
    for file in files:
        result = await process_document(file, document_type)
        results.append(result)
    return results

@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"} 