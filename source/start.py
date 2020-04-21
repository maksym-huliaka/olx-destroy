from modules.connection.connection_factory import getDriver
from modules.database.repository.repository import delete, get, save
from modules.scheduler import start_scheduler
from modules.telegram.bot import BOT
from modules.util.words_migrate import migrate_to_db

print("[OK] Program started")
start_scheduler()
BOT.polling()

