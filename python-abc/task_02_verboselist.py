#!/usr/bin/python3
"""verbose kalsi"""


class VerboseList(list):
    """emeliyyatlari cap eden klas"""

    def append(self, item):
        """elave etme emeliyyati"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """toplu elave etme"""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """silme emeliyyati"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """pop emeliyyati"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
