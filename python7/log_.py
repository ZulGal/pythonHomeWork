from datetime import datetime as d
from time import time

def contact_logger(done_):
    
    time = d.now().strftime('%Y-%m-%d %H:%M')
    path = r'log.csv'
    with open (path,'a') as f:
        f.write(f'{time},{done_}')
