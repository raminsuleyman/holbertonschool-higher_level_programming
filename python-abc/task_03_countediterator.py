#!/usr/bin/python3
"""
İterasiya olunan elementləri sayan CountedIterator klası.
"""


class CountedIterator:
    """İteratoru bükən (wrap) və elementləri sayan klas."""

    def __init__(self, iterable):
        """
        İteratoru və sayğacı başladır.

        Args:
            iterable: Üzərində gəzilə bilən obyekt (list, tuple və s.)
        """
        self.counter = 0
        self.iterator = iter(iterable)

    def get_count(self):
        """İndiyə qədər götürülmüş elementlərin sayını qaytarır."""
        return self.counter

    def __next__(self):
        """
        Növbəti elementi qaytarır və sayğacı artırır.
        Əgər element bitibsə, StopIteration xətası atır.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
