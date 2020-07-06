import credentials

print("Program is starting...")

old_account = credentials.old_account

print("Signed in to old account.")

new_account = credentials.new_account

print("Signed in to new account.")

def get_subs(account):
    return account.user.subreddits(limit=None)

def get_saved(account):
    return reversed(list(account.user.me().saved(limit=None)))

def follow_subs(account, subs):
    for sub in subs:
        try:
            account.subreddit(sub.display_name).subscribe()
            print("Followed", sub.display_name)
        except Exception as e:
            print(e)

def save_submissions(account, submissions):
    for submission in submissions:
        try:
            account.submission(id=submission.id).save()
            print("Saved", submission.id)
        except Exception as e:
            print(e)

follow_subs(new_account, get_subs(old_account))
save_submissions(new_account, get_saved(old_account))

print("Account transfered.")
print("Program finished.")