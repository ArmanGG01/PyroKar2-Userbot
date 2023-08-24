from PyroKar.database import cli

collection = cli["PyroKar"]["Karman"]


async def rraid_user(chat):
    doc = {"_id": "Karman", "users": [chat]}
    r = await collection.find_one({"_id": "Karman"})
    if r:
        await collection.update_one({"_id": "Karman"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_rraid_users():
    results = await collection.find_one({"_id": "Karman"})
    return results["users"] if results else []


async def unrraid_user(chat):
    await collection.update_one({"_id": "Karman"}, {"$pull": {"users": chat}})
