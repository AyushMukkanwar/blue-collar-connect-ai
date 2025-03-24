import os

# Directory for your persisted Chroma database
CHROMA_DB_DIR = "./my_chroma_db"

# Module-level variable for the vector store (initialized later)
_vector_store = None

def init_embeddings():
    """Initializes the Vertex AI embeddings and creates the vector store.
    
    Returns:
        tuple: (embeddings, vector_store)
    """
    from langchain_google_vertexai import VertexAIEmbeddings
    from langchain_chroma import Chroma

    embeddings = VertexAIEmbeddings(model=os.getenv("EMBEDDINGS_MODEL_ID"))
    
    global _vector_store
    _vector_store = Chroma(embedding_function=embeddings, persist_directory=CHROMA_DB_DIR)
    
    return embeddings, _vector_store

def get_vector_store():
    """Returns the vector store. Raises an error if it has not been initialized."""
    if _vector_store is None:
        raise ValueError("Vector store not initialized. Ensure init_embeddings() is called first.")
    return _vector_store
