from bs4 import BeautifulSoup
import requests
import argparse
import json

# instagram URL
URL = "https://www.instagram.com/{}/"

# parse function
def parse_data(s):
    # creating a dictionary
    data = {}

    # splitting the content
    # then taking the first part
    s = s.split("-")[0]

    # again splitting the content
    s = s.split(" ")

    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]

    # returning the dictionary
    return data

# scrape function
def scrape_data(usernames):
    scraped_data = {}
    for username in usernames:
        # getting the request from url
        r = requests.get(URL.format(username))

        # converting the text
        s = BeautifulSoup(r.text, "html.parser")

        # finding meta info
        meta = s.find("meta", property="og:description")

        # calling parse method
        data = parse_data(meta.attrs['content'])

        # adding username to the data
        data['username'] = username

        # add scraped data for current user to dictionary
        scraped_data[username] = data

    # returning the data dictionary
    return scraped_data

# main function
if __name__ == "__main__":
    # create argument parser
    parser = argparse.ArgumentParser(description="Scrape Instagram data")

    # add username argument
    parser.add_argument("-u", "--usernames", nargs="+", help="Instagram usernames (separate multiple usernames with a space)")

    # parse arguments
    args = parser.parse_args()

    # check if usernames are provided
    if args.usernames:
        # calling scrape function
        data = scrape_data(args.usernames)

        # writing the data to separate files for each user
        for username, user_data in data.items():
            with open('Instagram/users/'+ username + '.json', 'w') as f:
                json.dump({username: user_data}, f, indent=4)
            # printing success message for each user
            print("Scraped data for {} has been saved to {}.json".format(username, username))
    else:
        print("Please provide Instagram usernames with the -u or --usernames argument (separate multiple usernames with a space)")
