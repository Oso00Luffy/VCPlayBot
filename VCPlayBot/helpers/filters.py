from typing import List, Union
from pyrogram import filters
from VCPlayBot.config import COMMAND_PREFIXES

# تعديل الفلتر بحيث يستخدم filters.update.edited بدلاً من filters.edited
other_filters = filters.group & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.update.edited & ~filters.via_bot & ~filters.forwarded
)

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
