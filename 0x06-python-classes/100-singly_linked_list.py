#!/usr/bin/python3
"""This module defines a node of singly linked list
"""


class Node:
    """Define a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """Initialize all the data

        Args:
            data: data of the singly linked list
            next_node = reference to the next node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Get data of the object
        """
        return self.__data

    @property
    def next_node(self):
        """Get the reference of the next object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set new reference for the next element
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @data.setter
    def data(self, value):
        """Set the object's data
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value


class SinglyLinkedList:
    """Defines a singly linked list
    """
    def __init__(self):
        """Initialize the singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts ordered elements in a singly linked list
        """
        new = Node(value, None)
        if self.__head is None:
            self.__head = new
        else:
            node = self.__head
            prev = None
            while node is not None\
                    and node.data < value:
                prev = node
                node = node.next_node
            if node is self.__head:
                new.next_node = node
                self.__head = new
            else:
                prev.next_node = new
                new.next_node = node

    def __str__(self):
        """Prints all elements of the list, line by line
        """
        node = self.__head
        while node.next_node is not None:
            print("{:d}".format(node.data))
            node = node.next_node
        return str(node.data)
