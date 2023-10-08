class ShoppingList (object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        lowcase_item = item.lower()
        if lowcase_item in self.shopping_list:
            None
        else:
            self.shopping_list.append(lowcase_item)
            print("-----------------------------------------------")
            print(item + " has been added to the list: " + self.list_name + ".")
            print("-----------------------------------------------")

    def remove_item(self, item):
        if item.lower() in self.shopping_list:
            self.shopping_list.remove(item.lower())
            print("-----------------------------------------------")
            print(item + " has been removed from the list: " + self.list_name + ".")
            print("-----------------------------------------------")
        else:
            print("-----------------------------------------------")
            print(item + ' was not found on this list.')
            print("-----------------------------------------------")


    def view_list(self):
        print("-----------------------------------------------")
        print(self.shopping_list)
        print("-----------------------------------------------")

    def merge_lists(self, obj):
        merged_lists_name = 'Merged List - ' + self.list_name + ' + ' + obj.list_name
        merged_lists_obj = ShoppingList(merged_lists_name)
        merged_lists_obj.shopping_list = self.shopping_list.copy()

        for item in obj.shopping_list:
            lowcase_item = item.lower()
            if not lowcase_item in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(lowcase_item)

        return merged_lists_obj

pet_store_list = ShoppingList('Pet Store Shopping List')
grocery_store_list = ShoppingList('Grocery Store List')

pet_store_list.add_item('Dog Food')
pet_store_list.add_item('Frisbee')
pet_store_list.add_item('Bowl')
pet_store_list.add_item('Collars')
pet_store_list.add_item('Flea Collars')

for item in ['fruits', 'vegetables', 'bowl', 'ice cream']:
    grocery_store_list.add_item(item.lower())

pet_store_list.remove_item('Flea Collars')

pet_store_list.add_item('Frisbee')

pet_store_list.view_list()

merged_list = pet_store_list.merge_lists(grocery_store_list)

merged_list.view_list()