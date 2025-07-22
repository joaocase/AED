class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Aluno:
    def __init__(self, nome, matricula, status=True):
        self.nome = nome
        self.matricula = matricula
        self.status=status


    def __str__(self):
        return f'------------------------\nNome: {self.nome}\nMatrícula: {self.matricula}\nStatus: {self.status}\n------------------------'


class List:
    def __init__(self):
        self.init = None
        self.end = None

    def add(self, value)-> bool:
        #Regras:
        #1 - Só pode aceitar value do tipo Aluno
        #2 - Não pode ter matricula repetida
        if not isinstance(value, Aluno):
            return "\033[31mValor inválido! Tente novamente.\033[m"
        if self.get_document(value.matricula):
            return "\033[31mMatrícula repetida! Tente novamente.\033[m"
        no = Node(value)
        if self.init is None:
            self.init = no
            self.end = no
        else:
            self.end.next = no
            self.end = no
        return "\033[32mAdicionado com sucesso!\033[m"
    

    def insert(self, index, value)-> bool:
        #Regras:
        #1 - Só pode aceitar value do tipo Aluno
        #2 - Não pode ter matricula repetida
        if not isinstance(value, Aluno):
            return "\033[31mValor inválido! Tente novamente.\033[m"
        if self.get_document(value.matricula):
            return "\033[31mMatrícula repetida! Tente novamente.\033[m"
        no = Node(value)
        if index == 0:
            no.next = self.init
            self.init = no
            if self.end is None:
                self.end = no
            return "\033[32mAdicionado com sucesso!\033[m"
        percorredor = self.init
        noAnterior = None
        contador = 0
        while percorredor and contador < index:
            noAnterior = percorredor
            percorredor = percorredor.next
            contador += 1
        if percorredor is None and contador < index:
            return self.add(value)
        elif percorredor:
            noAnterior.next = no
            no.next = percorredor
            return "\033[32mAdicionado com sucesso!\033[m"
        else:
             return self.add(value)


    def get_document(self, doc) -> Aluno:
        #retornar o aluno com a matricula igual ao doc, ou null se nao existir
        percorredor = self.init
        while percorredor is not None:
            if percorredor.value.matricula == doc:
                return percorredor.value
            percorredor = percorredor.next
        return None
    

    def get_index(self, index) -> Aluno:
        #retornar o aluno no index passado
        percorredor = self.init
        contador = 0
        while percorredor:
            if contador < index:
                percorredor = percorredor.next
                contador += 1
            else:
                return percorredor.value
        return None
    

    def remover_doc(self, doc) -> Aluno:
        #remover o aluno com a matricula igual ao doc, ou null se nao existir
        #depois de remover, retornar o aluno
        percorredor = self.init
        noAnterior = None
        while percorredor:
            if percorredor.value.matricula == doc:
                if noAnterior:
                    noAnterior.next = percorredor.next
                    if percorredor == self.end:
                        self.end = noAnterior
                else:
                    self.init = percorredor.next
                    if self.init is None:
                        self.end = None
                return percorredor.value
            noAnterior = percorredor
            percorredor = percorredor.next
        return None

    def get_alunos(self, name)-> list:
        #vai retornar a lista de Alunos que contem o nome
        alunos_pesquisados = List()
        percorredor = self.init
        while percorredor is not None:
            if name.lower() in percorredor.value.nome.lower():
                alunos_pesquisados.add(percorredor.value)
            percorredor = percorredor.next
        return alunos_pesquisados

    def get_total(self):
        #retornar total de alunos
        percorredor = self.init
        contador = 0
        while percorredor:
            percorredor = percorredor.next
            contador += 1
        return contador

    def get_alunos_por_status(self, status):
        #retornar uma lista de alunos com status igual ao parametro
        lista_alunos_status = List()
        percorredor = self.init
        while percorredor is not None:
            if percorredor.value.status == status:
                lista_alunos_status.add(percorredor.value)
            percorredor = percorredor.next
        return lista_alunos_status


    def ordenar_por_nome(self):
        #vai reoordenar a lista por nome
        trocou = True
        while trocou:
            percorredor = self.init
            noAnterior = None
            trocou = False
            while percorredor and percorredor.next is not None:
                novo_no = percorredor.next
                if percorredor.value.nome.lower() > novo_no.value.nome.lower():
                    trocou = True
                    if noAnterior is None:
                        self.init = novo_no
                    else:
                        noAnterior.next = novo_no
                    percorredor.next = novo_no.next
                    novo_no.next = percorredor
                    noAnterior = novo_no
                else:
                    noAnterior = percorredor
                    percorredor = percorredor.next
        percorredor = self.init
        while percorredor.next is not None:
            percorredor = percorredor.next
        self.last = percorredor


    def print(self):
        #retornar a lista com os nomes dos alunos separando por ,
        # [heldon,joão, pedro]
        retorno = '['
        percorredor = self.init
        primeiro = True
        while percorredor:
            if not primeiro:
                retorno += ', '
            retorno += percorredor.value.nome
            primeiro = False
            percorredor = percorredor.next
        retorno += ']'
        return retorno

    

aluno = Aluno('João', 123, True)
aluno2 = Aluno('Camila', 321, False)
aluno3 = Aluno('Dowglas', 456, True)
aluno4 = Aluno('Jonas', 765, False)
aluno5 = Aluno('Raí', 987, True)

lista = List()

#Testando add
print(f'Adicionando {aluno.nome}:\t{lista.add(aluno)}')
print(f'Adicionando {aluno2.nome}:\t{lista.add(aluno2)}')
print(f'Adicionando {aluno3.nome}:\t{lista.add(aluno3)}')
print(f'Adicionando {aluno4.nome}:\t{lista.add(aluno4)}')
print(f'Adicionando {aluno5.nome}:\t{lista.add(aluno5)}')
print(f'Adicionando {aluno.nome}:\t{lista.add(aluno)}') #repetição
print(f'Adicionando outro valor:\t{lista.add('abcdefg')}') #valor inválido

print(lista.print())

#Testando insert
aluno_novo = Aluno('Raiam Santos', 9043, False)
print(f'Adicionando {aluno_novo.nome} no índice 2:\t{lista.insert(2, aluno_novo)}')
print(f'Lista atual: {lista.print()}')

#Testando get_document
print(f'Procurando pela matrícula "{aluno.matricula}":\n{lista.get_document(aluno.matricula)}')
print(f'Procurando pela matrícula "{aluno2.matricula}":\n{lista.get_document(aluno2.matricula)}')
print(f'Procurando pela matrícula "inexistente":\n{lista.get_document('inexistente')}') #valor inválido

#Testando get_index
print(f'Aluno no índice 1:\n{lista.get_index(1)}')
print(f'Aluno no índice 1000:\n{lista.get_index(1000)}') #índice enorme

#Testando remover_doc
print(f'Removendo {aluno4.nome}:\n{lista.remover_doc(aluno4.matricula)}')
print(f'Removendo aluno inexistente:\n{lista.remover_doc(12024008)}') #aluno inexistente

#Testando get_alunos
alunos_com_e = lista.get_alunos('e')
print(f'Lista de alunos com "e":\t{alunos_com_e.print()}') #alunos sem essa letra
alunos_com_a = lista.get_alunos('A')
print(f'Lista de alunos com "a":\t{alunos_com_a.print()}')

#Testando get_total
print(f'Total da lista de alunos:\t{lista.get_total()}')

#Testando print
print(f'Lista atual:\t{lista.print()}')

#Testando get_alunos_por_status
status_false = lista.get_alunos_por_status(False)
print(status_false.print())
status_true = lista.get_alunos_por_status(True)
print(status_true.print())

#Testando ordenar_por_nome
lista.ordenar_por_nome()
print(lista.print())
