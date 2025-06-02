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
        data = json_data.get("person")
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )
        data = response.json().get("person")

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None, '', "") and k not in ["certifications"]
    }
    print(data)
    return data

if __name__ == "__main__":
    mock = False  # Set to False to scrape live data
    scrape_linkedin_profile('https://www.linkedin.com/in/sunmk/', mock)
