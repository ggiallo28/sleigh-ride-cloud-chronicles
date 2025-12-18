# Day 16: The API Call (MCP)

## Story

Elfie was holding the tool call like a baton. `get_inventory("Red Racing Bike")`.

"Okay," Elfie said. "I'm ready. Connect me to the matrix."

"It's just a Python script, Elfie," the Apprentice said.

"It is the MATRIX," Elfie insisted. "I am reaching out from the digital void to touch the physical world. I am crossing the boundary!"

"Sure," the Apprentice said. "Here's the API endpoint."

Elfie executed the call. The signal raced through the simulated network, hit the mock database, and returned a payload.

`{ "status": "success", "stock": 15, "location": "Warehouse A" }`

Elfie gasped. "I saw it. I saw the bikes. They are red. They are shiny. They are in Aisle 3."

Rudy popped up on the screen. "Excellent! Now, about that Plush Dragon..."

---

## Learning Goal

**AWS Lambda and API Integration**

Defining a tool is only half the battle. You also need the code that *executes* the tool. In a serverless architecture, this is often an **AWS Lambda** function. When the agent decides to call a tool, the platform (Bedrock) pauses, sends the parameters to your Lambda, waits for the result, and then resumes the conversation. Today, you will write the "Lambda" (a local Python function) that actually performs the logic.

---

## Participant Challenge

Your challenge is to implement the "backend" for Elfie. You will write a Python function that accepts the tool call payload (`inventory_event.json`), queries your mock database (`inventory_db.json`), and returns the result in a format the agent can understand.

---

## Cost-Saving Tips

1.  **Local Testing**: You don't need to deploy a real AWS Lambda function to test the logic. Write a standard Python function and pass the JSON event to it locally. This saves deployment time and cloud costs.

2.  **Efficient Lookups**: Load your `inventory_db.json` into a dictionary (hash map) at the start of the function for O(1) lookups, rather than scanning the list every time.

3.  **Standardized Responses**: Ensure your function always returns a consistent JSON structure (e.g., `{"status": "...", "data": "..."}`). This helps the agent parse the result reliably, reducing the need for retries.

4.  **Error Handling**: If the item isn't found, return a clear error message ("Item not found") rather than crashing. The agent can read the error and tell the user, which is a better experience than a timeout.

---

## Tomorrow's Teaser

Elfie is powerful now. Too powerful. What happens when she tries to order something... dangerous?

---

## Technical Specifications

### Input Files

*   **inventory_event.json**: A JSON object simulating the event passed to a Lambda function.
*   **inventory_db.json**: The database to query.

**Preview of inventory_event.json:**
```json
{
  "action": "check_inventory",
  "item_name": "Super Console 5000"
}
```

### Expected Output

*   **api_response.json**: The result returned by your function.

**Format Example:**
```json
{
  "status": "success",
  "item_name": "Super Console 5000",
  "stock": 2,
  "location": "Vault 1"
}
```

### Validation Criteria

*   The script reads the event and the database.
*   The function correctly finds the item in the database.
*   The function returns the correct stock count and location.
*   The function handles "Item Not Found" gracefully (if tested with a fake item).

### Getting Started

1.  **Load DB**: Read `inventory_db.json` into a Python list/dict.
2.  **Define Handler**: Create a function `lambda_handler(event, context)`.
3.  **Parse Event**: Extract `item_name` from the `event` dictionary.
4.  **Logic**: Search the DB for the item.
5.  **Return**: Construct the response dictionary and return it.
6.  **Test**: Call `lambda_handler` with the data from `inventory_event.json`.

### Prerequisites

*   Completion of Day 14 (Tool Definition).
*   Basic Python functions.
