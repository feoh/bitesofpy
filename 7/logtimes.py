from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def parse_logline(line):
    (level, ts, *rest) = line.split()
    return level, ts, rest


def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    (level, ts, *rest) = parse_logline(line)
    return datetime.fromisoformat(ts)

    


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_lines = [ line for line in loglines if "Shutdown initiated." in line ]
    first_shutdown_dt = convert_to_datetime(shutdown_lines[0])
    last_shutdown_dt = convert_to_datetime(shutdown_lines[-1])
    return last_shutdown_dt - first_shutdown_dt