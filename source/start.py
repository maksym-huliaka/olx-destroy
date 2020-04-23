from modules.publication_filter import get_current_time
from modules.scheduler import start_scheduler
from modules.telegram.bot import BOT

print(get_current_time()+" [OK] Program started")
start_scheduler()
BOT.polling()
