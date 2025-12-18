import json
import os

# Mock Database Path (referencing Day 15 input)
DB_PATH = "../../day15/input/inventory_db.json"


def load_db(path):
    """Load the inventory database."""
    if not os.path.exists(path):
        # Fallback for standalone testing if file doesn't exist
        return [
            {"name": "Super Console 5000", "stock": 2, "location": "Vault 1"},
            {"name": "Red Racing Bike", "stock": 15, "location": "Warehouse A"},
        ]

    with open(path, "r") as f:
        return json.load(f)


def lambda_handler(event, context):
    """
    Simulated Lambda Handler.

    Args:
        event (dict): The event payload (e.g., {"item_name": "..."})
        context (object): AWS Lambda context object (unused here)

    Returns:
        dict: API response
    """
    print(f"🔌 Received event: {json.dumps(event)}")

    item_name = event.get("item_name")
    if not item_name:
        return {"status": "error", "message": "Missing item_name"}

    # Load DB
    inventory = load_db(DB_PATH)

    # Search for item
    # Optimizing to O(1) lookup would be better, but linear scan is fine for small DB
    found_item = next(
        (item for item in inventory if item["name"].lower() == item_name.lower()), None
    )

    if found_item:
        response = {
            "status": "success",
            "item_name": found_item["name"],
            "stock": found_item["stock"],
            "location": found_item.get("location", "Unknown"),
        }
    else:
        response = {
            "status": "error",
            "message": f"Item '{item_name}' not found in inventory.",
        }

    print(f"📤 Returning response: {json.dumps(response)}")
    return response


def main():
    # Load the test event
    with open("../input/inventory_event.json", "r") as f:
        test_event = json.load(f)

    # Run the handler
    result = lambda_handler(test_event, None)

    # Save output
    with open("api_response.json", "w") as f:
        json.dump(result, f, indent=2)
    print("✅ Response saved to api_response.json")


if __name__ == "__main__":
    main()
