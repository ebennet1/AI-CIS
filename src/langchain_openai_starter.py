from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """
    You are an AI Chief of Staff assistant.

    Summarize the following meeting notes:

    {meeting_notes}
    """
)

model = ChatOpenAI(model="gpt-4o-mini")

chain = prompt | model

response = chain.invoke(
    {
        "meeting_notes": "Project is delayed due to unresolved dependencies. Leadership escalation needed."
    }
)

print(response)
