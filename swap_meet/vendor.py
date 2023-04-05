from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None): 
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False        # IF raise exception it will stop the whole program, for example it will not be necessery to have line 26-28 to return F
    
    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:           
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
    
    def swap_first_item(self, other_vendor):

        if self.inventory == [] or other_vendor.inventory == []: 
            # Empty list is not equal to default None. Because line 5 `[]` is passed to inventory.
            return False
        else:
            my_first = self.inventory[0]
            friend_first = other_vendor.inventory[0]
            self.remove(my_first)
            other_vendor.add(my_first)
            other_vendor.remove(friend_first)
            self.add(friend_first)
            return True