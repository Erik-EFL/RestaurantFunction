""" import csv """
import csv
from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    """
    Analyzes a CSV log file and writes the results to a new file.

    Args:
        path_to_file: The path to the CSV log file to analyze.
        customer: The name of the customer to analyze.
        dish: The name of the dish to analyze.

    Returns:
        None.
    """
    # Read the log file and create a TrackOrders object
    content = TrackOrders()
    read_log_file(path_to_file, content)

    # Analyze the data and write the results to a new file
    with open('data/mkt_campaign.txt', mode="w", encoding="utf-8") as file:
        most_ordered_dish = content.get_most_ordered_dish_per_customer("maria")
        quantity_ordered = content.quantity_ordered("arnaldo", "hamburguer")
        never_ordered = content.get_never_ordered_per_customer("joao")
        days_never_visited = content.get_days_never_visited_per_customer(
            "joao"
        )

        file.write(
            f"{most_ordered_dish}\n"
            f"{quantity_ordered}\n"
            f"{never_ordered}\n"
            f"{days_never_visited}\n"
        )


def read_log_file(path_to_file, content):
    """
    Reads a CSV log file and adds the data to a TrackOrders object.

    Args:
        path_to_file: The path to the CSV log file to read.
        content: The TrackOrders object

    Returns:
        None.
    """
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
