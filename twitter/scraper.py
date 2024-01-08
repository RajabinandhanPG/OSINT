import os
import time
import argparse
import json
from threading import Thread
from time import sleep
from os import _exit
from requests import session
from ui import UI


class Scraper:
  def __init__(self, username: str) -> None:
    self.username: str = username
    self.headers: dict = {
      'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'}
    self.scraped: int = 0

  def __save_results(self, users: list) -> None:
    with open(f"twitter/users/{self.username}_followers.json", "w") as f:
      json.dump(users, f)

  def __display(self) -> None:
    while True:
      print(f"{ui.prefix} Scraped: {self.scraped:,}", end="\r")
      sleep(1.22)

  def __get_cursor(self) -> str:
    cursor = session.get(f"https://api.twitter.com/1.1/followers/list.json?screen_name={self.username}&count=200",
                         headers=self.headers).json()
    try:
      cursor = cursor["next_cursor_str"]
      return cursor
    except:
      print(f"{ui.prefix} Unable to grab cursor, check the username again!")
      _exit(0)

  def __scrape(self, cursor: str) -> bool:
    users = []
    while cursor != '0':
      scrape = session.get(
        f"https://api.twitter.com/1.1/followers/list.json?screen_name={self.username}&count=200&cursor={cursor}",
        headers=self.headers).json()
      cursor = scrape["next_cursor_str"]
      user_list = scrape["users"]
      for user in user_list:
        user_data = {
          "name": user["name"],
          "screen_name": user["screen_name"],
          "description": user["description"],
          "location": user["location"],
          "followers_count": user["followers_count"],
          "friends_count": user["friends_count"],
          "statuses_count": user["statuses_count"],
          "verified": user["verified"],
          "created_at": user["created_at"],
        }
        self.scraped += 1
        users.append(user_data)
      sleep(1)
    self.__save_results(users)
    return True

  def _handle(self) -> None:
    ui.clear()
    Thread(target=self.__display).start()
    cursor = self.__get_cursor()
    scrape = self.__scrape(cursor)
    if scrape:
      print(
        f"{ui.prefix} Successfully scraped {ui.red}{self.scraped:,}{ui.reset} followers from {ui.red}@{self.username}{ui.reset}.")
      _exit(0)


def __user_input() -> str:
  parser = argparse.ArgumentParser(description='Scrape Twitter followers')
  parser.add_argument('-u', '--username', type=str, help='Username to scrape (without @)', required=True)
  args = parser.parse_args()
  return args.username


if __name__ == "__main__":

	ui = UI()
	session = session()
	username = __user_input()

	scraper = Scraper(username)
	scraper._handle()