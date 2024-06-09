from datetime import datetime

class View():
    def main(self):
        return self.menu()
    
    def menu(self):
        print('MENU')
        print('1 - Criar pedido')
        print('2 - Consultar um pedido')
        print('3 - Ranking dos funcionários')
        print('4 - Encerrar')
        
        opcao = int(input('O que deseja? '))
        return opcao
    
    def criarPedido(self):
        orderid = int(input('Id do pedido: '))
        customerid = input('Id do cliente: ')
        employeeFirstName = input('Primeiro nome do fúncionário: ')
        employeeLastName = input('Sobrenome do fúncionário: ')
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
        
        pedidoAtributos = [orderid, customerid, employeeFirstName, 
                        employeeLastName, orderdate, requireddate, 
                        shippeddate, products]
        
        return pedidoAtributos
        
    def consultarPedido(self):
        orderid = int(input('Id do pedido para a consulta: '))
        
        return orderid
    
    def relatorioConsultaPedido(self, order, orderDetails):
        if (order is not None):
            print(f'Id do pedido: {order.orderid}')
            print(f'Id do cliente: {order.customerid}')
            print(f'Id do funcionário: {order.employeeid}')
            print(f'Data do pedido: {order.orderdate}')
            print(f'Data necessária: {order.requireddate}')
            print(f'Data de envio: {order.shippeddate}')
            print(f'Produto: {orderDetails.productid}')
            print(f'Quantidade: {orderDetails.quantity}')
            print(f'Preço unitário: {orderDetails.unitprice}')
            print(f'Preço total: {orderDetails.unitprice*orderDetails.quantity}')
        
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
            
    def responseCriarPedido(self, response):
        if(response != None):
            print(response)
        else:
            print("Algo deu errado!")
            