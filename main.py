from models.gemini_model import call_gemini_model

if __name__ == "__main__":
    print("process started")
    result = call_gemini_model("Give me 5 facts about GCP.")
    print(result)
