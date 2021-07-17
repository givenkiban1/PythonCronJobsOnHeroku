#package scheduler
from apscheduler.schedulers.blocking import BlockingScheduler

#main cronjob function
from main import cronjob

#create an instance of scheduler and add function
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, "interval", seconds=30)

scheduler.start()
