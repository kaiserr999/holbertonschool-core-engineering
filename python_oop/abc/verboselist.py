#!/usr/bin/env python3
"""
Module providing the VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications upon modification.
    """

    def append(self, item):
        """
        Adds an item to the list and prints a notification.

        Args:
            item: The item to add.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item_list):
        """
        Extends the list with items from an iterable and prints a notification.

        Args:
            item_list (iterable): The items to add.
        """
        super().extend(item_list)
        print("Extended the list with [{}] items.".format(len(item_list)))

    def remove(self, item):
        """
        Removes an item from the list and prints a notification.

        Args:
            item: The item to remove.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list and prints a notification.

        Args:
            index (int, optional): The index to pop. Defaults to -1.

        Returns:
            The popped item.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
