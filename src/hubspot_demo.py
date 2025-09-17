# hubspot_demo.py
# Demo script: Pull HubSpot deals/contacts (mock example)

def get_hubspot_deals():
    # In a real workflow, this would call HubSpot’s API
    # Here we’ll just mock it for demo purposes
    return [
        {"deal_id": 1, "customer": "Green Leaf Dispensary", "amount": 5000},
        {"deal_id": 2, "customer": "Herbal Supply Co.", "amount": 3200}
    ]

if __name__ == "__main__":
    deals = get_hubspot_deals()
    print("Fetched HubSpot deals:")
    for deal in deals:
        print(deal)
