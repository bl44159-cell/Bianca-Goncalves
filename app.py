import os

TAREFAS_FILE = "tarefas.txt"

def limpar_tela():
    """Limpa o terminal para manter a interface organizada"""
    # 'cls' funciona no Windows, 'clear' no Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_tarefas():
    """Carrega as tarefas salvas no arquivo tarefas.txt"""
    tarefas = []
    if os.path.exists(TAREFAS_FILE):
        with open(TAREFAS_FILE, "r", encoding="utf-8") as file:
            for linha in file:
                partes = linha.strip().split(" | ")
                if len(partes) == 2:
                    tarefas.append({"titulo": partes[0], "concluida": partes[1] == "Sim"})
    return tarefas

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo de texto"""
    with open(TAREFAS_FILE, "w", encoding="utf-8") as file:
        for t in tarefas:
            status = "Sim" if t["concluida"] else "Nao"
            file.write(f"{t['titulo']} | {status}\n")

def listar_tarefas(tarefas):
    """Exibe todas as tarefas formatadas"""
    if not tarefas:
        print("\n📌 Nenhuma tarefa cadastrada.")
        return

    print("\n--- 📋 LISTA DE TAREFAS ---")
    for i, t in enumerate(tarefas, 1):
        status = "✅ [Concluída]" if t["concluida"] else "⏳ [Pendente]"
        print(f"{i}. {t['titulo']} {status}")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa"""
    titulo = input("\n✍️ Digite a descrição da nova tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        salvar_tarefas(tarefas)
        print("\n🎉 Tarefa adicionada com sucesso!")
    else:
        print("\n⚠️ A descrição não pode ser vazia.")
    input("\nPressione ENTER para voltar ao menu...")

def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída"""
    listar_tarefas(tarefas)
    if not tarefas:
        input("\nPressione ENTER para voltar ao menu...")
        return
    
    try:
        num = int(input("\n👉 Digite o número da tarefa a concluir: "))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("\n✅ Tarefa marcada como concluída!")
        else:
            print("\n⚠️ Número inválido.")
    except ValueError:
        print("\n⚠️ Por favor, digite apenas números.")
    input("\nPressione ENTER para voltar ao menu...")

def remover_tarefa(tarefas):
    """Remove uma tarefa da lista"""
    listar_tarefas(tarefas)
    if not tarefas:
        input("\nPressione ENTER para voltar ao menu...")
        return
    
    try:
        num = int(input("\n🗑️ Digite o número da tarefa a remover: "))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            salvar_tarefas(tarefas)
            print(f"\n🗑️ Tarefa '{removida['titulo']}' removida com sucesso!")
        else:
            print("\n⚠️ Número inválido.")
    except ValueError:
        print("\n⚠️ Por favor, digite apenas números.")
    input("\nPressione ENTER para voltar ao menu...")

def main():
    """Função principal com o menu de opções"""
    tarefas = carregar_tarefas()

    while True:
        limpar_tela()  # <--- LIMPA A TELA A CADA REPETIÇÃO DO MENU
        
        print("==============================")
        print("   SISTEMA DE GERENCIAMENTO   ")
        print("==============================")
        print("1. Listar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ").strip()

        if opcao == "1":
            limpar_tela()
            listar_tarefas(tarefas)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "2":
            limpar_tela()
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            limpar_tela()
            concluir_tarefa(tarefas)
        elif opcao == "4":
            limpar_tela()
            remover_tarefa(tarefas)
        elif opcao == "5":
            limpar_tela()
            print("Até logo! 👋\n")
            break
        else:
            print("\n⚠️ Opção inválida!")
            input("Pressione ENTER para tentar novamente...")

if __name__ == "__main__":
    main() 

