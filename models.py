from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, Float, DateTime, func, String
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash


engine = create_engine('mysql+pymysql://usuario:senha@localhost:3306/nome_banco')

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Funcionario(Base, UserMixin):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(DateTime, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    cargo = Column(String, nullable=False)
    salario = Column(Float, nullable=False)
    criado_em = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f'<Funcionario {self.nome}>'

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)
