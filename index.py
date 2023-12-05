import requests
import json

# Replace the base URL with your actual API endpoint
base_url = "https://api.codenary.co.kr/techstack/list?page="

# Create an empty list to store all techstack names
all_techstack_names = []

# Loop through pages 1 to 21
for page_number in range(1, 22):
    # Construct the complete URL for the current page
    api_url = base_url + str(page_number)

    # Make a request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()

        # Extract the "name" from each "techstack"
        techstack_names = [entry['techstack']['name'] for entry in json_data['techstacks']]

        # Add the names to the overall list
        all_techstack_names.extend(techstack_names)
    else:
        print(f"Failed to retrieve data for page {page_number}. Status code: {response.status_code}")

# Save the list of names to a JSON file 
with open("techstack_names.json", "w", encoding="utf-8") as json_file:
    json.dump(all_techstack_names, json_file, ensure_ascii=False, indent=2)

print("Techstack names have been saved to techstack_names.json")
