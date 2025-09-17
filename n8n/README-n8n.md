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
1. Open [n8n.io](https://n8n.io/) (self-hosted or cloud).
2. Import the `.json` workflow file from this folder.
3. Update credentials (HubSpot, QuickBooks, OneDrive, Metrc).
4. Run workflow and monitor execution in n8n dashboard.

---


