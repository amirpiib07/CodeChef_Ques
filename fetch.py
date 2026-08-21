import os
import requests
import json

USERNAME = "amirpiib07"  # quotes ke andar apna username daalein

def sync_codechef():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    # CodeChef recent activities endpoint
    url = f"https://www.codechef.com/api/ratings/all?username=amirpiib07"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching profile: Status {response.status_code}")
            return

        data = response.json()
        os.makedirs("CodeChef_Solutions", exist_ok=True)

        # Profile summary tracker create karna
        summary_path = "CodeChef_Solutions/README.md"
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"# CodeChef Submissions - amirpiib07\n\n")
            f.write(f"- **Current Rating:** {data.get('currentRating', 'N/A')}\n")
            f.write(f"- **Global Rank:** {data.get('globalRank', 'N/A')}\n")
            f.write(f"- **Country Rank:** {data.get('countryRank', 'N/A')}\n\n")
            f.write("### Note\n")
            f.write("Full source code export requires CodeChef OAuth2 API or Browser Extension (CodeSync) due to session protection.\n")

        print("Sync successful.")
    except Exception as e:
        print(f"Failed: {str(e)}")

if __name__ == "__main__":
    sync_codechef()
