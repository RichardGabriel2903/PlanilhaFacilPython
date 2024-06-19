from task_manager import TaskManager


def main():
    manager = TaskManager()
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            description = input("Descrição da tarefa: ")
            due_date = input("Data de vencimento (YYYY-MM-DD): ")
            manager.add_task(description, due_date)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            task_index = int(input("Índice da tarefa para marcar como concluída: "))
            manager.mark_task_as_completed(task_index)
        elif choice == '4':
            task_index = int(input("Índice da tarefa para remover: "))
            manager.remove_task(task_index)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
