import base64
from dotenv import load_dotenv
import os
import requests

load_dotenv()


class ManipulateRepositories():
    def __init__(self, username: str) -> None:
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('GITHUB_API_KEY')
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': os.getenv('GITHUB_API_VERSION')
        }

    def create_repo(self, repo_name: str) -> None:
        data = {
            'name': repo_name,
            'description': 'Dados dos repositórios de algumas empresas',
            'private': False,
        }

        url = f'{self.api_base_url}/user/repos'
        response = requests.post(url, headers=self.headers, json=data)

        if (response.status_code == 201):
            print('Repository created successful')
        else:
            print(f'Failed with status_code: {response.status_code}')

    def add_archive(self, repo_name: str, archive_name: str, path_archive: str):
        with open(path_archive, 'rb') as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)

        url_update = f'{
            self.api_base_url}/repos/{self.username}/{repo_name}/contents/{archive_name}'

        data = {
            'message': 'add new archive',
            'content': encoded_content.decode('utf-8')
        }

        response = requests.put(url_update, json=data, headers=self.headers)

        if (response.status_code == 201):
            print('Archive added successful')
        else:
            print(f'Failed with status_code: {response.status_code}')

    def delete_repo(self, repo_name: str) -> None:
        url = f'{self.api_base_url}/repos/{self.username}/{repo_name}'

        response = requests.delete(url, headers=self.headers)

        print(f'delete status_code: {response.status_code}')


new_repo = ManipulateRepositories(os.getenv('USERNAME'))


# create repository
repository_name = 'corporate-language-repository'
# new_repo.delete_repo(repository_name)  # remove repository if exists
new_repo.create_repo(repository_name)

# # add archives
new_repo.add_archive(repository_name, 'languages_amzn.csv',
                     'data/languages_amzn.csv')
new_repo.add_archive(repository_name, 'languages_netflix.csv',
                     'data/languages_netflix.csv')
new_repo.add_archive(repository_name, 'languages_spotify.csv',
                     'data/languages_spotify.csv')
