from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
Admin = env.int("Admin")
