# Reddit Account Transferer
Transfers your old Reddit account's subscribed subreddits and saved posts.

## Description
If you want to transfer your old Reddit account's subscribed subreddits and saved posts to a new account and you are too lazy this script is for you. The script uses "The Python Reddit API Wrapper for short) to transfer your account.

## Getting Started

### What do you need

* First you'll need a Reddit account.
* Then you'll need another Reddit account.
* Next you'll need to install PRAW (Python Reddit API Wrapper). You can install PRAW by opening your command line window and typing ```pip3 install praw```.

### Configuring the script

* You don't need to touch the script file itself ("main.py").
* Put your old Reddit account's credentials to the old_account variable in the "credentials.py" file.
* Put your new Reddit account's credentials to the new_account variable in the "credentials.py" file.
* Congratulations, you're good to go!

### Executing the script

* To run the program simply type ```python main.py``` on the command line.
* Then the program will start subscribing to your old account's subscribed subreddits in your new account.
* Then the program will start saving every post your saved in your old account in your new account.
