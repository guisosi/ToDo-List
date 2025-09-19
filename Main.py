import os
import json

FILE = 'tarefas.json'

def clear_system():
    os.system('cls' if os.name == 'nt' else 'clear')

def  load_tasks():
    if not os.path.exists(FILE):
        return[]
    with open(FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def list_tasks(tasks):
    if not tasks:
        print('Nenhuma tarefa encontrada.')
        return
    print("\nTarefas:")