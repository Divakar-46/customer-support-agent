# Customer Support Ticket Agent (Simple Agentic AI)

def intent_agent(text):
    text = text.lower()

    if "not working" in text or "error" in text:
        return "Technical Issue"
    elif "not delivered" in text or "delivery" in text:
        return "Delivery Issue"
    elif "refund" in text or "money" in text:
        return "Payment Issue"
    else:
        return "General Query"


def priority_agent(intent):
    if intent in ["Payment Issue", "Technical Issue"]:
        return "High Priority"
    elif intent == "Delivery Issue":
        return "Medium Priority"
    else:
        return "Low Priority"


def response_agent(intent, priority):
    return f"""
Dear Customer,

We have received your complaint regarding: {intent}.
This has been marked as: {priority}.

Our support team will resolve your issue shortly.

Thank you for your patience.
"""


# MAIN PROGRAM
if __name__ == "__main__":

    complaint = input("Enter customer complaint: ")

    intent = intent_agent(complaint)
    priority = priority_agent(intent)
    response = response_agent(intent, priority)

    print("\n--- TICKET ANALYSIS ---")
    print("Intent:", intent)
    print("Priority:", priority)
    print("\n--- RESPONSE ---")
    print(response)