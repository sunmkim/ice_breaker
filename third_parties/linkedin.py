import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        with open("data/mock_profile.json", "r") as f:
            json_data = json.load(f)
            return json_data
    
    

if __name__ == "__main__":
    mock = True  # Set to False to scrape live data
    dt = scrape_linkedin_profile('www.linkedin.com', mock)
    print(dt)
