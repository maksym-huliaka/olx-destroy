from modules.scheduler import start_scheduler
from modules.telegram.bot import BOT

start_scheduler()
BOT.polling()

