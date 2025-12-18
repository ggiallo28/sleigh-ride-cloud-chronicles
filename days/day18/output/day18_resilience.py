import json
import time
import random

# Configuration
MAX_RETRIES = 5
BASE_DELAY = 1.0  # seconds


def mock_api_call(attempt):
    """
    Simulates a flaky API.
    Succeeds only on the 3rd attempt (or later).
    """
    print(f"📞 Calling API (Attempt {attempt})...")

    if attempt < 3:
        # Simulate Error
        return {"status": "error", "code": 503, "message": "Service Unavailable"}
    else:
        # Simulate Success
        return {"status": "success", "stock": 5000, "item": "Reindeer Feed"}


def main():
    print("🛡️ Starting Resilient Workflow...")

    log_entries = []

    for attempt in range(1, MAX_RETRIES + 1):
        # 1. Call API
        response = mock_api_call(attempt)

        # 2. Check Result
        if response.get("status") == "success":
            msg = f"✅ Success! Stock: {response['stock']}"
            print(msg)
            log_entries.append(f"Attempt {attempt}: {msg}")
            break
        else:
            error_msg = f"Error: {response.get('code')} {response.get('message')}"
            print(f"❌ {error_msg}")
            log_entries.append(f"Attempt {attempt}: {error_msg}")

            # 3. Backoff Strategy
            if attempt < MAX_RETRIES:
                # Exponential Backoff with Jitter
                # delay = base * (2 ^ (attempt - 1)) + random_jitter
                delay = (BASE_DELAY * (2 ** (attempt - 1))) + random.uniform(0, 0.5)

                wait_msg = f"⏳ Retrying in {delay:.2f} seconds..."
                print(wait_msg)
                log_entries.append(f"Action: {wait_msg}")

                time.sleep(delay)
            else:
                fail_msg = "💀 Max retries reached. Workflow failed."
                print(fail_msg)
                log_entries.append(fail_msg)

    # Save Log
    with open("recovery_log.txt", "w") as f:
        f.write("\n".join(log_entries))
    print("📝 Log saved to recovery_log.txt")


if __name__ == "__main__":
    main()
