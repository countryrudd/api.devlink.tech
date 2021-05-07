class GitHubApiError(Exception):
    """
    Base exception class for GitHub errors
    """

    def __init__(self, errors):
        super().__init__('Request to GitHub resulted in errors.')
        self.errors = errors
