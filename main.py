import requests
import os
import pyfiglet
import json
tarefas = []
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_reset = "\033[0m"
arquivo = "tarefas.json"
if os.path.exists(arquivo):
  with open(arquivo,"r") as dados:
    tarefas = json.load(dados)
else:
  with open(arquivo,"w") as dados:
    json.dump(tarefas,dados)
def text():
  os.system('clear')
  texto = pyfiglet.figlet_format('Lista de Tarefas')
  print(cor_vermelha + texto + cor_reset )
def menu():
  text()
  print('[1] Lista de Tarefas')
  print('[2] Sair\n\n')
  while True:
    ac = input("Digite um Numero: ")
    if ac.isdigit():
      if int(ac) == 1:
        listT()
        break
      elif int(ac) == 2:
        os.system("clear")
        print("exit")
        break
    else:
      menu()
      break
def listT():
  text()
  with open(arquivo,"r") as dados:
    tarefas = json.load(dados)
  print("[exit] Voltar")
  print("[add] Adicionar Tarefa\n")
  count = 0
  for data in tarefas:
    print(f"[{count}] {data['nome']} ")
    count += 1
  if len(tarefas) == 0:
    print("nenhuma tarefa encontrada")
  print("\n\n")
  while True:
    act = input("Digite um ação: ")
    if act == "exit":
      menu()
      break
    elif act == "add":
      addTarefa()
      break
    elif act.isdigit() & tarefaExits(int(act)):
      viewTarefa(int(act))
      break
def addTarefa():
  text()
  print("Adicionar Tarefa: ")
  print("Digite $ EXIT Para voltar")
  nome = ''
  desc = ''
  while True:
    if len(nome) == 0:
      nome = input("Nome da Tarefa: ")
    if nome == "$ EXIT" or desc == "$ EXIT":
      listT()
      break
    if len(desc) == 0:
      desc = input("Descrição da tarefa: ")
    if nome == "$ EXIT" or desc == "$ EXIT":
      listT()
      break
    if len(nome) > 0 and len(desc) > 0:
      list_temp = {
          "id": len(tarefas),
          "nome": nome,
          "descricao": desc
        }
      tarefas.append(list_temp)
      input("Tarefa Adicionada Com sucesso. aperte enter para continuar")
      with open(arquivo,"w") as dados:
        json.dump(tarefas,dados)
      listT()
      break
    else:
      print(f"error {nome} {len(nome)} {desc} {len(desc)}")
      break
def tarefaExits(id):
  if len(tarefas) > id and tarefas[id] != "":
    return True
  else:
    return False
def viewTarefa(id):
  text()
  print("[exit] voltar")
  print("[excluir] Excluir tarefa\n\n")
  print("Nome: " + tarefas[id]['nome'] + "\n")
  print("Descrição: " + tarefas[id]['descricao'] + "\n\n")
  while True:
    ac = input("Digite uma ação: ")
    if ac == "exit":
      listT()
    elif ac == "excluir":
      tarefas.pop(id)
      with open(arquivo,"w") as dados:
        json.dump(tarefas,dados)
      input("tarefa excluída com sucesso. aperte enter para continuar: ")
      listT()
      break
if __name__ == "__main__":
  menu()
