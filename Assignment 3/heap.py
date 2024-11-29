'''
Python Code to implement a heap with general comparison function
'''
import custom
class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        self.data=custom.deep_copy(init_array)
        self.comparison_function=comparison_function
        
        # Write your code here
        pass
    
    def parent(self, j):
        return (j-1) // 2
    
    def left(self, j):
        return 2*j+1
    
    def right(self, j):
        return 2*j+2
    
    def has_left(self, j):
        return self.left(j)< len(self.data) # index beyond end of list?
    
    def has_right(self, j):
        return self.right(j) < len(self.data) # index beyond end of list?
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def upheap(self, j):
        parent = self.parent(j)
        if j > 0 and self.comparison_function(self.data[j] , self.data[parent]):
            self.swap(j, parent)
            self.upheap(parent) # recur at position of parent
    
    def downheap(self, j):
     if self.has_left(j):
        left = self.left(j)
        small_child = left # although right may be smaller
     if self.has_right(j):
        right = self.right(j)
     if self.has_right(j) and self.comparison_function(self.data[right] , self.data[left]):
         small_child = right
     if self.has_left(j) and self.comparison_function(self.data[small_child] , self.data[j]):
        self.swap(j, small_child)
        self.downheap(small_child)    
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        self.data.append(value)
        self.upheap(len(self.data) - 1)
        # Write your code here
        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        #if self.is empty( ):
            #raise Empty( Priority queue is empty. )
        self.swap(0, len(self.data) - 1) # put minimum item at the end
        item = self.data.pop( ) # and remove it from the list;
        self.downheap(0) # then fix new root
        return item
        # Write your code here
        pass
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        return self.data[0]
        # Write your code here
        pass
    
    # You can add more functions if you want to
