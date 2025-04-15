import os
from pathlib import Path
from typing import List, Optional

def ensure_directory_exists(directory: str) -> None:
    """Ensure that a directory exists, create it if it doesn't."""
    Path(directory).mkdir(parents=True, exist_ok=True)

def get_file_extension(file_path: str) -> str:
    """Get the file extension in lowercase."""
    return Path(file_path).suffix.lower()

def is_supported_document(file_path: str) -> bool:
    """Check if the file is a supported document type."""
    supported_extensions = {
        '.pdf', '.jpg', '.jpeg', '.png', '.tiff', '.bmp',
        '.doc', '.docx', '.txt'
    }
    return get_file_extension(file_path) in supported_extensions

def list_files_in_directory(directory: str, 
                          extensions: Optional[List[str]] = None) -> List[str]:
    """
    List all files in a directory with optional extension filtering.
    
    Args:
        directory: Directory to search
        extensions: List of file extensions to include (e.g., ['.pdf', '.jpg'])
        
    Returns:
        List of file paths
    """
    if not os.path.exists(directory):
        return []
        
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if extensions is None or get_file_extension(file_path) in extensions:
                files.append(file_path)
                
    return files

def generate_output_filename(input_path: str, 
                           output_dir: str,
                           suffix: str = "_processed") -> str:
    """
    Generate an output filename based on the input file.
    
    Args:
        input_path: Path to input file
        output_dir: Directory for output file
        suffix: Suffix to add to filename
        
    Returns:
        Path to output file
    """
    input_filename = Path(input_path).stem
    extension = get_file_extension(input_path)
    output_filename = f"{input_filename}{suffix}{extension}"
    return os.path.join(output_dir, output_filename) 