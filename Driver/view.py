from datetime import datetime

class View():
    def __init__(self):
        return self.menu()
    
    def menu(self):
        print('MENU')
        print('1 - Criar pedido')
        print('2 - Consultar um pedido')
        print('3 - Ranking dos funcionários')
        print('4 - Encerrar')
        
        opcao = int(input('O que deseja?'))
        return opcao
    
    def criarPedido(self):
        orderid = int(input('Id do pedido: '))
        customerid = input('Id do cliente: ')
        employeeLastName = input('Primeiro nome do fúncionário: ')
        employeeFirstName = input('Sobrenome do fúncionário: ')
        orderdate = input('Data do pedido (YYYY-MM-DD): ')
        year, month, day = map(int, orderdate.split('-'))
        orderdate = datetime(year, month, day)
        
        requireddate = input('Data necessária (YYYY-MM-DD): ')
        year, month, day = map(int, requireddate.split('-'))
        requireddate = datetime(year, month, day)
        
        shippeddate = input('Data de envio (YYYY-MM-DD): ')
        year, month, day = map(int, shippeddate.split('-'))
        shippeddate = datetime(year, month, day)
        
        addProduto = 1
        products = []
        while addProduto == 1:
            productid = int(input('Id do produto: '))
            quantity = int(input('Quantidade: '))
            
            products.append([productid, quantity])
            
            addProduto = int(input('Deseja inserir mais produtos? \nDigite 1 caso afirmativo e 0 para negativo\n'))
        
        pedidoAtributos = [orderid, customerid, 
                  employeeLastName, employeeFirstName,
                  orderdate, requireddate, shippeddate,
                  products]
        
        return pedidoAtributos
        
    def consultarPedido(self):
        orderid = int(input('Id do pedido para a consulta: '))
        
        return orderid
    
    def relatorioConsultaPedido(self, order):
        if (order is not None):
            print(f'Id do pedido: {order.orderid}')
            print(f'Id do cliente: {order.customerid}')
            print(f'Id do funcionário: {order.employeeid}')
            print(f'Data do pedido: {order.orderdate}')
            print(f'Data necessária: {order.requireddate}')
            print(f'Data de envio: {order.shippeddate}')
            print(f'Produto: {order.productid}')
            print(f'Quantidade: {order.quantity}')
            print(f'Preço unitário: {order.unitprice}')
            print(f'Preço total: {order.unitprice*order.quantity}')
        
        else:
            print("O pedido não existe")
            
            
    def rankearFuncionarios(self):
        print('Diga o intervalo de tempo de xx dos funcionários')
        dataini = input('Data inicial (YYYY-MM-DD): ')
        year, month, day = map(int, dataini.split('-'))
        dataini = datetime(year, month, day)
        
        datafim = input('Data final (YYYY-MM-DD): ')
        year, month, day = map(int, datafim.split('-'))
        datafim = datetime(year, month, day)
        
        intervalo = [dataini, datafim]
        
        return intervalo
    
    def relatorioRankingFuncionarios(self, listEmployees):
        if (listEmployees is not None):
            for employeer in listEmployees:
                print(f'Nome do funcionário: {employeer.lastname} {employeer.firstname}')
                print(f'Total de pedidos: {employeer.orders}')
                print(f'Soma dos valores vendidos: {employeer.value}')
            
        else:
            print("O pedido não existe")