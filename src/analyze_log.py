""" import csv """
import csv
from track_orders import TrackOrders


def analyze_log(path_to_file):
    """ this function parses and writes a new document from specific
    information provided by the user """
    content = TrackOrders()

    if not path_to_file.lower().endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=",")
            for customer, order, day in csv_reader:
                content.add_new_order(customer, order, day)
    except FileNotFoundError as err:
        raise FileNotFoundError(
            f"Arquivo inexistente: {path_to_file}"
        ) from err

    most_ordered_dish = content.get_most_ordered_dish_per_customer("maria")
    quantity_ordered = content.quantity_ordered("arnaldo", "hamburguer")
    never_ordered = content.get_never_ordered_per_customer("joao")
    days_never_visited = content.get_days_never_visited_per_customer("joao")

    with open('data/mkt_campaign.txt', mode="w", encoding="utf-8") as file:
        file.write(
            f"{most_ordered_dish}\n"
            f"{quantity_ordered}\n"
            f"{never_ordered}\n"
            f"{days_never_visited}\n"
        )
