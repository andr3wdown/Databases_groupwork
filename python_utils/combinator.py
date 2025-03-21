import os


def combine_files(path):
    files = ["hotels.sql", "rooms.sql", "customers.sql", "employees.sql", "reservations.sql", "shifts.sql"]
    files = [os.path.join(path, f) for f in files]
    with open(os.path.join(path, 'combined.sql'), 'w') as outfile:
        for fname in files:
            with open(fname) as infile:
                outfile.write('\n')
                outfile.write(infile.read())
                outfile.write('\n')

if __name__ == '__main__':
    combine_files('../creation')