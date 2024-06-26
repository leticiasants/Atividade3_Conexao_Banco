from datetime import datetime

class View():
    def main(self):
        return self.menu()
    
    def menu(self):
        print('\n --- MENU ---')
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
    
    def relatorioConsultaPedido(self, order, orderDetails, employee):
        if (order is not None):
            print('----')
            print(f'Id do pedido: {order.orderid}')
            print(f'Id do cliente: {order.customerid}')
            print(f'Nome do funcionário: {employee.firstname} {employee.lastname}')
            print(f'Data do pedido: {order.orderdate}')
            print(f'Data necessária: {order.requireddate}')
            print(f'Data de envio: {order.shippeddate}')
            for det in orderDetails:
                print(f'Produto: {det.productid}')
                print(f'Quantidade: {det.quantity}')
                if det.unitprice is not None:
                    print(f'Preço unitário: {det.unitprice}')
                    print(f'Preço total: {det.unitprice*det.quantity}')
        
        else:
            print("O pedido não existe")
            
            
    def rankearFuncionarios(self):
        print('Diga o intervalo de tempo de contratação dos funcionários')
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
                print('\n ---- ')
                print(f'Nome do funcionário: {employeer.firstname} {employeer.lastname}')
                print(f'Total de pedidos: {employeer.orders}')
                print(f'Soma dos valores vendidos: {employeer.total_value}')
            
        else:
            print("Não existe funcionário contratado nesse periodo de tempo")
            
    def responseCriarPedido(self, response):
        if(response != None):
            print(response)
        else:
            print("Algo deu errado!")
            