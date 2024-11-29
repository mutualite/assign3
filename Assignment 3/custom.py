# You can add any additional function and class you want to implement in this file
import heap
class Item:
    __slots__='key','value'
    def __init__(self,key,value):
        self.key=key
        self.value=value
def deep_copy(original):
    # Check if the input is a list
    if isinstance(original, list):
        # Create a new list to store the deep copy
        copied_list = []
        # Iterate over each element in the original list
        for element in original:
            # If the element is a list, recursively deep copy it
            copied_list.append(deep_copy(element))
        # Return the deep copied list
        return copied_list
    else:
        # If it's not a list, return the element (base case)
        return original

def deep_copy_heap(treas):
    newtreas=heap.Heap(lambda a, b: a<b,[])
    for tr in treas:
        newtreas.insert([tr.arrival_time,tr.size])

    return newcrewmates
