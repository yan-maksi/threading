import threading
import random

counter = 0
our_counter = 0
thread_count = 5

threads = []

job = None
locker = threading.Lock()
thread = threading.current_thread()
current_thread = threading.current_thread()
queue = list(map(lambda x: ('main', random.randrange(5)), range(20)))
