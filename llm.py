import os

_model = None

def init_llm():
    """Initializes the chat model for Google Vertex AI."""
    from langchain.chat_models import init_chat_model
    model = init_chat_model(
        os.getenv("GOOGLE_MODEL_ID"),               
        model_provider="google_vertexai"
    )
    global _model
    _model = model
    return model

def get_llm():
    """Returns the chat model. Raises an error if it has not been initialized."""
    if _model is None:
        raise ValueError("LLM not initialized. Ensure init_llm() is called first.")
    return _model
