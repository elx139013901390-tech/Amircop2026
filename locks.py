LOCKS = {
    "gif": True,
    "photo": True,
    "video": True,
    "sticker": True,
    "document": True,
    "voice": True,
}

def lock(name):
    if name in LOCKS:
        LOCKS[name] = True
        return True
    return False

def unlock(name):
    if name in LOCKS:
        LOCKS[name] = False
        return True
    return False
