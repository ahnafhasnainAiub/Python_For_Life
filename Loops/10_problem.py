# Implement an Exponential backoff strategy that doubles the wait time between retires, starting from 1 second, but stops after 5 tries

import time

wait_time = 1
attempts = 1
max_tries = 5

while attempts <= max_tries:
    print("Attempt",attempts, "wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1