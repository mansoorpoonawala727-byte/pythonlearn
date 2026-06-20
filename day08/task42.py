import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Public repos: {data['public_repos']}")
        print(f"Followers: {data['followers']}")
    else:
        print("User not found!")

get_github_user("mansoorpoonawala727-byte")