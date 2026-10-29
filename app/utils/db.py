import os
import yaml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_PATH = os.path.join(BASE_DIR, 'app', 'config', 'app.yml')

with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)['database']

db_url = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['db_name']}?charset=utf8mb4"

engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()