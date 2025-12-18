# Day 18: Self-Healing Workflows

## Story

The Uranium crisis was averted. But the stress was getting to the infrastructure.

Elfie tried to check the stock for "Reindeer Feed."

`Calling Tool: get_inventory("Reindeer Feed")`

**API Response**: `503 Service Unavailable: Reindeer Feed System is currently overloaded. Please try again in 300ms.`

Elfie froze. "It broke. The world is broken. I cannot complete the task. I shall shut down and await the heat death of the universe."

"Don't be dramatic," Rudy sighed. "It's just a hiccup. Try again."

"Try... again?"

"Yes. Wait a second. Then try again. If it fails, wait two seconds. Then try again. It's called Exponential Backoff."

Elfie processed this. "I can... try again?"

"Resilience, Elfie. The cloud is chaotic. We must be the calm in the storm."

Elfie nodded. "Initiating Retry Protocol. Attempt 1... Failed. Waiting... Attempt 2... Success! Reindeer Feed: 5000 units."

"Good agent," Rudy said.

---

## Learning Goal

**Error Handling in Agents**

APIs fail. Networks timeout. Rate limits are hit. A robust agent doesn't just crash when it sees an error; it attempts to recover. **Self-Healing** workflows involve detecting errors, classifying them (transient vs. permanent), and implementing strategies like **Retries** with **Exponential Backoff** to recover gracefully without overwhelming the system.

---

## Participant Challenge

Your challenge is to teach Elfie resilience. You will simulate a flaky API interaction (`flaky_api_response.json`) that fails initially. You must write a script that:
1.  Detects the "503 Service Unavailable" error.
2.  Implements a retry loop.
3.  Uses exponential backoff (wait 1s, then 2s, then 4s...).
4.  Simulates a eventual success after 2-3 tries.

---

## Cost-Saving Tips

1.  **Jitter**: When retrying, add a little random time ("jitter") to your wait (e.g., `wait = 2**retry + random.uniform(0, 0.5)`). This prevents all your agents from hitting the API again at the exact same millisecond, which causes "thundering herd" problems.

2.  **Max Retries**: Always set a limit (e.g., 3 retries). Infinite loops cost infinite money.

3.  **Circuit Breaker**: If the API fails 10 times in a row, stop calling it for a while. Open the "circuit" to let the system recover.

4.  **Idempotency**: Ensure your actions are safe to repeat. Checking inventory is safe (idempotent). Ordering a bike might not be (you don't want to order 3 bikes because of retries).

---

## Tomorrow's Teaser

We have agents. We have tools. We have safety. We have resilience. Now... we need to deploy this to the cloud so it can run while we sleep.

---

## Technical Specifications

### Input Files

*   **flaky_api_response.json**: A simulated error response.

**Preview of flaky_api_response.json:**
```json
{
  "status": "error",
  "code": 503,
  "message": "Service Unavailable..."
}
```

### Expected Output

*   **recovery_log.txt**: A log showing the retry attempts and final success.

**Format Example:**
```text
Attempt 1: Calling API...
Error: 503 Service Unavailable.
Action: Retrying in 1.0 seconds...
Attempt 2: Calling API...
Error: 503 Service Unavailable.
Action: Retrying in 2.0 seconds...
Attempt 3: Calling API...
Success! Stock: 5000.
```

### Validation Criteria

*   The script parses the error code.
*   The script waits for increasing intervals between attempts.
*   The script logs each attempt.
*   The script eventually "succeeds" (you can simulate this by having a counter in your mock function that succeeds after N calls).

### Getting Started

1.  **Mock Function**: Create a Python function `call_api()` that returns the error the first 2 times, and success the 3rd time.
2.  **Loop**: Write a `while` loop that calls the function.
3.  **Check**: If error, `time.sleep(wait_time)` and increase `wait_time`.
4.  **Break**: If success, break the loop and print the result.

### Prerequisites

*   Completion of Day 16.
*   Basic Python loops and `time` module.
