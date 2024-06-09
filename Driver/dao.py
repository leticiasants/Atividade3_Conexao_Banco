import psycopg
from psycopg.errors import OperationalError, DatabaseError
from model import Order, OrderDetail, Employee, Customer, EmployeeRanking

#Classe com métodos genéricos para execução de queries e processamento dos resultados
class Auxiliar:

    #método que recebe a query a ser executada e seus parâmetros.  Cria a conexão com o banco
    def executar_query(self, sql, parametros):
        try:
            with psycopg.connect(host='localhost', dbname='northwind', user='postgres', password='03122018') as northwind:
                with northwind.cursor() as sessao:
                    sessao.execute(sql, parametros)
                    #checa se o comando executado retornou resultados
                    if sessao.description is not None:
                        colunas_metadado = [desc[0] for desc in sessao.description]
                        return colunas_metadado, sessao.fetchall() #retorna uma tuple com os registros e os metadados para facilitar o processamento
        except OperationalError as e:
            print(f"Erro de conexão: {e}")
            return None
        except DatabaseError as e:
            print(f"Erro no banco de dados: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None

    #método que recebe o conteudo retornado por um select e processa os resultados, de modo a transformá-los em objetos model
    def processar(self, resultados, nome_classe):
        lista_resultados = [] #lista que vai conter os objetos model para retorno
        metadados, registros = resultados #separa os metadados e os registros retornados pela função executar_query
        for registro in registros:
            dicionario = dict(zip(metadados, registro)) #cria um dicionário no qual as chaves são o nome da coluna na tabela
            lista_resultados.append(nome_classe(**dicionario)) #instancia um objeto da classe passada como parâmetro para a função e o coloca na lista de resultados. O dicionário é usado para passar os parâmetros de forma nomeada para o construtor da classe
        return lista_resultados if len(lista_resultados) > 1 else lista_resultados[0] #retorna a lista de resultados se a consulta retornou mais de um registro. Caso contrário, retorna somente o objeto. (útil para quando um registro é filtrado por id nas classes dao)


class OrderDao:
    def __init__(self) -> None:
        self.auxiliar = Auxiliar()

    def inserir(self, pedido):
        sql = "Insert into northwind.orders (orderid, customerid, employeeid, orderdate, requireddate, shippeddate) values (%s,%s,%s,%s,%s,%s)"
        parametros = (pedido.orderid, pedido.customerid,
                      pedido.employeeid, pedido.orderdate, pedido.requireddate, pedido.shippeddate)
        return self.auxiliar.executar_query(sql, parametros)

    def obter(self, id=None):
        sql = 'select * from northwind.orders'
        parametros = None
        if id is not None:
            sql += ' where orderid=%s'
            parametros = (id,)
        res = self.auxiliar.executar_query(sql, parametros)
        return self.auxiliar.processar(res, Order)


class OrderDetailsDao:
    def __init__(self) -> None:
        self.auxiliar = Auxiliar()

    def inserir(self, detalhes_pedido):
        sql = "Insert into northwind.order_details (orderid, productid, quantity) values (%s,%s,%s)"
        parametros = (detalhes_pedido.orderid, detalhes_pedido.productid,
                      detalhes_pedido.quantity)
        self.auxiliar.executar_query(sql, parametros)

    def obter(self, id=None):
        sql = 'select * from northwind.order_details'
        parametros = None
        if id is not None:
            sql += ' where orderid=%s'
            parametros = (id,)
        res = self.auxiliar.executar_query(sql, parametros)
        return self.auxiliar.processar(res, OrderDetail)


class FuncionarioDao:
    def __init__(self):
        self.auxiliar = Auxiliar()

    def obter(self, primeiro_nome=None, ultimo_nome=None):
        sql = 'select * from northwind.employees'
        parametros = None
        if primeiro_nome is not None and ultimo_nome is not None:
            sql += ' where firstname=%s and lastname=%s'
            parametros = (primeiro_nome,ultimo_nome)
        res = self.auxiliar.executar_query(sql, parametros)
        return self.auxiliar.processar(res, Employee)

class RankingFuncionarioDao:
    def __init__(self):
        self.auxiliar = Auxiliar()

    def obter(self, dataIni=None, dataFin=None):
        sql = '''
            SELECT 
                employees.firstname, 
                employees.lastname, 
                COUNT(orders.orderid) AS orders, 
                SUM(order_details.unitprice * order_details.quantity) AS total_value 
            FROM northwind.employees 
            LEFT JOIN northwind.orders ON employees.employeeid = orders.employeeid 
            LEFT JOIN northwind.order_details ON orders.orderid = order_details.orderid
        '''
        parametros = None
        if dataIni is not None and dataFin is not None:
            sql += ' WHERE employees.hiredate BETWEEN %s AND %s'
            parametros = (dataIni, dataFin)
        sql += ' GROUP BY employees.employeeid, employees.firstname, employees.lastname'
        
        res = self.auxiliar.executar_query(sql, parametros)
        return self.auxiliar.processar(res, EmployeeRanking) 


class ClienteDao:
    def __init__(self) -> None:
        self.auxiliar = Auxiliar()

    def obter(self, id=None):
        sql = 'select * from northwind.customers'
        parametros = None
        if id is not None:
            sql += ' where customerid=%s'
            parametros = (id,)
        res = self.auxiliar.executar_query(sql, parametros)
        return self.auxiliar.processar(res, Customer)


