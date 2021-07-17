from datetime import datetime

def cronjob():
    """
    Main cron job that will be run continuously ...
    """

    print("Cron job is running.");
    print("Tick! The time is: %s" %datetime.now());
