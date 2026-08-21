import os
import requests
import json

# Apna CodeChef username yahan replace karein
USERNAME = "amirpiib07"

def get_recent_submissions():
    # CodeChef public user API endpoint
    url = f"https://www.codechef.com/api/ratings/all?username=amirpiib07"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch user profile data")
        return

    # Folder create karein
    os.makedirs("Submissions", exist_ok=True)
    
    # Submissions info log update karein
    with open("Submissions/log.txt", "a") as f:
        f.write(f"Synced for user: amirpiib07\n")
    
    print("Sync complete.")

if __name__ == "__main__":
    get_recent_submissions()
