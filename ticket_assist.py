from dotenv import load_dotenv
import os



passw = os.getenv('ENV', 'local')
load = f".env.{passw}"
load_dotenv(load)
