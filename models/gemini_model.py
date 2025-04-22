from utils.auth import init_vertex_ai
from vertexai.generative_models import GenerativeModel

def call_gemini_model(prompt):
    print("-----")
    init_vertex_ai()
    model = GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
