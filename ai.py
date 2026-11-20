import os
from langchain_openrouter import ChatOpenRouter


def get_ai_response(prompt):
    llm = ChatOpenRouter(
        model="openrouter/free",
        api_key=os.environ["OPENROUTER_API_KEY"]
    )

    response = llm.invoke(prompt)

    return response.content
