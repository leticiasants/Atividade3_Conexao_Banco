from view import View
from dao import Auxiliar, OrderDao, OrderDetailsDao, FuncionarioDao, ClienteDao

class Controller:
    def __init__(self):
        self.view = View()

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
        
        employeeFirstName = pedido[2]
        employeeLastName = pedido[3]
        
        employeeid = FuncionarioDao.obter(employeeFirstName, employeeLastName)
        pedido.append(employeeid)
        
        responsePedido = OrderDao.inserir(pedido)
        
        if responsePedido != None:
            response = 1
            while response != None:
                for prodQuant in pedido[7]:
                    detalhes_pedido = []
                    detalhes_pedido.append(pedido[0])
                    
                    for prod in prodQuant:
                        detalhes_pedido.append(prod)
                    
                response = OrderDetailsDao.inserir(detalhes_pedido)
        
        self.view.responseCriarPedido(response)
    
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
        