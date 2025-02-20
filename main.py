import sys

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from notion_helpers import (
    list_tasks,
    get_task_details,
    update_task_status,
    add_text_to_task_body,
)


def main():
    """
    Main function that handles the user interaction with the program.

    The function prompts the user for an action and performs the corresponding
    operation based on user input.
    The available actions are:
    - list: Lists all the tasks.
    - details: Displays the details of a specific task.
    - update: Updates the status of a specific task.
    - add_text: Adds text to the body of a specific task.
    - exit: Exits the program.

    The function uses the `WordCompleter` class to provide autocompletion for the user input.

    Returns:
        None
    """

    task_completer = WordCompleter(["list", "details", "update", "add_text", "exit"])
    status_completer = WordCompleter(["Not Started", "In Progress", "Completed"])
    task_id_completer = None
    task_id_list = []

    # first process verbs on the command line if any
    # so you can call e.g.
    # python main.py list
    # and it will first list the tasks and then prompt for more input
    # and you can also call just
    # python main.py
    # and it will prompt for input
    while True:
        if sys.argv[1:]:
            user_input = sys.argv[1]
            sys.argv[1:2] = []
        else:
            user_input = prompt("Action: ", completer=task_completer)
        if user_input == "list":
            list_tasks(task_id_list)
            task_id_completer = WordCompleter(task_id_list)
        elif user_input == "details":
            task_id = prompt("Enter task ID: ", completer=task_id_completer)
            get_task_details(task_id)
        elif user_input == "update":
            task_id = prompt("Enter task ID: ", completer=task_id_completer)
            new_value = prompt("Enter new value: ", completer=status_completer)
            update_task_status(task_id, new_value)
        elif user_input == "add_text":
            page_id = prompt("Enter page ID: ", completer=task_id_completer)
            text = prompt("Enter text to add: ")
            add_text_to_task_body(page_id, text)
            break
        elif user_input == "exit":
            break


if __name__ == "__main__":
    main()
