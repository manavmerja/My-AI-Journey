from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os


os.environ["LANGCHAIN_PROJECT"] = "Langsmith_sequential_chain"

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model1 = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
model2 = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5)

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

config={
    'tags': ['sequential_chain', 'report_generator'],
    'metadata': {
        'topic': 'Unemployment in India'
    }
    
}

result = chain.invoke({'topic': 'Unemployment in India'}, config=config)

print(result)
