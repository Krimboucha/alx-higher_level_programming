#!/usr/bin/python3
"""singly linked list"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        self.__data = value
        if type(value) is not int:
            raise TypeError("data must be an integer")

    @property
    def next(self):
        """next getter"""
        return self.__next

    @next.setter
    def next(self, value):
        """next setter"""
        self.__next = value
        if type(value) is not Node and value:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if not self.__head:
            new.next = None
            self.__head = new
        elif value < self.__head.data:
            new.next = self.__head
            self.__head = new
        else:
            h = self.__head
            while (h.next) and (h.next.data < value):
                h = h.next
            new.next = h.next
            h.next = new

    def __str__(self):
        char = []
        h = self.__head
        while h:
            char.append(str(h.data))
            h = h.next
        return "\n".join(char)
