from csv import writer

def save_data(filename: str, data: list):
    with open(filename, 'w', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerows(data)