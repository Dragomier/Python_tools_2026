from csv import reader

def load_data(filename: str):
    with open(filename) as file:
        csv_reader = reader(file)
        # Last column determines Species, it is useless for calculations
        rows  = [row[:-1] for row in csv_reader]
        cols = [[rows[row][index] for row in range(1, len(rows))] for index in range(len(rows[0]))]
        # We return observations as list of rows and additional list of column names
        return [[list(map(float, col)) for col in cols], [""] + [rows[0][index] for index in range(len(rows[0]))]]

