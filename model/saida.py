from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String, DateTime, Integer
from sys import path
from datetime import datetime
class Saida():
    __tablename__ = "entrada"
    valor = Column(Float)
    data = Column(DateTime)
    obs = Column(String)
    id = Column(Integer, primary_key = True)

    def __init__(self):
        self.engine = create_engine("sqlite:///{}/model/SQL/base.db".format(path[0]), echo=True)
        self.conn = self.engine.connect()
    
    def adicionarSaida(self, valor, obs=""):
        self.engine.execute("INSERT INTO saida (valor, data, obs) VALUES ('{}', '{}', '{}')".format(valor, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), obs))

    def listarSaidas(self):
        return (self.engine.execute("SELECT * FROM saida")).fetchall()

