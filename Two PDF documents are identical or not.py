import hashlib 
from difflib import SequenceMatcher 

def compute_file_hashes(file_path1, file_path2): 
    """Compute SHA-1 hashes for two files and compare them."""
    
    # Initialize SHA-1 hash objects for both files
    hash1 = hashlib.sha1() 
    hash2 = hashlib.sha1() 

    # Read and hash the first file in chunks
    with open(file_path1, "rb") as file1: 
        chunk = b''  # Initialize chunk
        while chunk != b'': 
            chunk = file1.read(1024)  # Read file in 1024-byte chunks
            hash1.update(chunk)  # Update hash with the chunk
            
    # Read and hash the second file in chunks
    with open(file_path2, "rb") as file2: 
        chunk = b''  # Initialize chunk
        while chunk != b'': 
            chunk = file2.read(1024)  # Read file in 1024-byte chunks
            hash2.update(chunk)  # Update hash with the chunk

    # Return the hexadecimal digest of both hashes
    return hash1.hexdigest(), hash2.hexdigest() 

# Compute hashes for the specified files
hash1, hash2 = compute_file_hashes("pd1.pdf", "pd1.pdf") 

# Compare the two hashes and print the result
if hash1 != hash2: 
    print("These files are not identical") 
else: 
    print("These files are identical") 