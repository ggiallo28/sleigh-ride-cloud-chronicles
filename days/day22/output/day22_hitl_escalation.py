# /// script
# dependencies = [
#   "boto3",
#   "strands-agents",
# ]
# ///

import json
from dataclasses import dataclass
from typing import Dict, Any, Optional

# -------------------------------------
# Day 22 – Human-in-the-Loop (HITL)
# Treating humans as first-class agents
# -------------------------------------

INPUT_LETTER = "../input/letter_pony.txt"
OUTPUT_LOG = "hitl_log.txt"
OUTPUT_APPROVAL = "approval_request.json"


# ============================================
# APPROVAL REQUEST
# ============================================


@dataclass
class ApprovalRequest:
    """Structured request for human review."""
    request_id: str
    child_name: str
    request_type: str
    item_requested: str
    risk_level: str
    confidence_score: float
    context: str
    recommendation: str


# ============================================
# WORKFLOW STATE
# ============================================


@dataclass
class WorkflowState:
    """Track workflow through suspension and resumption."""
    status: str  # running, suspended, resumed, completed
    current_step: str
    human_decision: Optional[str]


# ============================================
# ESCALATION LOGIC
# ============================================


def load_letter(filepath: str) -> str:
    """TODO: Load letter content from file."""
    pass


def analyze_request(letter_content: str) -> Dict[str, Any]:
    """
    TODO: Analyze letter for escalation triggers.

    Check for:
    - Live animal requests ("real pony")
    - High-value items
    - Low confidence situations

    Return analysis dict with child_name, item, risk_factors
    """
    pass


def should_escalate(analysis: Dict[str, Any]) -> tuple:
    """
    TODO: Determine if request needs human approval.

    Rules:
    - Live animals → Always escalate
    - Confidence < 0.5 → Escalate
    - High-value → Escalate

    Return: (should_escalate: bool, reason: str)
    """
    pass


def create_approval_request(analysis: Dict, letter: str) -> ApprovalRequest:
    """TODO: Create structured approval request."""
    pass


# ============================================
# HUMAN INTERACTION
# ============================================


def get_human_decision() -> str:
    """
    TODO: Get human input using input().

    Validate response is Y/N/A.
    In production: async webhook/callback.
    """
    pass


def process_decision(decision: str, request: ApprovalRequest) -> Dict[str, Any]:
    """
    TODO: Process human's decision.

    Y → APPROVE, proceed with order
    N → REJECT, send apology
    A → ALTERNATIVE, switch to toy version
    """
    pass


# ============================================
# MAIN ORCHESTRATION
# ============================================


def save_log(entries: list, filepath: str):
    """TODO: Save HITL log to file."""
    pass


def main():
    """
    TODO: Orchestrate the Human-in-the-Loop workflow.

    Flow:
    1. Load letter
    2. Analyze for escalation triggers
    3. If escalation needed:
       a. Create approval request
       b. SUSPEND workflow
       c. Get human decision
       d. RESUME workflow
       e. Process decision
    4. Save logs

    Expected: Pony request triggers escalation, human decides
    """
    print("=" * 60)
    print("Day 22: Human-in-the-Loop as a First-Class Agent")
    print("=" * 60)

    log_entries = []

    # TODO: Implement workflow


if __name__ == "__main__":
    main()
