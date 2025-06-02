import os
from dotenv import load_dotenv
load_dotenv()

from langchain import hub
from langchain_core.prompts import PromptTemplate
from lancghain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent


def lookup(name: str) -> str:
    return ""