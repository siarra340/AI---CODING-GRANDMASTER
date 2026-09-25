#I tried my own with a shopping list code using abstraction and Inheritance

from abc import ABC, abstractmethod

class Shopping(ABC):

    def __init__(self, store, rating):
        self.store = store
        self.rating = rating

    def display(self):
        print(f"Store: {self.store} | Rating: {self.rating}")

    @abstractmethod
    def list(self):
        pass

class Store_1(Shopping):
    def __init__(self, store, rating, status):
        super().__init__(store, rating)
        self.status = status

    def list(self):
        print(f"{self.store} Shopping List ({self.status}): Tomatos, Carrots, Rice")

class Store_2(Shopping):
    def __init__(self, store, rating, location):
        super().__init__(store, rating)
        self.location = location

    def list(self):
        print(f"{self.store} ({self.location}): Paper, Cake, Air fryer")

class Store_3(Shopping):
    def __init__(self, store, rating, importance, items):
        super().__init__(store, rating)
        self.importance = importance
        self.items = items

    def list(self):
        print(f"{self.store}: {self.items} ==> Importance: {self.importance}")

store_1 = Store_1("South West Market", "⭐️⭐️⭐️⭐️", "Uncompleted")
store_2 = Store_2("Farm Fresh", "⭐️⭐️", "Oakville 52 Avenue")
store_3 = Store_3("Food and Beyond", "⭐️⭐️⭐️⭐️⭐️", "Urgent", "Book, Nuggets, Salmon, Onions")

print("\n=== Shopping/Groccery List ===")
for store in (store_1, store_2, store_3):
    store.display()
    store.list()
    print()
    





