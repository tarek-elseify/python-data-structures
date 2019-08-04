#-----------------------------------------------------------------------#
# Name: Tarek Elseify
# File: binary_search_tree.py
# Date: 08/03/2019
# Description: This class is implements a BST as a class
#-----------------------------------------------------------------------#

# import the tree node module
#
from node import TreeNode

# defines the binary search tree data structure
#
class BinarySearchTree:

    # takes in a list as an argument
    #
    def __init__(self, array = None):

        # set the root
        #
        self.root = None

        # get the size
        #
        self.size = 0

        # initialize the BST
        #
        self.initialize(array)
    #
    # end of init

    # initializes a BST from an array
    #
    def initialize(self, array):

        # if no array was given
        #
        if array is None:

            # set size to 0
            #
            self.size = 0

            # do nothing
            #
            return True

    #
    # end of method

    # method to insert an element into the BST
    #
    def insert(self, value):

        # initialize a tree node
        #
        node = TreeNode(value)

        # if the BST is empty
        #
        if self.size == 0:

            # set this as the root
            #
            self.root = node

            # do nothing
            #
            return True

        # start at the root
        #
        current = self.root

        
