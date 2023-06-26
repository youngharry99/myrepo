import requests

html = requests.get("https://prodharry.com")
print(html.text)