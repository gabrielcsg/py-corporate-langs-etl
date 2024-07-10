from dotenv import load_dotenv
from math import ceil
import os
import pandas as pd
import requests

load_dotenv()


class DataRepository:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('GITHUB_API_KEY')
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': os.getenv('GITHUB_API_VERSION')
        }

    def repositories_list(self) -> list[list[dict]]:
        repos_list: list[list[dict]] = []
        url = f'{self.api_base_url}/users/{self.owner}'
        response = requests.get(url, headers=self.headers)

        total_repos = response.json().get('public_repos')

        if not isinstance(total_repos, int):
            total_repos = 0

        total_pages = ceil(total_repos / 30)

        for page_num in range(1, total_pages):
            try:
                url = f'''
                    {self.api_base_url}/users/{self.owner}/repos?page={page_num}'''
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list

    def repositoriy_names(self, repos_list: list[list[dict]]) -> list[str]:
        return [repo.get('name') for page in repos_list for repo in page]

    def repository_languages(self, repos_list: list[list[dict]]) -> list[str]:
        return [repo.get('language') for page in repos_list for repo in page]

    def create_df_languages(self) -> pd.DataFrame:
        repositories = self.repositories_list()
        names = self.repositoriy_names(repositories)
        languages = self.repository_languages(repositories)

        data = pd.DataFrame()
        data['repository_name'] = names
        data['language'] = languages

        return data


# Extract and Transform
amazon_rep = DataRepository(owner='amzn')
lang_df_amzn = amazon_rep.create_df_languages()

netflix_rep = DataRepository(owner='netflix')
lang_df_netflix = netflix_rep.create_df_languages()

spotify_rep = DataRepository(owner='spotify')
lang_df_spotify = spotify_rep.create_df_languages()

# Load
lang_df_amzn.to_csv('data/languages_amzn.csv')
lang_df_netflix.to_csv('data/languages_netflix.csv')
lang_df_spotify.to_csv('data/languages_spotify.csv')
