import os
from dotenv import load_dotenv


class MissingConfigError(Exception):
    pass


class EnvironmentValidator:
    """Class to validate required environment variables."""

    @staticmethod
    def validate_env_vars(required_vars, platform_name):
        """Raise an error if any required environment variable is missing."""
        missing_vars = [var for var in required_vars if os.getenv(var) is None]
        if missing_vars:
            raise MissingConfigError(f"Missing {platform_name} environment variables: {', '.join(missing_vars)}")


class TwitterConfig:
    """Configuration class to store and access Twitter API credentials."""

    REQUIRED_ENV_VARS = [
        'TWITTER_CLIENT_ID', 'TWITTER_CLIENT_SECRET', 'TWITTER_BEARER_TOKEN',
        'TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_TOKEN_SECRET',
        'TWITTER_API_KEY', 'TWITTER_API_KEY_SECRET'
    ]

    def __init__(self):
        EnvironmentValidator.validate_env_vars(self.REQUIRED_ENV_VARS, "Twitter")
        self.client_id = os.getenv('TWITTER_CLIENT_ID')
        self.client_secret = os.getenv('TWITTER_CLIENT_SECRET')
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_key_secret = os.getenv('TWITTER_API_KEY_SECRET')

    def get_credentials(self):
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "bearer_token": self.bearer_token,
            "access_token": self.access_token,
            "access_token_secret": self.access_token_secret,
            "api_key": self.api_key,
            "api_key_secret": self.api_key_secret
        }


class RedditConfig:
    """Configuration class to store and access Reddit API credentials."""

    REQUIRED_ENV_VARS = [
        'REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET',
        'REDDIT_USER_AGENT'
        ] #, 'REDDIT_ACCESS_TOKEN']

    def __init__(self):
        EnvironmentValidator.validate_env_vars(self.REQUIRED_ENV_VARS, "Reddit")
        self.client_id = os.getenv('REDDIT_CLIENT_ID')
        self.client_secret = os.getenv('REDDIT_CLIENT_SECRET')
        self.user_agent = os.getenv('REDDIT_USER_AGENT')
        #self.access_token = os.getenv('REDDIT_ACCESS_TOKEN')

    def get_credentials(self):
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "user_agent": self.user_agent,
            #"access_token": self.access_token
        }


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env

    try:
        twitter_config = TwitterConfig()
        reddit_config = RedditConfig()
        print("Twitter Config:", twitter_config.get_credentials(),"\n")
        print("Reddit Config:", reddit_config.get_credentials())
    except MissingConfigError as e:
        print(f"Configuration Error: {e}")
