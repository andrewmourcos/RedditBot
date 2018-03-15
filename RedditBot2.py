# importing modules for reddit API and a config file containing password,
# client id and client secret
import praw
import time
import config
import random

# logging into reddit using praw module and credentials
# from config file
def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Massachussetts incorrection responder v0.1")
    return r

def run_bot(r, replied_to, incorrections, n):
    # look for comments in r/bottest containing words in "incorrections" list
    for comment in r.subreddit('bottest').comments(limit=20):
        for word in incorrections:
            if word in comment.body and comment.id not in replied_to and not comment.author == r.user.me():
                incorrections.remove(word)
                print "String found"
                print(comment.author)
                randword = incorrections[n]
                string = "\* I believe it's spelled %s \n\n  \n\n beep boop I'm just kidding, that's not actually how it's spelled, but you may want to revise your comment... ;) " %(randword)
                comment.reply(string)
                print(randword)
                print "replied to comment"
                replied_to.append(comment.id)
                time.sleep(10)

# List of IDs for ppl already replied to (to not send the same comment
# over and over again)
replied_to = []

while 1:
    r = bot_login()
    print "logged in"
    try:
        while 1:
            # list of possible words to comment
            incorrections = ["Massachussetts", "Masachussetts",
                                "Massachussets", "Masachusets", "Mazdachusets",
                                "massachusets", "massachussetts",
                                "masachussetts", "massachussets", "masachusets",
                                "mazdachusets"]
            n = random.randint(0, 3)
            run_bot(r, replied_to, incorrections, n)
    except Error as e:
        print(e)
        time.sleep(600)
        print "trying again"
