import requests

username = input("Enter your GitHub username: ")
response = requests.get(f"https://api.github.com/users/{username}/events/public")
if response.status_code == 200:
    events = response.json()
    for event in events:
        print(f"{event['type']} at {event['repo']['name']} on {event['created_at']} by {event['actor']['login']}")
else:
    print(f"Error: {response.status_code} - {response.text}")