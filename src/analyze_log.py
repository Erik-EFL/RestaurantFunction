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


def write_file(content: str) -> None:
    most_ordered_dish = content.get_most_ordered_dish_per_customer("maria")
    quantity_ordered = content.quantity_ordered("arnaldo", "hamburguer")
    never_ordered = content.get_never_ordered_per_customer("joao")
    days_never_visited = content.get_days_never_visited_per_customer("joao")

    with open('data/mkt_campaign.txt', "w") as file:
        file.write(
            f"{most_ordered_dish}\n"
            f"{quantity_ordered}\n"
            f"{never_ordered}\n"
            f"{days_never_visited}\n"
        )


