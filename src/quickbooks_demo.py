"""
QuickBooks Demo Script
Creates a dummy invoice (sandbox or mocked).
"""

import json

def create_invoice():
    # Mock invoice JSON
    invoice = {
        "invoice_id": "INV-1001",
        "customer": "Test Customer A",
        "amount": 250.00,
        "status": "Created"
    }

    with open("invoice.json", "w") as f:
        json.dump(invoice, f, indent=2)

    print("✅ Dummy invoice saved to invoice.json")

if __name__ == "__main__":
    create_invoice()
