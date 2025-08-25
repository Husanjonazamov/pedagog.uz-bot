from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
ADMIN = env('ADMIN')
WEB_URL = env('WEB_URL')
IMAGE_ID = env('IMAGE_ID')
BASE_URL = env('BASE_URL')

