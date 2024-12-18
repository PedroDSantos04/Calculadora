class Calculadora:
    @staticmethod
    def soma(x, y):
        return x + y
    
    @staticmethod
    def subtracao(x, y):
        return x - y 
    
    @staticmethod
    def multiplicacao(x, y):
        return x*y
    
    @staticmethod
    def divisao(x, y):
        if y == 0 or x == 0:
            return 'Erro! Divisão por zero'        
        return x/y
    
    @staticmethod
    def potencia(x, y):
        return x**y
    
    @staticmethod
    def raiz(x, y):
        return x//y
    
    @staticmethod
    def modulo(x, y):
        return x%y
    
    @staticmethod
    def porcentagem(x, y):
        y_porcent = y/100
        return x * y_porcent
    

def opera():
    opera=['soma', 'subtracao', 'multiplicacao', 'divisao', 'potencia', 'raiz', 'modulo', 'porcentagem']
    while True:
            ope = str(input("Digita a operação desejada [soma, subtracao, multiplicacao, divisao, potencia, raiz, modulo, porcentagem]: ")).lower()
            if ope in opera:
                return ope
            print('Opção inválida, tente novamente')

def peg_num(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print("Digite um valor válido")


if __name__ == "__main__":

    ope = opera()
    x = peg_num("Digite o valor de X: ")
    y = peg_num("Digite o valor de Y: ")

    operacoes = {
        'soma': Calculadora.soma,
        'subtracao': Calculadora.subtracao,
        'multiplicacao': Calculadora.multiplicacao,
        'divisao': Calculadora.divisao,
        'potecia': Calculadora.potencia,
        'raiz': Calculadora.raiz,
        'modulo': Calculadora.modulo,
        'porcentagem': Calculadora.porcentagem
    }

    resultado = operacoes[ope](x, y)
    print(f"O resultado é {resultado}")