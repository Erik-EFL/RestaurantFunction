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

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
