import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://pmo_user:12345@localhost:5432/pmo_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False