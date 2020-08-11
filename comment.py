from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyautogui import press, typewrite, hotkey
from bs4 import BeautifulSoup
import json
import time
import random

def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type("Enum", (), enums)
CommentType = enum("paste", "type", "script")


numComments = 500 # Only used for paste/type. You probably shouldn't do something like 100 thousand
# commentMode = CommentType.paste # paste text from clipboard repeatedly (fastest)

# commentMode = CommentType.type # type out something specific over and over (slower, might have a lower chance of being spotted by FB's spam filter?)
commentToType = "Type whatever you want to be commented here"

commentMode = CommentType.script # read from external file and post each comment separately (slowest, funniest)

with open("./credentials.json", 'r') as file:
    credentials = json.load(file)

# Do something fun. Save a script (or a book or anything) as a '.txt' file, then load it here.
# Separate lines that should be comments by new lines.
# See frankendoodle.txt 
scriptLines = []
scriptIndex = 0
with open("./frankendoodle.txt", 'r') as file:
    scriptLines = file.readlines() 
            

emailCredentials = credentials["email"]
passwordCredentials = credentials["password"]
chromeDriverLocation = credentials["chromeDriverLocation"]

driver = webdriver.Chrome(chromeDriverLocation)
driver.get("https://www.facebook.com/plankton77/posts/10223870342847047")

email = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

email.send_keys(emailCredentials)
password.send_keys(passwordCredentials)
password.send_keys(Keys.RETURN)

time.sleep(10)

def postComment():
    global scriptIndex
    # https://stackoverflow.com/questions/13564851/how-to-generate-keyboard-events-in-python
    # https://github.com/asweigart/pyautogui

    if commentMode == CommentType.paste:
        # If you copy whatever you want to post onto your clipboard, the script can paste it instead of typing it manually each time
        hotkey('ctrl', 'v')
    elif commentMode == CommentType.type:
        # Whatever you want to spam on Sheldon's post. Much faster if you just copy it and let the script paste for you.
        typewrite(commentToType, interval=0.1)
    elif commentMode == CommentType.script:
        text = scriptLines[scriptIndex]
        typewrite(text, interval=0.1)
        scriptIndex = scriptIndex + 1

    # time.sleep(...) is just a pause - I'm thinking it'll help us avoid Facebook's antispam filter a little bit?
    time.sleep(0.5)
    hotkey('\n')

def findCommentField():
    # TODO: See if alert was thrown that you've hit a comment spam filter? Check if certain wording appears in driver.page_source?
    # 1. Tap "Okay"?
    # 2. time.sleep(1 hour)?
    # 3. Continue the process?

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup.find_all('div')

    # I know this is kind of hacky, but something about Facebook changing HTML div class names
    # after you post a comment makes it difficult to find the comment box otherwise, I think.
    for div in divs:
        if div.get('contenteditable'):
            divClass = div.get('class')[-1]

            commentField = driver.find_element_by_xpath("//div[contains(@class, '" + divClass + "')]")
            time.sleep(1)
                    
            try:
                # I haven't gotten it to work where it actually types using Selenium's built-in `send_keys("...")`` method. 
                # `send_keys("...")` might work after you post the first comment?? Not sure. Facebook's HTML is weird.
                # So, we're using a different package for typing comments: pyautogui
                commentField.send_keys(" ")
                postComment()
                break
            except:
                # The first time you find the text field the page reloads so you can't type into it? 
                # It throws an error, but the cursor is still in the textbox, and we can type using a different package.
                postComment()
                break

if commentMode == 3:
    while scriptIndex < len(scriptLines):
        findCommentField()
else:
    for _ in range(numComments):
        findCommentField()
    
driver.close()