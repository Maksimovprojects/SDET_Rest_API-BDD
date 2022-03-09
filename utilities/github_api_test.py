import requests

# Authentication. Troubles with autorization

current_session = requests.session()
current_session.auth = auth= ("maximebayer@gmail.com", "Resiver2486mma")
url = "https://api.github.com/user"
url_2 = "https://api.github.com/user/repos"

response_1 = requests.get("https://api.github.com/user", verify=False, auth=("maximebayer@gmail.com", "Resiver2486mma"))
response_2 = current_session.get(url_2)

print(response_1.status_code)
print(response_2.status_code)

