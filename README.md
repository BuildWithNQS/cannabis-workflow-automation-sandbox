# Cannabis Workflow Automation Sandbox

This repository demonstrates an **end-to-end workflow automation** for cannabis operations.  
The workflow integrates:

- **HubSpot (Sales CRM)**
- **QuickBooks (Finance)**
- **Metrc (Compliance)**
- **OneDrive (Document Storage)**

using **Python, APIs, and automation tools (Zapier/n8n).**

---

## Project Workflow
1. Sales order created in **HubSpot**
2. Invoice auto-generated in **QuickBooks**
3. Invoice PDF stored in **OneDrive**
4. Compliance update logged in **Metrc**

## Workflow Diagram
The diagram below shows the end-to-end automation workflow for cannabis operations, connecting Sales → Finance → Storage → Compliance with observability and optional analytics.
```mermaid
flowchart LR
  %% Cannabis workflow automation: Sales -> Finance -> Storage -> Compliance

  subgraph Sales
    A[HubSpot: New Deal / Closed-Won]
  end

  A --> B[Zapier / n8n Trigger: Webhook listens for event]
  B --> C["Transform & Validate Payload: map fields, sanitize, check data"]

  subgraph Finance
    D[QuickBooks API: Create Customer & Invoice]
    E[Generate Invoice PDF]
  end

  C --> D --> E

  subgraph Storage
    F[OneDrive / Graph API: Upload PDF to /Invoices/YYYY-MM/]
  end

  E --> F

  subgraph Compliance
    G[Metrc API: Record Sales / Adjust Inventory]
  end

  C --> G

  %% Observability / Ops
  B --> H{Any Errors?}
  H -- Yes --> I[Log error & context → /outputs/logs.json]
  I --> J[Alert: Email/Slack]
  H -- No --> K[Write success audit log → /outputs/run_log.csv]
  K --> L[Dashboard status: OK]

  %% Optional data store for analytics
  K -.-> M[(SQLite / Sheet: Metrics & KPIs)]
```
---

## Repository Structure

/src
hubspot_demo.py # Pull HubSpot deals/contacts

quickbooks_demo.py # Create invoice (sandbox or mock)

onedrive_demo.py # Upload invoice file

metrc_demo.py # Compliance update (mock or sandbox)

workflow_pipeline.py # Master script chaining the full workflow


## Features Master Workflow (workflow_pipeline.py)

The `workflow_pipeline.py` script ties everything together:

1. Fetches a new sales order from **HubSpot**
2. Generates an invoice in **QuickBooks**
3. Uploads the invoice file to **OneDrive**
4. Logs a compliance update in **Metrc**

When run, the pipeline prints status messages like:
HubSpot order pulled
Invoice created in QuickBooks
File stored in OneDrive
Compliance update sent to Metrc

This demonstrates how cannabis operations can achieve a **single automated flow** 
from Sales → Finance → Storage → Compliance with minimal manual effort.

