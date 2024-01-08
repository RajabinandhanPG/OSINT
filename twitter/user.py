import os
import requests
import json
import argparse

def __user_input() -> str:
    parser = argparse.ArgumentParser(description='Scrape Twitter followers')
    parser.add_argument('-u', '--username', type=str, help='Username to scrape (without @)', required=True)
    args = parser.parse_args()
    return args.username

def get_user_details(username: str) -> dict:
    url = f"https://api.twitter.com/1.1/users/show.json?screen_name={username}"
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_details = response.json()
        print(username)
        return user_details
    else:
        print(f"Error fetching user details for {username}: {response.status_code} {response.reason}")
        return {}

if __name__ == '__main__':
    username = __user_input()
    user_details = get_user_details(username)

    if user_details:
        # Create the directory if it does not exist
        os.makedirs("twitter/users/", exist_ok=True)

        # Write the user details to the file
        filename = f"twitter/users/{username}.json"
        try:
            with open(filename, "w") as f:
                json.dump(user_details, f)
            print(f"User details saved to {filename}")
        except IOError:
            print(f"Error writing user details to {filename}")
