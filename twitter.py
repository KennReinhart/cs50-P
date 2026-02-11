import re

url = input("URL: ").strip()
# print(url)

#url.replace, removeprefix
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

username = re.sub(r"^https?://twitter.com/", "", url)
print(f"Username: is now logged in as {username}")