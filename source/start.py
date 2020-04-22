from modules.fingerprint.finger_test import test_fingers
from modules.fingerprint.proxy_test import check_driver_2ip
from modules.scheduler import start_scheduler
from modules.telegram.bot import BOT

test_fingers()
print("[OK] Program started")
start_scheduler()
BOT.polling()
