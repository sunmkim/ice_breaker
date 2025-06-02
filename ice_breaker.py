import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent



def ice_break_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)
    # linkedin_data = scrape_linkedin_profile(
    #     "https://www.linkedin.com/in/sunmk/",
    #     mock=True  # Set to False to scrape live data
    # )

    # set up templates for prompt
    summary_template = """
        Given the following LinkedIn profile information {information} about a person, I want you to create:
        1. A short summary of the person in 2-3 sentences.
        2. A list of 2-3 skills that the person possesses.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # instantiate LLM and chain
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = summary_prompt_template | llm
    res = chain.invoke(
        input={"information": linkedin_data}
    )
    print(res)



if __name__ == '__main__':
    print("Ice breaker started")

    load_dotenv()    
    ice_break_with(name="Sun M. Kim at Fidelity Investments")