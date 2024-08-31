import requests

# GitHub username
username = 'rakibhassan66'

# Function to get language statistics
def get_top_languages(username):
    url = f'https://api.github.com/users/{username}/repos?per_page=100'
    response = requests.get(url)
    repos = response.json()

    # Count the usage of each language
    language_counts = {}
    for repo in repos:
        if 'language' in repo and repo['language']:
            language = repo['language']
            language_counts[language] = language_counts.get(language, 0) + 1

    return language_counts

def update_readme(language_counts):
    # Read the current README content
    with open('README.md', 'r') as file:
        readme_content = file.read()

    # Generate the URL for the top languages card
    languages = list(language_counts.keys())
    count = min(30, len(languages))  # Show up to 30 languages
    top_langs_url = f'https://github-readme-stats.vercel.app/api/top-langs/?username={username}&theme=blue-green&hide_border=true&include_all_commits=true&count_private=true&layout=compact&count={count}'

    # Update README content
    new_readme_content = readme_content.replace(
        '![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=rakibhassan66)',
        f'![Top Languages]({top_langs_url})'
    )

    with open('README.md', 'w') as file:
        file.write(new_readme_content)

if __name__ == "__main__":
    language_counts = get_top_languages(username)
    update_readme(language_counts)
