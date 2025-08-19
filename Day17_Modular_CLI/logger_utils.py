import datetime

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_calculation(num1, num2, operator, result, filename="calc_log.txt"):
    timestamp = get_timestamp()
    with open(filename, 'a') as file:
        file.write(f"{timestamp}| {num1} {operator} {num2} = {result}\n")