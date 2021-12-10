import requests

response = requests.get('https://github.com/PdxCodeGuild/class_tardigrade/blob/main/1%20Python/docs/15%20Requests.md')

print(response.text)