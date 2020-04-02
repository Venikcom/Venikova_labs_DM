import collections
import logging
import time
import threading

def worker(stopped):
    while not stopped.wait(1.5):
        logging.info("heartbeat")

logging.basicConfig(level=logging.INFO,
    format="%(relativeCreated)d %(threadName)s %(message)s")
events = collections.deque(maxlen=10)
while True:
    events.append(threading.Event())
    threading.Thread(target=worker, args=[events[-1]], daemon=True).start()
    if len(events) == 10:
        events.popleft().set()
    time.sleep(1 - time.monotonic() % 1)
