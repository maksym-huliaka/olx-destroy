from apscheduler.schedulers.background import BackgroundScheduler

from modules.telegram.bot import BOT
from modules.telegram.bot_helper import send_publications
from modules.util.config import config

scheduler = BackgroundScheduler()

def job_function ():
    print ('[JOB] Schedule job started')
    chat_id=config().get("telegram.chat_id")
    send_publications(chat_id, BOT)

def start_scheduler():
    scheduler.add_job(job_function, trigger='cron', minute='*/30')
    scheduler.start()
