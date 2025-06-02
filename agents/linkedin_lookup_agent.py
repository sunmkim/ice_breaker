import os
from dotenv import load_dotenv
load_dotenv()

from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini"
    )

    str_template = """
    Given the full name {name_of_person}, I want you to return a https link to their LinkedIn profile page. 
    Your answer should only contain a URL.
    """

    prompt_template = PromptTemplate(template=str_template, input_variables=["name_of_person"])

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to retrieve a LinkedIn page URL of a profile"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    # runtime of our agent
    executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    # invoke the agent
    result = executor.invoke(
        input={
            "input": prompt_template.format_prompt(name_of_person=name)
        }
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


# if __name__ == "__main__":
#     linkedin_url = lookup(name="LinkedIn profile of Sun M. Kim at Fidelity Investments")
#     print(linkedin_url)