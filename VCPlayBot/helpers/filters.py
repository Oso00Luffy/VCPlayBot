from typing import List, Union
from pyrogram import filters
from VCPlayBot.config import COMMAND_PREFIXES

# إزالة filters.update.edited لأنه غير موجود في pyrogram
other_filters = filters.group & ~filters.via_bot & ~filters.forwarded
other_filters2 = filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
