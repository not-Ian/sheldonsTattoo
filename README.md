This is a script to comment on Sheldon's post about getting a tattoo. Post can be found here: https://www.facebook.com/plankton77/posts/10223870342847047

I'm trying to make this easy enough for a not-so-technical person to use.

## Installation

1. Install Python 3. I'm using 3.6.11. Our versions don't have to be exactly the same. Download python here: https://www.python.org/downloads/
2. Install all the packages this project uses. This can be done by opening up a `terminal` or `command prompt` *(depending on if you're on OSX or Windows)*, navigating to the directory this project is saved in using terminal *(this is done with the `cd`. You might run something like this command to go to my project directory on Windows: `cd ".\Development\python\Sheldons Tattoo"` or something like this command if you're on OSX: `cd "~/Development/python/Sheldons\ Tattoo`)*. Then finally, run this command: `pip install -r requirements.txt`. This should take some time to install everything, and there might be some prompts asking if you're sure you want to download.

3. You'll also need to install a webdriver in order for one of the Python packages "Selenium" to interact with a web browser. Instructions for that can be found here: https://selenium-python.readthedocs.io/installation.html

I downloaded a Google Chrome driver, found here: https://sites.google.com/a/chromium.org/chromedriver/getting-started

---

Almost there. Now that you've downloaded a driver, you'll need to make a file "credentials.json" in the same directory as this project. This file is used to 1. Log into Facebook with your account and make comments. And 2. store the location you just saved that webdriver to. It will include your Facebook email, Facebook password, and webdriver location. It should look something like this:

```
{
    "email": "email@email.com",
    "password": "Password!",
    "chromeDriverLocation": "~/location/to/chromedriver/chromedriver.exe"
}
```

## Using the script

There's three ways to post a commment. You can select a certain method by uncommenting one line from lines 16, 18, or 21. Leave the other two commented out.

A description of each:

1. `paste` - Post comments from whatever you have copied on your clipboard. This method is the fastest.
2. `type` - Posts comments from the text on line 20. This is slower since it types it out manually, rather than copy/pasting like `paste` does. 
3. `script` - Putting various text in a separate file, and having the code read that file line by line, and posting each line separately as a comment. If you want to use your own, save a script as a `.txt` file in this directory, and change line 32 to point to your new script.

There's a variable on line 15 `numComments` - put the number of comments you want to make here if you're using comment type `paste` or `type`.

You can now run the script by opening up your command prompt or terminal and running `python3 ./comment.py`, or running it in your favorite IDE.

#### Misc

It's kind of annoying to stop the script in the middle of running. It'll be trying to type stuff, so you need to go really quickly and `ctrl+c` or whatever command it is to stop.
You can't really do other things with your computer while this is running. Close your eyes and think about Sheldon at a tattoo shop.
The slower methods likely have a lower chance of being caught by Facebook's spam filter? I think the script method probably has the lowest since it 1. paces itself, and 2. has different content for each comment.