class TrackOrders:
    # aqui deve expor a quantidade de estoque
    # começando o projeto
    def __init__(self):
        self.orders = []
        self._customers = set()
        self._orders = set()
        self._days = set()

    def __len__(self) -> int:
        return len(self.orders)

    def quantity_ordered(self, customer: str, dish: str) -> int:
        counter = 0

        for order in self.orders:
            if order["customer"] == customer and order["order"] == dish:
                counter += 1

        return counter

    def counter_most_frequent(self, customer: str):
        counter = {}
        for item in customer:
            counter[item] = counter.get(item, 0) + 1

        return max(counter, key=counter.get)

    def counter_lass_frequent(self, customer: str):
        counter = {}
        for item in customer:
            counter[item] = counter.get(item, 0) + 1

        return min(counter, key=counter.get)

    def add_new_order(self, customer: str, order: str, day: str):
        self.orders.append({"customer": customer, "order": order, "day": day})
        self._customers.add(customer)
        self._orders.add(order)
        self._days.add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        dishes = [
            entry["order"]
            for entry in self.orders
            if entry["customer"] == customer
        ]
        return self.counter_most_frequent(dishes)

    def get_never_ordered_per_customer(self, customer):
        ordered = {
            entry["order"]
            for entry in self.orders
            if entry["customer"] == customer
        }
        return self._orders - ordered

    def get_days_never_visited_per_customer(self, customer):
        days = {
            entry["day"]
            for entry in self.orders
            if entry["customer"] == customer
        }
        return self._days - days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
