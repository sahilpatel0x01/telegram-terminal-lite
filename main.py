import asyncio
import os
from auth import get_client
from chat_loader import load_dialogs
from ui import select_folder, select_chat, show_messages
from rich.console import Console

console = Console()

async def run():
    try:
        client = get_client()
    except ValueError as e:
        console.print(f"[bold red]Error[/bold red]: {e}")
        return

    await client.start()
    console.print("[bold green]Successfully logged in![/bold green]")

    while True:
        with console.status("[bold blue]Loading dialogs...[/bold blue]"):
            dialogs = await load_dialogs(client)
        
        folder = await select_folder()

        if folder == "Exit" or folder is None:
            break

        chats = dialogs.get(folder, [])
        if not chats:
            console.print(f"[yellow]No {folder} found.[/yellow]")
            continue

        while True:
            selected = await select_chat(chats)

            if selected == "Back" or selected is None:
                break

            # Find the dialog matching the selected name
            # Handle possible duplicate names by taking the first match
            dialog = next((d for d in chats if (d.name if d.name else str(d.id)) == selected), None)
            
            if dialog:
                await show_messages(client, dialog)

    await client.disconnect()

if __name__ == "__main__":
    # Ensure console clears gracefully
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\nExiting...")
