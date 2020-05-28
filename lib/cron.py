from crontab import CronTab
from datetime import datetime

def schedule():
    cron = CronTab(user='root')
    for job in cron:
        sched = job.schedule(date_from=datetime.now())
        return sched.get_next()

def create_cronjob():
    cron = CronTab(user='root')

    for line in cron.lines:
        if int(str(len(line))) <= 0:
            continue
        else:
            if 'bitg-autodrop' in str(line).strip():
                print ("CronJob already exists!")
            else:
                job = cron.new(command='/usr/bin/python3 ~/airdrop-prod/autodrop.py', comment='bitg-autodrop')
                job.hour.every(6)
                job.minute.on(0)
                job.enable(False)
                cron.write()
                print ("Cron job created!")

def enable_batch_airdrop():
    cron = CronTab(user='root')
    for job in cron:
        if job.comment == 'bitg-autodrop':
            job.enable(True)
            cron.write()
            print ("Enabled!")
        else:
            print("Job doesn't exist")

def disable_batch_airdrop():
    cron = CronTab(user='root')
    for job in cron:
        if job.comment == 'bitg-autodrop':
            job.enable(False)
            cron.write()
            print ("Disabled!")
        else:
            print("Job doesn't exist")