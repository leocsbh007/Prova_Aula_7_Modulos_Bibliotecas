'''
[PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. 
O programa deve permitir:
1 - Adicionar
2 - Remover
3 - Atualizar
4 - Listar os alunos.
Para isso, você deve implementar um módulo que contém as seguintes funções:
AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
Lembre Se de Modularizar o código
'''

def AdicionarAluno(nome:str, matricula:int):
    # Verifica se este aluno já esta cadastrado
    if matricula in alunos.keys():        
        print("Já existe matricula cadastrada")        
    else:
        aluno["Nome"] = nome
        alunos[matricula] = aluno.copy()


def RemoverAluno(matricula:int):    
    # Verifica se existe aluno cadastrado
    if matricula in alunos.keys():        
        alunos.pop(matricula)
    else:
        print("Não existe matricula cadastrada")
    

def AtualizarAluno(matricula:int, nome:str):
    # Verifica se existe aluno cadastrado
    if matricula in alunos.keys():        
        alunos[matricula]["Nome"] = nome
    else:
        print("Não existe matricula cadastrada")

def VerAlunos(alunos:dict):
    # Verifica se existe aluno cadastrado
    if len(alunos) == 0:
        print("Não existe nenhum aluno cadastrado")  
    else:
        print('Matricula || Nome')
        for matricula, aluno in alunos.items():
            print(f'{matricula}         || {aluno["Nome"]}')

# Variaveis do Sistema
alunos = {}
aluno = {}
controle = True

# Loop Principal
while controle:
    print("""
            ADICIONAR ALUNO     ( 1 )
            VISUALIZAR ALUNO    ( 2 )        
            ATUALIZAR ALUNO     ( 3 )      
            EXCLUIR ALUNO       ( 4 )          
            SAIR                ( 0 )                                    
          """)
    opcao = input("Digite a Opção: ")

    match opcao:        
        case '1':
            print("Inserindo Aluno")
            try:
                nome = str(input("Nome do Aluno: ")).strip()
                matricula = int(input("Matricula do Aluno: "))      
            except ValueError:
                print("Erro: Matricula deve ser um número inteiro válido.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
            else:
                AdicionarAluno(nome, matricula)
            
        case '2':
            print("Listando Alunos")
            VerAlunos(alunos)
        case '3':
            print("Atualizando Aluno")
            try:
                matricula = int(input("Matricula do Aluno para atualizar: "))
                nome = str(input("Nome do Aluno : ")).strip()
            except ValueError:
                print("Erro: Matricula deve ser um número inteiro válido.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
            else: 
                AtualizarAluno(matricula, nome)
        case '4':
            print("Removendo Aluno")
            try:
                matricula = int(input("Digite a Matricula do Aluno: "))
            except ValueError:
                print("Erro: Matricula deve ser um número inteiro válido.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
            else: 
                RemoverAluno(matricula)
        case '0':
          controle = False
        case _:
            print('OPÇÃO INVALIDA')
else:
    print("Saindo do Sistema")
