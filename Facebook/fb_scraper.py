import os
import requests
import json
from argparse import ArgumentParser
from facebook_scraper import get_profile, set_cookies
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

# Define the command line arguments
parser = ArgumentParser()
parser.add_argument("-u", "--username", dest="username", required=True,
                    help="The Facebook username to scrape")
args = parser.parse_args()

# Replace these with your own Facebook login cookies
cookies = {
    'datr': 'PwwyZOsBfXX1QblvXq7RdXXL',
    'sb': 'bWRMZJ90e6xZ8V3-i-CDM3nL',
    'c_user': '100004889646019',
    'xs': '35%3A-JNjLxCYiKbNLA%3A2%3A1682728407%3A-1%3A5653',
    'fr': '0FVbdeFhB1pvfZrgy.AWXCoMCE0Zc-SXnBKCYYZuwAWTk.BkTGRt.5F.AAA.0.0.BkTGXW.AWWv69936vw',
}

# Set the cookies
set_cookies(cookies)

# Scrape the profile
profile_data = get_profile(args.username)

# Extract the name of the profile
profile_name = profile_data["Name"]

# Save the profile data to a JSON file
with open(f"Facebook/user/{profile_name}.json", "w") as f:
    json.dump(profile_data, f, cls=CustomEncoder)
