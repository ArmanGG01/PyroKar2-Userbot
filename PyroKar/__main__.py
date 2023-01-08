import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from PyroKar import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, clients
from PyroKar.helper.misc import create_botlog, heroku
from PyroKar.modules import ALL_MODULES

MSG_ON = """
💢 **PyroKar-Userbot Udah Aktif** 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("PyroKar.modules" + all_module)
        print(f"Successfully Imported {all_module} ✔")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            try:
                await cli.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            print(f"Started {ex.first_name} ✔")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("PyroKar").info(f"PyroKar-UserBot v{BOT_VER} [👑 BERHASIL DIAKTIFKAN YA KONTOL! 👑]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(app)
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
