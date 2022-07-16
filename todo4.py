print('Olá. Seja bem vindo a plataforma de recrutamento e seleção!')

nome = str(input('Digite seu nome: '))
cand_zero = 0
num_de_cand = int(input('Digite a quantidade de candidatos a participar do processo seletivo: '))
localizacao_cand = 1

lista_geral = []

lista_vagas1 = ['1']
lista_vagas2 = ['2']


requis_analista = ['python', 'powerbi', 'sql', 'boa comunicação']
requis_cientista = ['python', 'banco de dados', 'machine learning', 'resolução de problemas', 'estatística']

while cand_zero < num_de_cand:
  lista_infor_cand = []
  
  nome_do_candidato = str(input(f'Olá {nome}. Digite o nome do candidato {localizacao_cand} : '))
  resumo_candidato = str(input(f'Escreva o resumo do curriculo do {nome_do_candidato} : '))
  print('Essas são as vagas disponiveis: ')
  print('1 - Analista de dados') 
  print('2 - Cientista de dados')
  vaga_concorrendo = str(input(f'Digite o número da vaga pleiteada pelo {nome_do_candidato}: ')) 

  lista_infor_cand.append(vaga_concorrendo)  
  lista_infor_cand.append(nome_do_candidato)
  lista_infor_cand.append(resumo_candidato)
  
  lista_geral.append(lista_infor_cand)
  
  cand_zero += 1
  localizacao_cand += 1    



candidatos_cargo1 = []
candidatos_cargo2 = []
for candidatos, itens in enumerate(lista_geral):
    for dados, valor in enumerate (itens):
        if lista_vagas1[0]==valor:
            candidatos_cargo1.append(lista_geral[candidatos])
            # print(candidatos_cargo1)
        if lista_vagas2[0]==valor:
            candidatos_cargo2.append(lista_geral[candidatos])
            # print(candidatos_cargo2)

def selecao_vaga1(requis_analista, candidatos_cargo1):
    lista_cand_1_aprovado = []
    for candidatos, itens in enumerate(candidatos_cargo1):
        for dados, valor in enumerate(itens):
            if requis_analista[dados]==valor:
                lista_cand_1_aprovado.append(candidatos_cargo1[candidatos])
                print(f'{len(lista_cand_1_aprovado)} foram aprovados para a vaga de Analista de dados onde {len(candidatos_cargo1)} estavam inscritas')    
 
selecao_vaga1(requis_analista, candidatos_cargo1)

def selecao_vaga2(requis_cientista, candidatos_cargo2):
    lista_cand_2_aprovado = []
    for candidatos, itens in enumerate(candidatos_cargo2):
        for dados, valor in enumerate(itens):
            if requis_cientista[dados]==valor:
                lista_cand_2_aprovado.append(candidatos_cargo2[candidatos])
                print(f'{len(lista_cand_2_aprovado)} foram aprovados para a vaga de Cientista de dados onde {len(candidatos_cargo2)} estavam inscritas' )
selecao_vaga2(requis_cientista, candidatos_cargo2)




