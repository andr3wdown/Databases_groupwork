from table_creator import create_reservations

if __name__ == "__main__":
    l1 = []
    l2 = []
    l3 = []
    for i in range(30):
        l1.append(i)
    for i in range(10):
        l2.append(i)
    for i in range(60):
        l3.append(i)
    create_reservations("templates/reservations.sql", "output/reservations.sql", l1, l2, l3)
