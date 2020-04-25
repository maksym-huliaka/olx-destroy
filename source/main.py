from modules.publication_filter import get_current_time
from modules.telegram.bot import BOT, start_scheduler
from modules.util.config import config

print(get_current_time() + " [OK] Program started")
BOT.send_message(config().get("telegram.chat_id"), "👻 I'm alive!")
start_scheduler()
BOT.polling()
