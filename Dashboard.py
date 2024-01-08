import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import customtkinter
from customtkinter import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.notebook = None
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.configure(bg='#333333')
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master, width=1200, height=600)
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background="white",foreground="black")
        style.configure("TNotebook.Tab", padding=(30, 20), font=('Arial', 20), anchor='center', width=130)
        style.map("TNotebook", background=[("selected", "#333333")])

        # create Twitter tab
        self.twitter_tab = CTkFrame(self.notebook, width=400, height=50, fg_color="#333333")
        self.notebook.add(self.twitter_tab, text="Twitter")

        self.username_label = CTkLabel(self.twitter_tab, text="Enter Twitter Username:", font=('Arial', 20))
        self.username_label.pack(padx=40, pady=20)
        self.username_entry = CTkEntry(self.twitter_tab, width=400, height=50, font=('Arial', 20))
        self.username_entry.pack(padx=40, pady=20)

        # create new button for running the command with the entered username
        self.run_button = CTkButton(self.twitter_tab, text="Get User Info", command=self.run_command,
                                    font=('Arial', 20), width=400, height=50)
        self.run_button.pack(padx=20, pady=20)

        self.submit_button = CTkButton(self.twitter_tab, text="Get User Followers Information", command=self.submit,
                                       font=('Arial', 20), width=400, height=50)
        self.submit_button.pack(padx=20, pady=20)

        # Tweets button
        self.run_button = CTkButton(self.twitter_tab, text="Get all Tweets", command=self.tweets_submit,
                                    font=('Arial', 20), width=400, height=50)
        self.run_button.pack(padx=20, pady=20)

        # create Facebook tab
        self.facebook_tab = CTkFrame(self.notebook, width=400, height=50, fg_color="#333333")
        self.notebook.add(self.facebook_tab, text="Facebook")

        self.username_label2 = CTkLabel(self.facebook_tab, text="Enter Facebook Username:", font=('Arial', 20))
        self.username_label2.pack(padx=40, pady=20)
        self.username_entry2 = CTkEntry(self.facebook_tab, width=400, height=50, font=('Arial', 20))
        self.username_entry2.pack(padx=40, pady=20)

        self.submit_button2 = CTkButton(self.facebook_tab, text="Get User Information", command=self.submit2,
                                        font=('Arial', 20), width=400, height=50)
        self.submit_button2.pack(padx=20, pady=20)

        # create Instagram tab
        self.instagram_tab = CTkFrame(self.notebook, width=400, height=50, fg_color="#333333")
        self.notebook.add(self.instagram_tab, text="Instagram")

        self.username_label3 = CTkLabel(self.instagram_tab, text="Enter Instagram Username:", font=('Arial', 20))
        self.username_label3.pack(padx=40, pady=20)
        self.username_entry3 = CTkEntry(self.instagram_tab, width=400, height=50, font=('Arial', 20))
        self.username_entry3.pack(padx=40, pady=20)

        self.submit_button3 = CTkButton(self.instagram_tab, text="Get User Information", command=self.submit3,
                                        font=('Arial', 20), width=400, height=50)
        self.submit_button3.pack(padx=20, pady=20)

        # set tab position to top
        self.notebook.pack(side='top', fill=tk.BOTH, expand=True, padx=20, pady=20)


    def run_command(self):
        username = self.username_entry.get()
        os.system(f"python twitter/user.py -u {username}")
        messagebox.showinfo("Task Complete", "The command has been run!")

    def submit(self):
        username = self.username_entry.get()
        os.system(f"python twitter/scraper.py -u {username}")
        messagebox.showinfo("Task Complete", "The scraping process has completed!")

    def tweets_submit(self):
        username = self.username_entry.get()
        os.system(f"python twitter/tweets.py -u {username}")
        messagebox.showinfo("Task Complete", "The scraping process has completed!")

    def submit2(self):
        username = self.username_entry2.get()
        print(username)
        os.system(f'python Facebook/fb_scraper.py -u "{username}"')
        messagebox.showinfo("Task Complete", "The scraping process has completed!")

    def submit3(self):
        username = self.username_entry3.get()
        print(username)
        os.system(f'python Instagram/Insta_scraper.py -u "{username}"')
        messagebox.showinfo("Task Complete", "The scraping process has completed!")


root = tk.Tk()
root.geometry("900x700")
root.title("OSNIT Dashboard")
app = Application(master=root)
app.mainloop()
