"""
Master Workflow Script
Chains HubSpot → QuickBooks → OneDrive → Metrc
"""

import hubspot_demo
import quickbooks_demo
import onedrive_demo
import metrc_demo

def run_workflow():
    print(" Starting workflow...")

    hubspot_demo.fetch_hubspot_data()
    quickbooks_demo.create_invoice()
    onedrive_demo.upload_file()
    metrc_demo.compliance_update()

    print(" Workflow completed successfully!")

if __name__ == "__main__":
    run_workflow()
