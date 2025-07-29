# import google.generativeai as genai
# from crewai.llm import BaseLLM
# import os
# os.environ['GOOGLE_API_KEY'] = 'AIzaSyBHeqBtwDslD7kFXrfUDhk2r731DpQHzPg'

# class GeminiLLM(BaseLLM):
#     def __init__(self, model_name="gemini-pro", temperature=0.7):
#         genai.configure(api_key=os.environ["AIzaSyBHeqBtwDslD7kFXrfUDhk2r731DpQHzPg"])
#         self.model = genai.GenerativeModel(model_name)
#         self.temperature = temperature

#     def run(self, prompt: str) -> str:
#         response = self.model.generate_content(prompt, generation_config={"temperature": self.temperature})
#         return response.text


# gemini_llm.py
# gemini_llm.py

import os
import google.generativeai as genai

class GeminiLLM:
    def __init__(self, model_name="gemini-pro", temperature=0.7):
        # ✅ Ensure your key is loaded
        api_key = os.environ.get("AIzaSyBHeqBtwDslD7kFXrfUDhk2r731DpQHzPg")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.temperature = temperature

    def __call__(self, prompt: str) -> str:
        """Allows the class instance to be called like a function"""
        response = self.model.generate_content(prompt, generation_config={
            "temperature": self.temperature,
        })
        return response.text