from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate  # <-- 1. Import this
from dotenv import load_dotenv
import os

load_dotenv()

def generate_pet_name(animal_type):  # 2. Add 'animal_type' as a parameter
    llm = GoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

    # 3. Define the Blueprint (The Prompt Template)
    prompt = PromptTemplate.from_template("I have a {animal_type} pet so suggest me five names for it")

    # 4. Create the final question (The Formatted Prompt)
    formatted_prompt = prompt.format(animal_type=animal_type)

    # 5. Send the finished question to the AI
    name = llm.invoke(formatted_prompt)

    return name

if __name__ == "__main__": 
    print(generate_pet_name("elephant"))  # Now you can pass "Cat", "Hamster", etc.
