import csv
from track_orders import TrackOrders


def read_file(path_to_file: str, trackOrders: TrackOrders) -> list:
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            csv_reader = csv.reader(file, delimiter=",")
            for customer, order, day in csv_reader:
                trackOrders.add_new_order(customer, order, day)
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')


