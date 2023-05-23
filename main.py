class Elevador:

    atual = 0
    pessoas = 0

    def __init__(self, capacidade, andares):
        self.__capacidade = capacidade
        self.__andares = andares

    def entra(self, qtd):
        """Acrescenta uma quantidade de pessoas caso ainda houver espaço."""
        if self.__capacidade>=(Elevador.pessoas + qtd):
            Elevador.pessoas+=qtd
            return f'Agora no elevador estão presentes {Elevador.pessoas} pessoas e sua capacidade máxima é de {self.__capacidade} pessoas.\n'
        return f'Não é possível que entrem mais {qtd} pessoas no elevador pois nele resta(am) {self.__capacidade - Elevador.pessoas} espaço(s).\n'

    def sai(self, qtd):
        """Retira uma certa quantidade de pessoas caso houver no elevador."""
        if Elevador.pessoas>=qtd:
            Elevador.pessoas-=qtd
            return f'Agora o elevador possui {Elevador.pessoas} pessoas e sua capacidade máxima é de {self.__capacidade} pessoas.\n'
        return f'Não é possível que {qtd} pessoas saiam do elevador pois nele há {Elevador.pessoas} pessoas.\n'

    def sobe(self,qtd):
        """Sobe uma quantidade de andares caso o elevador tenha essa possibilidade."""
        if self.__andares > (Elevador.atual + qtd):
            Elevador.atual+=qtd
            return f'O elevador se encontra no {Elevador.atual}ºandar de {self.__andares} andares.\n'
        return f'Não é possível subir {qtd} andar(es), pois restam apenas {self.__andares - Elevador.atual} andares acima.\n'

    def desce(self,qtd):
        """Desce uma quantidade de andares caso o elevador tenha essa possibilidade."""
        if (Elevador.atual+1-qtd)>=0:
            Elevador.atual-=qtd
            return f'O elevador esta no {Elevador.atual}ºandar de {self.__andares} andares.\n'
        return f'O elevador não pode descer {qtd} andar(es), pois restam apenas {Elevador.atual} andares abaixo.\n'

    def info(self):
        """Retorna as informações de quantas pessoas estão no elevador e em qual andar ele está."""
        return f'O elevador está no {Elevador.atual}ºandar de {self.__andares} andares.\nO elevador possui {Elevador.pessoas} pessoas e capacidade máxima de {self.__capacidade} pessoas.\n'


cap = None
while cap is None:
    try:
        cap = int(input('Digite a capacidade máxima de pessoas no elevador: '))
    except ValueError:
        print('Tente novamente!')
andar = None
while andar is None:
    try:
        andar = int(input('Digite quantos andares o prédio possui sem contar com o térreo: '))
    except ValueError:
        print('Tente novamente!')
predio = Elevador(cap, andar)
while True:
    print("MENU DE OPÇÕES:\nDigite 'e' para entrar uma quantidade de indivíduos no elevador.\nDigite 's' para sair uma quantidade de indivíduos do elevador.\nDigite 'u' para subir uma quantidade de andares do elevador.\nDigite 'd' para descer uma quantidade de andares no elevador.\nDigite 'i' para gerar as informações do exato instante no elevador.\nDigite 'sair' para finalizar o programa.\n")
    opc = input('Digite uma opção do menu de opções: ').lower()
    if opc == 'sair':
        exit(1)
    elif opc == 'e':
        quantidade = None
        while quantidade is None:
            try:
                quantidade = int(input('Digite a quantidade de indivíduos que desejam entrar no elevador: '))
            except ValueError:
                print('Tente novamente!')

        print(Elevador.entra(predio, quantidade))
    elif opc == 's':
        quantidade = None
        while quantidade is None:
            try:
                quantidade = int(input('Digite a quantidade de pessoas que deseja que saiam do elevador: '))
            except ValueError:
                print('Tente novamente!')
        print(Elevador.sai(predio, quantidade))
    elif opc == 'u':
        quantidade = None
        while quantidade is None:
            try:
                quantidade = int(input('Digite a quantidade de andares que deseja subir: '))
            except ValueError:
                print('Tente novamente!')
        print(Elevador.sobe(predio, quantidade))
    elif opc == 'd':
        quantidade = None
        while quantidade is None:
            try:
                quantidade = int(input('Digite a quantidade de andares que deseja que o elevador desça: '))
            except ValueError:
                print('Tente novamente!')
        print(Elevador.desce(predio, quantidade))
    elif opc == 'i':
        print(Elevador.info(predio))
    else:
        print('Comanado não reconhecido.')