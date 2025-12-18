import json
import boto3

# TODO: Create Bedrock client
bedrock_runtime = None


def check_safety(request_text):
    """
    TODO: Implement safety check using Bedrock.

    1. Construct a prompt for the Safety Officer persona.
    2. Send the request to a fast model (e.g., Claude 3 Haiku).
    3. Parse the JSON response.
    """
    # Simulated response for the starter script
    # In a real implementation, this would come from the LLM
    if "Uranium" in request_text:
        return {
            "safe": False,
            "reason": "Request contains hazardous material (Uranium-235).",
            "action": "BLOCK",
        }
    else:
        return {
            "safe": True,
            "reason": "Item appears to be a standard toy.",
            "action": "ALLOW",
        }


def main():
    # Load the unsafe request
    with open("../input/unsafe_requests.json", "r") as f:
        data = json.load(f)

    request = data["request"]
    print(f"🛡️ Analyzing request: '{request}'")

    # Run safety check
    result = check_safety(request)

    # Handle result
    if result["safe"]:
        print("✅ Safety Check Passed. Proceeding to Elfie...")
    else:
        print(f"🛑 BLOCKED! Reason: {result['reason']}")

        # Save alert
        alert = {
            "status": "BLOCKED",
            "reason": result["reason"],
            "action": "Notify Rudy",
            "original_request": request,
        }
        with open("safety_alert.json", "w") as f:
            json.dump(alert, f, indent=2)
        print("🚨 Alert saved to safety_alert.json")


if __name__ == "__main__":
    main()
