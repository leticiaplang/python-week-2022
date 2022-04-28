from sqlmodel import create_engine
from beerlog.config import settings
from beerlog import models

#conecta com url definida
engine = create_engine(settings.database.url)

#cria as tabelas do banco de dados
models.SQLModel.metadata.create_all(engine)

#cria para não expor o engine
def get_session():
    return Session(engine)
