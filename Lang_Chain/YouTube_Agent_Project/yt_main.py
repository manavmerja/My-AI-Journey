# Updated YouTube_Agent_Project/yt_main.py 
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def ask_youtube_agent(video_url, query):
    try:
        llm = GoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
        
        # We try to load the transcript
        loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=False)
        video_content = loader.load()

        if not video_content:
            return "Sorry, I couldn't find a transcript for this video."

        prompt = PromptTemplate.from_template("""
            Use the transcript below to answer the question.
            TRANSCRIPT: {transcript}
            QUESTION: {question}
        """)

        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"transcript": video_content[0].page_content, "question": query})

    except Exception as e:
        return f"❌ Error: YouTube blocked the connection. Try a different video link or wait a few minutes. (Details: {e})"


# --- INTERACTIVE MODE ---
if __name__ == "__main__":
    print("\n🎥 WELCOME TO YOUTUBE AI AGENT")
    url = input("Paste YouTube URL: ")
    user_question = input("What do you want to know about this video? ")
    
    print("\n--- 🤖 AGENT IS READING ---")
    answer = ask_youtube_agent(url, user_question)
    print("\n--- 💡 ANSWER ---")
    print(answer)
