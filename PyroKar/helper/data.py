from pyrogram.types import InlineKeyboardButton

class Data:

    text_help_menu = (
        "**Command List & Help**\n**— Prefixes:** `.`"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    help_pic = or "https://telegra.ph//file/5f3929a7c65ed2dfd93db.jpg"
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
