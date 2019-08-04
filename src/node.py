#-----------------------------------------------------------------------#
# Name: Tarek Elseify
# File: node.py
# Date: 08/03/2019
# Description: This class is the blueprint for a binary tree node
#-----------------------------------------------------------------------#

# defines a node of a binary tree
#
class TreeNode:

    # initialize the object
    #
    def __init__(self, value):

        # set the value
        #
        self.val = value

        # parent and children initialized to None
        #
        self.parent = None
        self.left = None
        self.right = None
    #
    # end of init

    # method to set all the nodes
    #
    def set_all(self, parent, left, right):

        # set the values
        #
        self.parent = parent
        self.left = left
        self.right = right
    #
    # end of method

    # method to set children
    #
    def set_children(self, left, right):

        # set the values
        #
        self.left = left
        self.right = right
    #
    # end of method

    # method to set the parent
    #
    def set_parent(self, parent):

        # set the value
        #
        self.parent = parent
    #
    # end of method
#
# end of class
