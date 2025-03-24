from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from routers import process, stream
import os
import json
import tempfile
from dotenv import load_dotenv
from google.oauth2 import service_account
from google.cloud import aiplatform

# Import initialization functions
from embeddings import init_embeddings
from llm import init_llm

# Load environment variables at module level
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Check for credentials in environment variables
    service_account_info = os.getenv("GOOGLE_CREDENTIALS")
    if not service_account_info:
        # Fall back to previously used variable name
        service_account_info = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    
    if service_account_info:
        try:
            # Remove any backticks if present (optional)
            service_account_info_fixed = service_account_info.replace("`", "")
            # Replace single quotes with double quotes if necessary
            service_account_info_fixed = service_account_info_fixed.replace("'", '"')
            # Escape newline characters (replace literal newlines with the escaped form)
            service_account_info_fixed = service_account_info_fixed.replace("\n", "\\n")
            
            # Parse the credentials JSON string
            credentials_info = json.loads(service_account_info_fixed)
            
            # Create credentials object directly
            credentials = service_account.Credentials.from_service_account_info(credentials_info)
            # Extract project ID from credentials
            project_id = credentials_info.get("project_id")
            print("project id:", project_id)
            
            if project_id:
                # Write the credentials JSON to a temporary file and set GOOGLE_APPLICATION_CREDENTIALS
                with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as f:
                    json.dump(credentials_info, f)
                    temp_creds_path = f.name
                os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = temp_creds_path
                
                # Initialize Google Cloud client libraries directly with the credentials
                aiplatform.init(
                    project=project_id,
                    credentials=credentials
                )
                # Optionally, also store the raw JSON in another env variable if needed
                os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"] = service_account_info
                os.environ["VERTEX_PROJECT_ID"] = project_id
                
                print(f"Successfully initialized Google Cloud with project ID: {project_id}")
            else:
                print("ERROR: No project_id found in credentials")
        except json.JSONDecodeError as e:
            print("ERROR: Invalid JSON in credentials environment variable:", e)
    else:
        print("WARNING: No Google credentials found in environment variables")
    
    # Now that the credentials are set, initialize embeddings and LLM.
    app.state.embeddings, app.state.vector_store = init_embeddings()
    app.state.llm_model = init_llm()

    yield  # Startup complete

# Create FastAPI instance with lifespan
api = FastAPI(lifespan=lifespan)

# Middleware to allow CORS for your frontend
api.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "https://your-frontend-project.vercel.app",
        os.getenv("FRONTEND_URL", "")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
api.include_router(process.router)
api.include_router(stream.router)

# Health check endpoint
@api.get("/")
async def health_check():
    return {"status": "healthy"}
