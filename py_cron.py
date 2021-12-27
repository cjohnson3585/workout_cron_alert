from crontab import CronTab

#change to your username for the crontab file
cron = CronTab(user='user')
 
#First job, change python path and script path or enter any command you want. 
job1 = cron.new(command='/usr/bin/python3 /path/to/send_text.py', comment='First text')

#standard cron syntax for timing
job1.setall('0 10 * * *')

#Add As many Jobs as you want
job2 = cron.new(command='/usr/bin/python3 /path/to/send_text.py', comment='Second text')

job2.setall('0 18 * * *')

#Uncomment below to remov all jobs that contain comment='First text'
#cron.remove_all(comment='First text')

#print out current jobs
for item in cron:
    print(item)

#write to crob object
cron.write()
