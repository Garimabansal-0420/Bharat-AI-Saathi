def chatbot_response(message):

    message = message.lower()

    if "scheme" in message:
        return "Please enter your details to get personalized scheme recommendations."

    if "document" in message:
        return "Documents usually include Aadhar, Income Certificate, Caste Certificate."

    return "I am your AI assistant. Ask me about government schemes."
