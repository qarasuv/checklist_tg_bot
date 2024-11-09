from os import getenv

from dotenv import load_dotenv

load_dotenv()


TOKEN = getenv("BOT_TOKEN")
MODERATOR = getenv("ID_MODERATOR")
USER_NAME_ADMIN = getenv("USER_NAME_ADMIN")
PROVIDER_TOKEN = getenv("PROVIDER_TOKEN")

TARIFFS = {
    10: (3, 30, 41),
    12: (6, 30, 42),
    14: (15, 30, 43),
    249: (100, 30, 44),
    149: (3, 90, 51),
    210: (6, 90, 52),
    450: (15, 90, 53),
    747: (100, 90, 54),
    600: (3, 365, 61),
    840: (6, 365, 62),
    1800: (15, 365, 63),
    2988: (100, 365, 64),
}
