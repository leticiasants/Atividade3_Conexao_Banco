from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Order, OrderDetail, Employee, Customer

# Configurar o motor SQLAlchemy
DATABASE_URL = 'postgresql://postgres:root@localhost/northwind' # Trocar a senha e o usuario caso seja necessário
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class Auxiliar:
    def __init__(self):
        self.session = Session()

    def executar_query(self, query):
        try:
            result = self.session.execute(query)
            return result
        except Exception as e:
            print(f"Erro inesperado: {e}")
            self.session.rollback()
            return None

    def processar(self, resultados, modelo_classe):
        lista_resultados = []
        for registro in resultados:
            lista_resultados.append(modelo_classe(**registro))
        return lista_resultados if len(lista_resultados) > 1 else lista_resultados[0]

class OrderDao:
    def __init__(self) -> None:
        self.auxiliar = Auxiliar()

    def inserir(self, pedido):
        try:
            self.auxiliar.session.add(pedido)
            self.auxiliar.session.commit()
        except Exception as e:
            print(f"Erro ao inserir pedido: {e}")
            self.auxiliar.session.rollback()

    def obter(self, id=None):
        try:
            if id is not None:
                res = self.auxiliar.session.query(Order).filter(Order.orderid == id).all()
            else:
                res = self.auxiliar.session.query(Order).all()
            return res
        except Exception as e:
            print(f"Erro ao obter pedido: {e}")
            return None

class OrderDetailsDao:
    def __init__(self) -> None:
        self.auxiliar = Auxiliar()

    def inserir(self, detalhes_pedido):
        try:
            self.auxiliar.session.add(detalhes_pedido)
            self.auxiliar.session.commit()
        except Exception as e:
            print(f"Erro ao inserir detalhes do pedido: {e}")
            self.auxiliar.session.rollback()

    def obter(self, id=None):
        try:
            if id is not None:
                res = self.auxiliar.session.query(OrderDetail).filter(OrderDetail.orderid == id).all()
            else:
                res = self.auxiliar.session.query(OrderDetail).all()
            return res
        except Exception as e:
            print(f"Erro ao obter detalhes do pedido: {e}")
            return None

class FuncionarioDao:
    def __init__(self) -> None:
        self.auxiliar = Auxiliar()

    def obter(self, primeiro_nome=None, ultimo_nome=None):
        try:
            if primeiro_nome is not None and ultimo_nome is not None:
                res = self.auxiliar.session.query(Employee).filter(Employee.firstname == primeiro_nome, Employee.lastname == ultimo_nome).all()
            else:
                res = self.auxiliar.session.query(Employee).all()
            return res
        except Exception as e:
            print(f"Erro ao obter funcionário: {e}")
            return None

class ClienteDao:
    def __init__(self) -> None:
        self.auxiliar = Auxiliar()

    def obter(self, id=None):
        try:
            if id is not None:
                res = self.auxiliar.session.query(Customer).filter(Customer.customerid == id).all()
            else:
                res = self.auxiliar.session.query(Customer).all()
            return res
        except Exception as e:
            print(f"Erro ao obter cliente: {e}")
            return None

