from view import View
from dao import Dao

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
        self.dao.OrderDao.inserir(pedido)
    
    def consultarPedido(self):
        pass
    
    def rankingFunc(self):
        pass
    
if __name__ == "__main__":
    controller = Controller()
    controller.main()    
        