from telethon.tl.types import User, Chat, Channel

async def load_dialogs(client):
    users = []
    groups = []
    channels = []
    bots = []

    async for dialog in client.iter_dialogs():
        entity = dialog.entity

        if isinstance(entity, User):
            if entity.bot:
                bots.append(dialog)
            else:
                users.append(dialog)

        elif isinstance(entity, Chat):
            groups.append(dialog)

        elif isinstance(entity, Channel):
            if entity.broadcast:
                channels.append(dialog)
            else:
                groups.append(dialog)

    return {
        "Users": users,
        "Groups": groups,
        "Channels": channels,
        "Bots": bots
    }
