import os

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_USER = os.getenv("DATABASE_USER", "user")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
DATABASE_NAME = os.getenv("DATABASE_NAME", "authentication_db")
