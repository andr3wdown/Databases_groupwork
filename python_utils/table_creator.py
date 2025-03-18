import re
import random as rnd
from hotels_creator import create_hotels
from phone_number_generator import generate_phone_number
from name_generator import generate_name

def create_table_sql(template_path, output_path, operation, iterations):
    insert = ""
    ##add insert values
    insert, array = operation(insert, iterations)
    
    with open(template_path, "r") as f:
        content = f.read()
        
    content = re.sub("_inserts_", insert, content)
    with open(output_path, "w") as f:
        f.write(content)
    return array
    

def create_rooms(insert, num_rooms):
    rooms = []
    for i in range(num_rooms):
        hotel_id = rnd.randint(1, 2)
        capacity = rnd.randint(2, 8)
        daily_price = capacity * 150
        room_phone_nr = generate_phone_number()
        room = {"room_id" : i,"hotel_id": hotel_id, "capacity": capacity, "daily_price": daily_price, "room_phone_nr": room_phone_nr}
        rooms.append(room)
        sql = f'    ({hotel_id}, {capacity}, {daily_price}, "{room_phone_nr}")'
        if i != num_rooms - 1:
            sql += ",\n"
        else:
            sql += ";"
        insert += sql
    return insert, rooms

def create_person(insert, num_persons):
    persons = []
    for i in range(num_persons):
        f_name = generate_name(rnd.randint(4, 8))
        l_name = generate_name(rnd.randint(4, 8))
        phone_number = generate_phone_number()
        person = {"person_id": i, "f_name": f_name, "l_name": l_name, "phone_number": phone_number}
        persons.append(person)
        sql = f'    ("{f_name}", "{l_name}", "{phone_number}")'
        if i != num_persons - 1:
            sql += ",\n"
        else:
            sql += ";"
        insert += sql
    return insert, persons

def create_shifts(reservation, start_date, end_date):
    shifts = []
    for i in range(start_date, end_date):
        shift = {"room_id": reservation["room_id"], "employee_id": -1, "date": f"2025-03-{i}", "time": ""}
        shifts.append(shift)
    return shifts
    
def create_reservations_and_shifts(templates, outputs, rooms, employees, customers):
    reservations = []
    shifts = []
    rnd.shuffle(rooms)
    reservation_insert = ""
    for i in range(int(len(customers)/2)):
        customer = customers[i]
        room = rooms[i]
        sd = rnd.randint(1, 3)
        ed = rnd.randint(sd+1, 10)
        start_date = f"2025-03-{sd}"
        end_date = f"2025-03-{ed}"
        sql = f'    ({customer["person_id"]}, {room["room_id"]}, "{start_date}", "{end_date}")'
        sql += ",\n"
        reservation_insert += sql
        
        reservation = {"customer_id": customer["person_id"], "room_id": room["room_id"], "start_date": start_date, "end_date": end_date}
        reservations.append(reservation)
        shifts += create_shifts(reservation, sd, ed)

        
    for i in range(int(len(customers)/2), len(customers)):
        customer = customers[i]
        room_i = i - int(len(customers)/2)
        room = rooms[room_i]
        sd = rnd.randint(10, 13)
        ed = rnd.randint(sd+1, 20)
        start_date = f"2025-03-{sd}"
        end_date = f"2025-03-{ed}"
        
        sql = f'    ({customer["person_id"]}, {room["room_id"]}, "{start_date}", "{end_date}")'
        if i != len(customers) - 1:
            sql += ",\n"
        else:
            sql += ";"
        reservation_insert += sql
        
        reservation = {"customer_id": customer["person_id"], "room_id": room["room_id"], "start_date": start_date, "end_date": end_date}
        reservations.append(reservation)
        shifts += create_shifts(reservation, sd, ed)
    
    with open(templates[0], "r") as f:
        content = f.read()
    content = re.sub("_inserts_", reservation_insert, content)
    with open(outputs[0], "w") as f:
        f.write(content)
        
    shifts_dict = {}
    for i in range(len(shifts)):
        shift = shifts[i]
        if shift["date"] not in shifts_dict:
            shifts_dict[shift["date"]] = []
        shifts_dict[shift["date"]].append(shift)
    
    shifts_insert = ""
    counter = 0
    for date in set(shifts_dict):
        current_shifts = shifts_dict[date]
        current_employee = 0
        current_time = 10
        
        for i in range(len(current_shifts)):
            if current_employee == len(employees):
                current_employee = 0
                current_time += 2
            shifts_dict[date][i]["employee_id"] = current_employee
            shifts_dict[date][i]["time"] = f"{current_time}:00"
            current_employee += 1
            
            sql = f'    ({shifts_dict[date][i]["room_id"]}, {shifts_dict[date][i]["employee_id"]}, "{date}", "{shifts_dict[date][i]["time"]}")'
            if counter != len(shifts) - 1:
                sql += ",\n"
            else:
                sql += ";"
            counter += 1
            shifts_insert += sql
    with open(templates[1], "r") as f:
        content = f.read()
    content = re.sub("_inserts_", shifts_insert, content)
    with open(outputs[1], "w") as f:
        f.write(content)


if __name__ == "__main__":
    create_hotels()
    rooms = create_table_sql("templates/rooms.sql", "output/rooms.sql", create_rooms, 30)
    employees = create_table_sql("templates/employees.sql", "output/employees.sql", create_person, 10)
    customers = create_table_sql("templates/customers.sql", "output/customers.sql", create_person, 60)
    create_reservations_and_shifts(["templates/reservations.sql", "templates/shifts.sql"], ["output/reservations.sql", "output/shifts.sql"], rooms, employees, customers)
    
                