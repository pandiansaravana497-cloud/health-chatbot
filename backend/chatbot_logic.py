def get_response(message):
    message = message.lower()

    if "fever" in message:
        return "You may have a fever. Stay hydrated and consult a doctor if it persists."

    elif "headache" in message:
        return "Try resting and drinking water. If severe, consult a doctor."

    elif "covid" in message:
        return "Common symptoms include fever, cough, and fatigue. Consider testing."

    elif "hello" in message or "hi" in message:
        return "Hello! How can I assist you with your health today?"

    else:
        return "I'm not sure. Please consult a healthcare professional."
