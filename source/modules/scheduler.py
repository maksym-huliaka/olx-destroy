from apscheduler.schedulers.background import BackgroundScheduler

from modules.path import CHAT_ID_PATH
from modules.telegram.bot import BOT
from modules.telegram.bot_helper import send_publications

scheduler = BackgroundScheduler()

def job_function ():
    print ('schedule job started')
    chat_id=open(CHAT_ID_PATH).read()
    send_publications(chat_id, BOT)

def start_scheduler():
    scheduler.add_job(job_function, trigger='cron', minute='*/15')
    scheduler.start()
