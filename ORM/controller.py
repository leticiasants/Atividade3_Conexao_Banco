from view import View
from dao import OrderDao, OrderDetailsDao, FuncionarioDao, ClienteDao, RankingFuncionarioDao
from model import Category, Customer, Employee, Product, Shipper, Supplier, Order, OrderDetail

class Controller:
    def __init__(self):
        self.view = View()
        self.orderDao = OrderDao()
        self.orderDetailsDao = OrderDetailsDao()
        self.funcionarioDao = FuncionarioDao()
        self.rankingFuncionarioDao = RankingFuncionarioDao()

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
        pedido_atributos = self.view.criarPedido()
        
        employeeFirstName = pedido_atributos[2]
        employeeLastName = pedido_atributos[3]
        
        try:        
            employee = self.funcionarioDao.obter(employeeFirstName, employeeLastName)
            pedido = Order(orderid=pedido_atributos[0], customerid=pedido_atributos[1], orderdate=pedido_atributos[4],requireddate=pedido_atributos[4],shippeddate=pedido_atributos[5],employeeid=employee.employeeid)
            self.orderDao.inserir(pedido)
            for prod in pedido_atributos[7]:
                self.orderDetailsDao.inserir(OrderDetail(orderid=pedido_atributos[0],productid=prod[0],quantity=prod[1]))
        
            self.view.responseCriarPedido(1)
        except Exception as e:
            self.view.responseCriarPedido(None)
    
    def consultarPedido(self):
        pedidoCons = self.view.consultarPedido()
        pedido = self.orderDao.obter(pedidoCons)
        detalhes = self.orderDetailsDao.obter(pedidoCons)
        vendedor = self.funcionarioDao.obterFuncionarioPorId(pedido.employeeid)
        self.view.relatorioConsultaPedido(pedido, detalhes, vendedor)

        
    
    def rankingFunc(self):
        datas = self.view.rankearFuncionarios()
        dataIni = datas[0]
        dataFin = datas[1]
        ranking = RankingFuncionarioDao.obter(self, dataIni, dataFin)
        
        self.view.relatorioRankingFuncionarios(ranking)
    
if __name__ == "__main__":
    controller = Controller()
    controller.main()    
        