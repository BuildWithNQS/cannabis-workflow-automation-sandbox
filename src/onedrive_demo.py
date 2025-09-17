"""
OneDrive Demo Script
Pretends to upload a file to OneDrive (mocked for demo).
"""

import shutil

def upload_file():
    source = "invoice.json"
    destination = "onedrive_invoice.json"

    shutil.copy(source, destination)
    print(f"✅ Uploaded {source} to OneDrive (mock) as {destination}")

if __name__ == "__main__":
    upload_file()
