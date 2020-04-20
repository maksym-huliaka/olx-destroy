from apscheduler.schedulers.background import BackgroundScheduler

from modules.telegram.bot import BOT
from modules.telegram.bot_helper import send_publications
from modules.util.config import config

scheduler = BackgroundScheduler()

def job_function ():
    print ('schedule job started')
    chat_id=open(config(section='telegram').get("telegram.chatId"))
    send_publications(chat_id, BOT)

def start_scheduler():
    scheduler.add_job(job_function, trigger='cron', minute='*/30')
    scheduler.start()
