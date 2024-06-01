class View():
    def __init__(self):
        return self.menu()
    
    def menu(self):
        print('MENU')
        print('1 - Criar pedido')
        print('2 - Informações sobre pedido')
        print('3 - Ranking dos funcionários')
        print('4 - Encerrar')
        
        opcao = int(input('O que deseja?'))
        return opcao
    
    
    