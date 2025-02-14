import re
import os
from phone_number_generator import generate_phone_number
from name_generator import generate_name

def create_table_sql(template_path, output_path, operation):
    insert = ""
    ##add insert values
    operation()
    
    with open(template_path, "r") as f:
        content = f.read()
        
    content = re.sub("_inserts_", insert, content)
    with open(output_path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    user_input = ""
    while os.path.isfile(f"templates/{user_input}.sql") == False:
        user_input = input("Enter table name: ")
    
    path = f"templates/{user_input}.sql"
    output = f"output/{user_input}.sql"
    create_table_sql()            