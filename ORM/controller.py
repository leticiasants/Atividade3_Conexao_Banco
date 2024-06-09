from view import View
from dao import Auxiliar, OrderDao, OrderDetailsDao, FuncionarioDao, ClienteDao
from model import Category, Customer, Employee, Product, Shipper, Supplier, Order, OrderDetail

class Controller:
    def __init__(self):
        self.view = View()
        self.auxiliar = Auxiliar()
        self.order = Order()

    def main(self):
        opcao = self.view.main()

        while opcao != 4:
            if opcao == 1:
                self.criarPedido()
            elif opcao == 2:
                self.consultarPedido()
            elif opcao == 3:
                self.rankingFunc()

            opcao = self.view.main()
            
    def criarPedido(self):
        pedido = self.view.criarPedido()
        print(pedido)
        employeeFirstName = pedido[2]
        employeeLastName = pedido[3]
        
        employee = FuncionarioDao.obter(self, employeeFirstName, employeeLastName)
        print(employee)
        employee_id = employee.employeeid
    
        pedido.pop(2)
        pedido.pop(2)
        pedido.insert(2, employee_id)
        print(pedido)
        pedido_Data = Order(
        orderid=pedido[0],
        customerid=pedido[1],
        employeeid=pedido[2],
        orderdate=pedido[3],
        requireddate=pedido[4],
        shippeddate=pedido[5],
        freight=None,
        shipname=None,
        shipaddress=None,
        shipcity=None,
        shipregion=None,
        shippostalcode=None,
        shipcountry=None,
        shipperid=None,
        qtdprodutos=len(pedido[6]),
        maisdesconto=None
    )        
        
        responsePedido = OrderDao.inserir(self,pedido_Data)
        
        if responsePedido is not None:
            for detail in pedido[6]:
                detalhes_pedido = OrderDetail(
                    orderid=pedido[0],
                    productid=detail[0],  
                    unitprice= None,
                    quantity=detail[1],
                    discount=None
                )
                print(detalhes_pedido)
                response = OrderDetailsDao().inserir(detalhes_pedido)
                if response is None:
                    self.view.responseCriarPedido(None)
                    return

        self.view.responseCriarPedido(responsePedido)
    
    def consultarPedido(self):
        pedidoCons = self.view.consultarPedido()
        
        relatorio = OrderDao.obter(pedidoCons)
        self.view.relatorioConsultaPedido(relatorio)
    
    def rankingFunc(self):
        renkingFunc = self.view.rankearFuncionarios()
        
        self.view.relatorioRankingFuncionarios()
    
if __name__ == "__main__":
    controller = Controller()
    controller.main()    
        