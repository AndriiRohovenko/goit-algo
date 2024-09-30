from queue import Queue
import hashlib
import json
from time import sleep
# install Faker lib
from faker import Faker
import random


queue = Queue()
fake = Faker()

def generate_random_request_body() -> dict:
    return {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "age": random.randint(18, 80),
        "job": fake.job(),
        "company": fake.company(),
        "date": fake.date()
    }


def generate_hashed_request():
    try:
        request = generate_random_request_body()
        request_str = json.dumps(request, sort_keys=True)
        hash_request = hashlib.sha256(request_str.encode()).hexdigest()
        request = {hash_request: request}
        queue.put(request)
        print(f"Request is generated - The queue size : {queue.qsize()}")
        return request
    except Exception as ex:
        print(f"An error has been occurred.{ex}")


def process_request(delay: float):
    try:
        if queue.not_empty:
            size = queue.qsize()
            for _ in range(size):
                request = queue.get()
                print(f"Proceeding with request {request}")
                sleep(delay)
                size = queue.qsize()
                print(f"request was proceeded: The queue size : {size}")
        
        print("The queue is empty!")

    except Exception as ex:
        print(f"An error has been occurred.{ex}")


if __name__ == "__main__":

    while True:
        user_input = input("Enter a command - generate or process (type 'exit' to quit): ").strip().lower()
        
        if user_input == "exit" or user_input == "quit":
            print("Exiting the program. Goodbye!")
            break 

        elif user_input == "generate":
            while True:
                request_count_input = input("Enter how many requests should be generated (int numbers only): ").strip()
                
                # Validate if the input is an int
                if request_count_input.isdigit():
                    request_count = int(request_count_input)
                    break
                else:
                    print("Please enter a valid integer.")

            for _ in range(request_count):
                generate_hashed_request()

        elif user_input == "process":
            process_request(2.5)

        else:
            print(f"Use specify commands: generate/process/exit - The queue size : {queue.qsize()}")




    