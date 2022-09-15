from sqlalchemy import create_engine


class Config:
    connstr = "postgresql://postgres:201817005@localhost:5432/botDB"
    engine = create_engine(connstr, echo=False)
    conn = engine.connect()


settings = Config()
