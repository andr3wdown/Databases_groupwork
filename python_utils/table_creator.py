import re
import os
import random as rnd
from hotels_creator import create_hotels
from phone_number_generator import generate_phone_number
from name_generator import generate_name

def create_table_sql(template_path, output_path, operation, iterations):
    insert = ""
    ##add insert values
    insert = operation(insert, iterations)
    
    with open(template_path, "r") as f:
        content = f.read()
        
    content = re.sub("_inserts_", insert, content)
    with open(output_path, "w") as f:
        f.write(content)

def create_rooms(insert, num_rooms):
    for i in range(num_rooms):
        hotel_id = rnd.randint(1, 2)
        capacity = rnd.randint(2, 8)
        daily_price = capacity * 150
        room_phone_nr = generate_phone_number()
    
        sql = f'    ({hotel_id}, {capacity}, {daily_price}, "{room_phone_nr}")'
        if i != num_rooms - 1:
            sql += ",\n"
        else:
            sql += ";"
        insert += sql
    return insert

def create_person(insert, num_persons):
    for i in range(num_persons):
        f_name = generate_name(rnd.randint(4, 8))
        l_name = generate_name(rnd.randint(4, 8))
        phone_number = generate_phone_number()
        sql = f'    ("{f_name}", "{l_name}", "{phone_number}")'
        if i != num_persons - 1:
            sql += ",\n"
        else:
            sql += ";"
        insert += sql
    return insert

if __name__ == "__main__":
    create_hotels()
    create_table_sql("templates/rooms.sql", "output/rooms.sql", create_rooms, 30)
    create_table_sql("templates/employees.sql", "output/employees.sql", create_person, 10)
    create_table_sql("templates/customers.sql", "output/customers.sql", create_person, 30)
    
    
                