"""Emoji

Available Commands:

.think"""

from telethon import events

import asyncio





@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 2500)

    input_str = event.pattern_match.group(1)

    if input_str == "thinking":

        await event.edit(input_str)

        animation_chars = [
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\",
            "Thinking... (・_・ヾ  |",
            "Thinking... (・_・ヾ  /",
            "Thinking... (・_・ヾ  -",
            "Thinking... (・_・ヾ  \\"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 512])
