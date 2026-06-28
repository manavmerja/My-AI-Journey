import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

load_dotenv()

def search_wikipedia(query):
    # 1. Setup Brain
    llm = GoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

    # 2. Setup Tools
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
    tools = [wiki_tool]

    # 3. Get Instructions (Prompt)
    prompt = hub.pull("hwchase17/react")

    # 4. Build Agent
    agent = create_react_agent(llm, tools, prompt)

    # 5. Build Executor (The Manager)
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True
    )

    # 6. Run
    response = agent_executor.invoke({"input": f"Search Wikipedia about {query}"})
    return response["output"]

if __name__ == "__main__":
    print(search_wikipedia("Python Programming Language"))
