from dotenv import load_dotenv

load_dotenv()

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    MONGO_URI = f'mongodb+srv://{USER}:{PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true'
    MONGO_DATABASE = f'{DB_NAME}'
    
class ProductionConfig(Config):
    DEBUG = False
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    MONGO_URI = f'mongodb+srv://{USER}:{PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true'
    MONGO_DATABASE = f'{DB_NAME}'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}