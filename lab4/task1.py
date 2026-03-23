import webbrowser
import random


url_collection = [
    "https://github.com",
    "http://redis.io",
    "https://www.python.org",
    "https://www.github.com"
]

random.shuffle(url_collection)
selected_website = url_collection.pop()

print("Navigating to:", selected_website)

# Calling the browser
webbrowser.open(selected_website)