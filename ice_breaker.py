import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == '__main__':
    print("hi langchain project")
    summary_template = """
    Given the following LinkedIn profile information {information} about a person, I want you to create:
    1. A short summary of the person in 2-3 sentences.
    2. A list of 2-3 skills that the person possesses.
    """

    summary_promp_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    chain = summary_promp_template | llm

    linkedin_data = scrape_linkedin_profile(
        "https://www.linkedin.com/in/sunmk/",
        mock=True  # Set to False to scrape live data
    )

    res = chain.invoke(
        input={"information": linkedin_data}
    )

    print(res)