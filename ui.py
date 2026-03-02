import questionary
from rich.console import Console
from rich.table import Table

console = Console()

async def select_folder():
    return await questionary.select(
        "Select Folder",
        choices=["Users", "Groups", "Channels", "Bots", "Exit"]
    ).ask_async()

async def select_chat(dialogs):
    # dialogs can have duplicate names or empty names, so handle that nicely
    choices = []
    for d in dialogs:
        name = d.name if d.name else str(d.id)
        choices.append(name)
    
    return await questionary.select(
        "Select Chat",
        choices=choices + ["Back"]
    ).ask_async()

async def show_messages(client, dialog):
    table = Table(title=f"Messages - {dialog.name}")
    table.add_column("Sender")
    table.add_column("Message")

    # Get recent messages
    messages = []
    async for msg in client.iter_messages(dialog.entity, limit=20):
        messages.append(msg)
    
    # Reverse to show chronological order (oldest at top, newest at bottom of the 20)
    for msg in reversed(messages):
        sender = msg.sender_id
        text = msg.text or ""
        table.add_row(str(sender), text)

    console.print(table)
    input("Press Enter to go back...")
