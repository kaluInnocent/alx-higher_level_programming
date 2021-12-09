#!/usr/bin/python3
"""A Node class"""


class Node:
    """A class representing a Node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Method Initializes a node class
        Args:
            data (int): data to be added to the node
            next_node (None): empty head of the list
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """A method that getss the value of data of a node"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """"A method that sets the value of data
        Args:
            value (int): A value to be set
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")
    
    @property
    def next_node(self):
        """A method that retrieves the value of data in next node"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """ A method that sets value to the data of next_node
        Args:
            value (Node): A node class
        """
        if isinstance(value, Node) and value == None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
    

class SinglyLinkedList:
    """Defines a sinlgy linked list"""

    def __init__(self):
        """instantiaties a new linked list"""
        self.__head = None
    
    def __str__(self):
        """A method to print the data stored in a linked list"""
        temp = self.__head
        node_data = ""
        if not self.__head:
            return

        while temp:
            try:
                node_data += str(temp.data)
                node_data = '\n'
                temp = temp.next_node
            except:
                pass
        return node_data[:-1]
    
    def sorted_insert(self, value):
        """Method adds a new node in a sorted order
        Args:
            value (int): Value to be added to the list
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        if value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        temp = self.__head
        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new
