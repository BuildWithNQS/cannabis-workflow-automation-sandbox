# n8n Workflow (No-Code Example)

This folder contains **n8n workflow examples** for cannabis operations automation.  

## Example Workflow (High-Level)
1. **Trigger:** New Deal in HubSpot → via HubSpot node.
2. **Finance:** Create Invoice in QuickBooks node (sandbox or mock).
3. **Storage:** Upload Invoice PDF to OneDrive node.
4. **Compliance:** Record sales in Metrc (mock API or JSON file).
5. **Notifications:** Send Slack/Email alerts on success or error.

## Files
- `hubspot_to_quickbooks.json` → Example n8n workflow (HubSpot → QuickBooks).
- `full_pipeline.json` → Example workflow chaining Sales → Finance → Storage → Compliance.

## Usage
This folder is a placeholder for **n8n workflow examples**.  

- In a real setup, `.json` files exported from n8n would live here.  
- Each file would represent an automation flow (e.g., HubSpot → QuickBooks, or full Sales → Finance → Storage → Compliance).  
- These can be imported into [n8n.io](https://n8n.io) (self-hosted or cloud), updated with client credentials, and run from the n8n dashboard.  

Note: Prototype JSON exports are not yet included  this is part of the MVP build.

---


