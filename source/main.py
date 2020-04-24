from modules.publication_filter import get_current_time
from modules.scheduler import start_scheduler
from modules.telegram.bot import BOT
from modules.util.config import config

start_scheduler()
print(get_current_time() + " [OK] Program started")
BOT.send_message(config().get("telegram.chat_id"), "👻 I'm alive!")
BOT.polling()
