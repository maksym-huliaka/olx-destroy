from apscheduler.schedulers.background import BackgroundScheduler

from modules.publication_filter import get_current_time
from modules.states import bussy, get_bussy, set_bussy
from modules.telegram.bot import BOT
from modules.telegram.bot_helper import send_publications
from modules.util.config import config

scheduler = BackgroundScheduler()

def job_function ():
    print (get_current_time()+' [JOB] Schedule job started')
    chat_id=config().get("telegram.chat_id")
    if not get_bussy():
        set_bussy(True)
        send_publications(chat_id, BOT)
        set_bussy(False)


def start_scheduler():
    scheduler.add_job(job_function, trigger='cron', minute='*/30')
    scheduler.start()
