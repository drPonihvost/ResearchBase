import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    TITLE = 'ResearchBase'
    VERSION = '0.0.1'
    DESCRIPTION = '''Service for registration of incoming research directions'''
    NAME = 'drPonihvost'
    EMAIL = 'kudrovpn@gmail.com'
    TAGS_METADATA = [
                        {
                            'name': 'Research',
                            'description': 'Everything related to the registration of directions'
                        },
                        {
                            'name': 'Person',
                            'description': 'Everything related to the person in research'
                        }
                    ],
    SQLALCHEMY_DATABASE_URL = f'sqlite:///{os.path.dirname(__file__)}\\{os.getenv("DATABASE_NAME")}'


settings = Settings()
