import json


with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('lab8/chacon.csv', 'w') as csv_file:
    for repo in data[:5]:
        name = repo.get('name', 'N/A')
        html_url = repo.get('html_url', 'N/A')
        updated_at = repo.get('updated_at', 'N/A')
        visibility = repo.get('visibility', 'N/A')

        csv_file.write(f"{name},{html_url},{updated_at},{visibility}\n")
