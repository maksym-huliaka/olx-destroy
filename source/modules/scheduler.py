from apscheduler.schedulers.background import BlockingScheduler

from modules.telegram.bot import BOT
from modules.telegram.bot_helper import send_publications

CHAT_ID_PATH='resources/chatid.ini'
scheduler = BackgroundScheduler()

def job_function ():
    chat_id=open(CHAT_ID_PATH).read()
    send_publications(chat_id, BOT)
    print ('schedule job')

def start_scheduler():
    scheduler.add_job(job_function, trigger='cron', minute='*/15')
    scheduler.start()
