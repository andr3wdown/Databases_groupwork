numbers = None

def init():
    global numbers
    numbers = []
    with open("data/numbers.txt",  "r") as f:
        for line in f:
            numbers.append(line.strip())
            
def generate_phone_number() -> str:
    if numbers is None:
        init()
    new_number = 100000000 if len(numbers) == 0 else int(numbers[len(numbers) - 1][4:]) + 1 
    new_number = "+358" + str(new_number)
    numbers.append(new_number)
    with open("data/numbers.txt", "w") as f:
        f.write(new_number + "\n")
    return new_number

