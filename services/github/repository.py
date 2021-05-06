from services.github.util import github_request


def get_repositories(github_username: str) -> list:
    """
    Returns repositories
    @param github_username: A GitHub user's username
    @return: a list of repositories
    """
    return github_request('GET', f'/users/{github_username}/repos').json()
