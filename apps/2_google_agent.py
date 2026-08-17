from dotenv import load_dotenv
load_dotenv()


from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent

model = ChatGroq(model = 'openai/gpt-oss-20b')
search = GoogleSerperAPIWrapper()

agent = create_agent(
    model = model,
    tools = [search.run],
    system_prompt = "you are an agent and you can search any quesion on google"
)

while True:
    query = input("User: ")
    if query.lower() == "quit":
        print("good bye")
        break

    response = agent.invoke({"messages": [{"role" : "user", "content" : query}]})
    print("AI: ", response["messages"][-1].content)