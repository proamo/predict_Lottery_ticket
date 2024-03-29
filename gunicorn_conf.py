import multiprocessing
bind = '0.0.0.0:8000'
backlog = 512
timeout = 30
worker_class = 'gevent'

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

# accesslog = "/home/predict_Lottery_ticket/log/access.log"
# errorlog = "/home/predict_Lottery_ticket/log/error.log"
