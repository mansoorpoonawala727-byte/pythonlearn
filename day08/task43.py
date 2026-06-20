import requests
import json

def save_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        with open(f"{username}_info.json", "w") as f:
            json.dump(data, f, indent=4)
        
        print(f"Saved {username}'s info to {username}_info.json")
    else:
        print("User not found!")

save_github_user("mansoorpoonawala727-byte") 