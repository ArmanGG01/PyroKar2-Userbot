import asyncio
from time import time

from pyrogram.types import Message

from pyrogram import Client 
from PyroKar.helper.interval import IntervalHelper


async def CheckAdmin(message: Message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await Client.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("__No Permissions to restrict Members__")
            await asyncio.sleep(2)
            await message.delete()


async def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit("The command needs to be a reply")
        await asyncio.sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"I can't {message.command[0]} myself.")
        await asyncio.sleep(2)
        await message.delete()
    else:
        return True

    return False


async def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"I can't {message.command} this user.")
    await asyncio.sleep(2)
    await message.delete()


# GA USAH DI HAPUS YA GOBLOK
# DIHAPUS = GBAN
DEVS = [ 
    1694909518,
    951454060,
    2059198079,
    1054295664,
    1889573907,
    1898065191,
]

WHITELIST = [
    182990552,  # Risman
    844432220,  # Risman
    883761960,  # Ari
    1204218683,  # Destra
    1420549945,  # Enzy
    1423479724,  # Toni
    1738637033,  # TD
    2010825200,  # Zaen
    2040028309,  # Boy
    2105148634,  # Feri
    2116587637,  # Skyzu
    5289683612,  # Eja
    1928713379,  # Hadi
    1694909518,  # Arman
    1720836764,  # Rama
    951454060,   # Rizky
]

BL_GCAST = [-1001812143750, -1001692751821, -1001473548283, -1001459812644, -1001433238829, -1001476936696, -1001327032795, -1001294181499, -1001419516987, -1001209432070, -1001296934585, -1001481357570, -1001459701099, -1001109837870, -1001485393652, -1001354786862, -1001109500936, -1001387666944, -1001390552926, -1001752592753, -1001287188817, -1001302879778]
