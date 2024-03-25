import requests
import dotenv
import os 
from rich.console import Console
from rich.markdown import Markdown

console = Console()
dotenv.load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def list_tasks(task_id_list: list):
    """
    Retrieves and prints information about tasks from the Notion database.

    Args:
        task_id_list (list): A list to store the task IDs.

    Returns:
        None
    """
    url = f"https://api.notion.com/v1/......" ## Add the URL to fetch tasks from the Notion API
    response = requests.post(url, headers=HEADERS)
    tasks = response.json().get("results", [])
    keep_ids = False
    if not task_id_list:
        keep_ids = True
    for task in tasks:
        task_id = None    ## Add code to get the task ID
        task_name = None  ## Add code to get the task name
        task_status = None ## Add code to get the task status
        print(f"ID: {task_id} | Name: {task_name} | Status: {task_status}")
        if keep_ids:
            task_id_list.append(task_id)

def get_task_content(page_id: str):
    """
    Retrieves the content of a task page from Notion API.

    Args:
        page_id (str): The ID of the task page.

    Returns:
        None

    Raises:
        None

    """
    url = f"https://api.notion.com/v1/....."
    response = requests.get(url, headers=HEADERS)
    blocks = response.json().get("results", [])
    
    content = ""
    for block in blocks:
        if block['type'] == 'paragraph':
            text_content = None ## Add code to get the text content of the paragraph block
            content += text_content + "\n\n"
        elif block['type'] in ['heading_1', 'heading_2', 'heading_3']:
            text_content = None ## Add code to get the text content of the heading block
            if block['type'] == 'heading_1':
                content += None ## Add code to format the heading as a level 1 heading
            elif block['type'] == 'heading_2':
                content += None ## Add code to format the heading as a level 2 heading
            elif block['type'] == 'heading_3':
                content += None ## Add code to format the heading as a level 3 heading
        elif block['type'] == 'bulleted_list_item':
            text_content = None ## Add code to get the text content of the bulleted list item block
            content += None ## Add code to format the bulleted list item
        # Add here handling for other block types like links, etc.

    md = Markdown(content)
    console.print(md)

def get_task_details(task_id):
    """
    Retrieves and prints the details of a task from the Notion API.

    Args:
        task_id (str): The ID of the task to retrieve details for.

    Returns:
        None
    """
    url = f"https://api.notion.com/v1/....." # Add the URL to fetch task details from the Notion API
    response = requests.get(url, headers=HEADERS)
    task = response.json()
    
    task_name = None ## Add code to get the task name
    task_status = None ## Add code to get the task status
    task_creation_date = None ## Add code to get the task creation date
    
    print(f"Name: {task_name}\nStatus: {task_status}\nCreation Date: {task_creation_date}")
    get_task_content(task_id)


def update_task_status(task_id: str, new_status: str):
    """
    Update the status of a task in Notion.

    Args:
        task_id (str): The ID of the task to update.
        new_status (str): The new status to set for the task.

    Returns:
        None

    Raises:
        None
    """
    url = f"https://api.notion.com/v1/....." ## Add the URL to update the task status
    
    data = {
    } ## Add the data to update the task status
    
    response = requests.patch(url, json=data, headers=HEADERS)
    if response.status_code == 200:
        print("Task status updated successfully.")
    else:
        print("Failed to update task status.")

def add_text_to_task_body(page_id: str, text: str):
    """
    Adds text to the body of a task in Notion.

    Args:
        page_id (str): The ID of the page containing the task.
        text (str): The text to be added to the task body.

    Returns:
        None

    Raises:
        None
    """
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    
    data = {
        ## Add the data to add text to the task body    
    }
    
    response = requests.patch(url, json=data, headers=HEADERS)
    if response.status_code == 200:
        print("Text added successfully to the page.")
    else:
        print(f"Failed to add text to the page. Error: {response.json()}")
        print(response.json())
