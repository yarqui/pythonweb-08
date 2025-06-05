class Config:
    SQLALCHEMY_DATABASE_URL = (
        "postgresql+psycopg2://postgres:finalpassword@localhost:5432/contactapp-db"
    )


config = Config()
