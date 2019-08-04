#-----------------------------------------------------------------------#
# Name: Tarek Elseify
# File: min_heap.py
# Date: 08/03/2019
# Description: This class creates a MinHeap data structure
#-----------------------------------------------------------------------#

# defines the min heap data structure
#
class MinHeap:

    # takes in a list as an argument
    #
    def __init__(self, array):

        # set the array
        #
        self.sorted_array = array

        # get the size
        #
        self.size = len(self.sorted_array)

        # heapify the array ... O(N log N)
        #
        self.heapify(self.sorted_array)
    #
    # end of init
        
    # defines the heapify method
    #
    def heapify(self, array):

        # traverse the list backwards
        #
        for index in range(self.size - 1, -1, -1):

            # sink the element
            #
            self.sink(index)

        # exit gracefully
        #
        return True
    #
    # end of method

    # method to remove the min element from the heap
    #
    def remove_min(self):

        # if the heap is empty
        #
        if(self.size == 0):

            # raise an error
            #
            raise IndexError('Attemped to remove min from empty heap!')

        # store the value of the root
        #
        min_val = self.sorted_array[0]

        # set the root to be the last element
        #
        self.sorted_array[0] = self.sorted_array[self.size - 1]

        # remove the last element in the array ...O(1) for the last item
        #
        self.sorted_array.pop()

        # decrease the size
        #
        self.size -= 1

        # sink the root
        #
        self.sink(0)
        
        # return the min value
        #
        return min_val
    #
    # end of method
    
    # method to insert an element into the heap
    #
    def insert(self, element):

        # add the element to the end of the array
        #
        self.sorted_array.append(element)

        # increment the size of the heap
        #
        self.size += 1

        # make the last element swim ... O(log N)
        #
        self.swim(self.size - 1)
    #
    # end of method
    
    # method to sink a node
    #
    def sink(self, index):

        # set the parent index
        #
        p_index = index
        
        # while there are children
        #
        while self.has_children(p_index):
        
            # get the indices of potential children nodes
            #
            l_index = self.get_left_child_node(p_index)
            r_index = self.get_right_child_node(p_index)

            # get the parent and left value
            #
            p_val = self.sorted_array[p_index]
            l_val = self.sorted_array[l_index]
            
            # if there are two children
            #
            if self.has_both_children(p_index):

                # get the value of the right child
                #
                r_val = self.sorted_array[r_index]
                
                # if the left is smaller than the right and the parent
                #
                if(l_val <= r_val) and (l_val < p_val):

                    # swap the left child and parent
                    #
                    self.swap_values(p_index, l_index)

                    # set the parent as the left node
                    #
                    p_index = l_index

                # if the right is smaller than the left and the parent
                #
                elif(r_val < l_val) and (r_val < p_val):

                    # swap the right child and parent
                    #
                    self.swap_values(p_index, r_index)

                    # set the parent as the right node
                    #
                    p_index = r_index

                # this is already sorted
                #
                else:

                    # do not continue
                    #
                    return True

            # there is only a left child, check to see if it is smaller
            #
            elif (l_val <= p_val):

                # swap the values
                #
                self.swap_values(p_index, l_index)

                # set the parent as the left node
                #
                p_index = l_index

            # this is already sorted
            #
            else:
            
                # do not continue
                #
                return True

        # unreachable
        #
        return False
    #
    # end of method

    # method to make a node swim
    #
    def swim(self, index):

        # set the current index/val
        #
        c_index = index
        
        # while we are not at the root
        #
        while c_index != 0:
        
            # set the current val
            #
            c_val = self.sorted_array[c_index]
            
            # get the parent index/val
            #
            p_index = self.get_parent_node(c_index)
            p_val = self.sorted_array[p_index]

            # if the current is smaller than the parent
            #
            if(c_val < p_val):

                # swap the parent and child
                #
                self.swap_values(p_index, c_index)

                # set current index to the parent
                #
                c_index = p_index

            # the array is already sorted
            #
            else:

                # do not continue
                #
                return True

        # unreachable
        #
        return False
    #
    # end of method
    
    # method to swap values of parent/node
    #
    def swap_values(self, parent_index, child_index):

        # hold a temp value
        #
        temp = self.sorted_array[parent_index]

        # make the parent value the child's value
        #
        self.sorted_array[parent_index] = self.sorted_array[child_index]

        # make the child the temp value
        #
        self.sorted_array[child_index] = temp
    #
    # end of method
        
    # method to determine if node has any children
    #
    def has_children(self, index):

        # return the appropriate boolean
        #
        if self.has_right_child(index) or self.has_left_child(index):
            return True
        return False
    #
    # end of method

    # method to determine if node has both children
    #
    def has_both_children(self, index):

        # return the appropriate boolean
        #
        if self.has_right_child(index) and self.has_left_child(index):
            return True
        return False
    #
    # end of method
    
    # method to see if node has a right child
    #
    def has_right_child(self, index):

        # if it is within the bounds of the array
        #
        if self.get_right_child_node(index) < self.size:
            return True
        return False
    #
    # end of method

    # method to see if node has a left child
    #
    def has_left_child(self, index):

        # if it is within the bounds of the array
        #
        if self.get_left_child_node(index) < self.size:
            return True
        return False
    #
    # end of method

    # method to get the parent of the current node
    #
    def get_parent_node(self, index):
        
        # return the index of the parent node
        #
        return int((index - 1)//2)
    #
    # end of method
    
    # method to get the right child of node
    #
    def get_right_child_node(self, index):

        # return the index of the right child node
        #
        return int((index * 2) + 2)
    #
    # end of method
    
    # method to get the left child of node
    #
    def get_left_child_node(self, index):

        # return the index of the left child node
        #
        return int((index * 2) + 1)
    #
    # end of method

    # method to return the array as a list
    #
    def get_list(self):

        # return the list
        #
        return self.sorted_array
    #
    # end of method
#
# end of class
