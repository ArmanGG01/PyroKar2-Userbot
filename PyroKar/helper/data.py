from pyrogram.types import InlineKeyboardButton
from config import HELP_PIC

class Data:

    text_help_menu = (
        "**Command List & Help**\n**— Prefixes:** `.`"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    help_logo = HELP_PIC or "https://telegra.ph//file/5f3929a7c65ed2dfd93db.jpg"
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
