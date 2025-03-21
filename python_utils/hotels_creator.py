import re
from phone_number_generator import generate_phone_number

names = ["Trivago", "Korvatunturi"]
adresses = ["Joulukylänkuja 2, Korvatunturi 80010", "Korvatunturintie 1, Korvatunturi 80000"]
def create_hotels():
    insert = ""
    for i in range(len(names)):
        name = names[i]
        address = adresses[i]
        phone_number = generate_phone_number()
        sql = f'    ("{name}", "{address}", "{phone_number}")'
        if i != len(names) - 1:
            sql += ",\n"
        else:
            sql += ";"
        insert += sql
    with open("templates/hotels.sql", "r") as f:
        content = f.read()
        
    content = re.sub("_inserts_", insert, content)
    with open("output/hotels.sql", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    create_hotels()