# Some basic list manipulation from lab

def insert_items(s, before, after):
    # loop through the list and if the item is = to before insert the number in the digit after

    for i in range(len(s)):
        if s[i] == before:
            s.insert(i, after)
        if before == after:
            i += 1

    return s

def group_by(s, fn):
    # loop through list and caclulate the key and add it into the grouped dictionary if it is not in already 
    grouped = {}
    for ____ in ____:
        key = ____
        if key in grouped:
            ____
        else:
            grouped[key] = ____
    return grouped


def partial_reverse(s, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"

