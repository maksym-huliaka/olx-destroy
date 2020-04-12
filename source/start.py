from modules.scheduler import start_scheduler
from modules.telegram.bot import BOT

print("Program started")
start_scheduler()
BOT.polling()

