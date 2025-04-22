from google.oauth2.service_account import Credentials
import vertexai
from config.settings import API_KEY_PATH, REGION

def init_vertex_ai():
    credentials = Credentials.from_service_account_file(
        API_KEY_PATH,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )

    project_id = credentials.project_id
    vertexai.init(project=project_id, location=REGION, credentials=credentials)
    #return project_id  # Optional if you need it elsewhere
