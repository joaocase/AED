class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.nivel = 0

    def __str__(self):
        return str(self.value)
    

    def e_folha(self):
        return self.right is None and self.left is None


class Arvore:
    def __init__(self):
        self.init = None
        self.totalNos = 0


    def length(self):
        return self.totalNos
    

    def add(self, value)-> bool:
        no = Node(value)
        self.totalNos += 1
        if not self.init:
            self.init = no
            return True
        else:
            perc = self.init
            while True:
                no.nivel += 1
                if value < perc.value:
                    if not perc.left:
                        perc.left = no
                        break
                    perc = perc.left
                else:
                    if not perc.right:
                        perc.right = no
                        break
                    perc = perc.right


    def __str__(self):
        print(self.init.value)
        print(self.init.left.value)
        print(self.init.right.value)


    def get_perc(self, perc, value, ant=None):
        if not perc or perc.value == value:
            return perc, ant
        elif value > perc.value:
            return self.get_perc(perc.right, value, perc)
        else:
            return self.get_perc(perc.left, value, perc)


    def get(self, value):
        perc = self.init
        if not perc:
            return None
        while perc is not None and perc.value != value:
            if value > perc.value:
                perc = perc.right
            else:
                perc = perc.left
        return perc
    

    def get_min(self, no):
        perc = no
        while perc.left:
            perc = perc.left
        return perc
    

    def get_max(self, no):
        predecessor = no
        while predecessor.right:
            predecessor = predecessor.right
        return predecessor


    def get_sucessor(self, no):
        sucessor = self.get_min(no.right)
        return sucessor
    

    def get_predecessor(self, no):
        perc = self.get_max(no.left)
        return perc
    

    def update_niveis(self, no, nivel=0):
        if no:
            no.nivel = nivel
            self.update_niveis(no.left, nivel+1)
            self.update_niveis(no.right, nivel+1)
    

    def remove(self, value):
        # Para remover, precisa estudar o que e sucessor e predecessor
        #1º encontrar o no
        #2º para encontrar o no, precisamos percorrer
        #com o perc e outro apontador antras de perc
        #3º se o no encontrado for uma folha, remover,
        #para isso, pega a seta que aponta para o no que vai remover, e remove
        #4º .....
        pai = None
        perc = self.init
        while perc and perc.value != value:
            pai = perc
            if value < perc.value:
                perc = perc.left
            else:
                perc = perc.right
        if perc is None:
            return False
        self.totalNos -= 1
        if perc.e_folha():
            if pai is None:
                self.init = None
            elif pai.left == perc:
                pai.left = None
            else:
                pai.right = None
        elif perc.left is None:
            if pai is None:
                self.init = perc.right
            elif pai.left == perc:
                pai.left = perc.right
            else:
                pai.right = perc.right
        elif perc.right is None:
            if pai is None:
                self.init = perc.left
            elif pai.left == perc:
                pai.left = perc.left
            else:
                pai.right = perc.left
        else:
            sucessor_pai = perc
            sucessor = perc.right
            while sucessor.left is not None:
                sucessor_pai = sucessor
                sucessor = sucessor.left
            perc.value = sucessor.value
            if sucessor_pai.left == sucessor:
                sucessor_pai.left = sucessor.right
            else:
                sucessor_pai.right = sucessor.right
        self.update_niveis(self.init)
        return True
    

    def print_ordem(self):
        #https://pythonhelp.wordpress.com/2015/01/19/arvore-binaria-de-busca-em-python/
        # Verificar somente a parte de ordem, pre e pos ordem
        self.__print(self.init, 'em')


    def print_pre_ordem(self):
        self.__print(self.init, 'pre')


    def print_pos_ordem(self):
        self.__print(self.init, 'pos')


    def __print(self, perc, tipo):
        if not perc:
            return
        if tipo == 'pre':
            print(perc.value)
        self.__print(perc.left, tipo)
        if tipo == 'em':
            print(perc.value)
        self.__print(perc.right, tipo)
        if tipo == 'pos':
            print(perc.value)


    def get_nivel_no(self, value):
        #retornar o nivel do no
        no = self.get(value)
        if no:
            return no.nivel
        return None

arvore = Arvore()
#Testando o add
arvore.add(69)
arvore.add(100)
arvore.add(50)
arvore.add(30)
arvore.add(25)
arvore.add(60)
arvore.add(75)
arvore.add(72)
arvore.add(65)
arvore.add(78)
arvore.add(35)

#Testando os prints
print('PRE-----')
arvore.print_pre_ordem()
print('EM-----')
arvore.print_ordem()
print('POS-----')
arvore.print_pos_ordem()

#Testando o get com o get_nivel_no
print(f'Encontrando o número 30: {arvore.get(30)} (Nível: {arvore.get_nivel_no(30)})') #existente
print(f'Encontrando o número 150: {arvore.get(150)}') #inexistente

#Testando o remove com o get_nivel_no
#REMOVENDO O GALHO
print(f'Buscando nível do número 35 (ANTES): {arvore.get_nivel_no(35)}') #número existente
print(f'Buscando nível do número 60 (ANTES): {arvore.get_nivel_no(60)}') #número existente
n = 50
print(f'Removendo o número {n}: {arvore.remove(n)} (Nível: {arvore.get_nivel_no(n)})') #número existente
print(f'Buscando nível do número 35 (DEPOIS): {arvore.get_nivel_no(35)}') #número existente
print(f'Buscando nível do número 60 (DEPOIS): {arvore.get_nivel_no(60)}') #número existente


n2 = 150
print(f'Removendo o número {n2}: {arvore.remove(n2)}') #número inexistente

#REMOVENDO A RAÍZ
print(f'Buscando nível do número 65 (ANTES): {arvore.get_nivel_no(65)}')
print(f'Buscando nível do número 72 (ANTES): {arvore.get_nivel_no(72)}')
arvore.remove(69)
print(f'Buscando nível do número 65 (DEPOIS): {arvore.get_nivel_no(65)}')
print(f'Buscando nível do número 72 (DEPOIS): {arvore.get_nivel_no(72)}')
