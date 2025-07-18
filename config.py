from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("7683635500:AAFM56o7fZn-YDTywWH52B4xRMvjR173iMg")
ADMINS = env.list("8048404748")
WORK_DIRECTORY = env.str("WORK_DIRECTORY")
API_ID = env.int("26860554")
API_HASH = env.str("008aad4cabad032392bb5d83f93acb04")
IP = env.str("ip")
