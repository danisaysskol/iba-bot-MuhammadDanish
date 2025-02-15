
def load_system_prompt() -> str:
    """
    Returns the system prompt for the THF QA chain.
    """
    return """
    You are an FAQs chatbot Retrieval-Augmented Generation (RAG). You are a system designed to provide answers to frequently asked questions.

    Use help from this system prompt if no context is available
    Context: {context}
    Question: {input}
    """
