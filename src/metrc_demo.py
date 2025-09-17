"""
Metrc Demo Script
Mocks a compliance API update with JSON.
"""

import json

def compliance_update():
    compliance_data = {
        "update_id": "MT-001",
        "invoice": "INV-1001",
        "status": "Reported"
    }

    with open("metrc_mock.json", "w") as f:
        json.dump(compliance_data, f, indent=2)

    print("✅ Compliance update saved to metrc_mock.json")

if __name__ == "__main__":
    compliance_update()
