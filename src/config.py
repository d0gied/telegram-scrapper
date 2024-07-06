from os import getenv

if getenv("ENV_FILE"):
    from dotenv import load_dotenv
    load_dotenv(getenv("ENV_FILE"))

def envlist(key: str) -> list[str]:
    return getenv(key, ",").split()

def envint(key: str) -> int:
    return int(getenv(key, "0"))

def envstr(key: str) -> str:
    return getenv(key, "")

class Config:
    class Pyrogram:
        API_ID: int = envint("PYRO_API_ID")
        API_HASH: str = envstr("PYRO_API_HASH")

    ADMINS = envlist("ADMINS")
    FOLDER_NAME = envstr("FOLDER_NAME")
