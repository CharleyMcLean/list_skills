"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    # Iterate through the list and print each item.
    for item in items: 
        print item




def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """
    # Create an empty list for the words longer than 4 characters.
    words_longer_than_four = []

    # Iterate over the list of words and check their length.
    # Append word to list if it meets the conditions.
    for word in words:

        if len(word) > 4:
            words_longer_than_four.append(word)

    return words_longer_than_four




def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    # Create an empty list for the words longer than n characters.
    words_longer_than_n = []

    # Iterate over the list of words and check their length.
    # Append word to list if it meets the conditions.
    for word in words:

        if len(word) > n:
            words_longer_than_n.append(word)

    return words_longer_than_n




def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """

    # Check if list is empty.  If it is, return None (fail fast).
    if numbers == []:
        return None

    # Iterate through the list to check if each number is less than the
    # current value of the smallest integer.
    smallest_integer = numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i] < smallest_integer:
            smallest_integer = numbers[i]

    return smallest_integer




def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """

    # Check if list is empty.  If it is, return None (fail fast).
    if numbers == []:
        return None

    # Iterate through the list to check if each number is greater than the
    # current value of the largest integer.
    largest_integer = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest_integer:
            largest_integer = numbers[i]

    return largest_integer




def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    # Create an empty list to hold the halved numbers.
    halved_list = []
    
    # Iterate through number list.  Convert values to floats. Divide by 2.
    for number in numbers:
        halved_number = float(number) / 2
        halved_list.append(halved_number)
    
    return halved_list




def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    # Create an empty list to hold the word lengths.
    word_length_list = []

    # Iterate through word list.  Add word lengths to new list.
    for word in words:
        word_length_list.append(len(word))
    
    return word_length_list




def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """

    # Check if list is empty.  If it is, return 0.
    if numbers == []:
        return 0

    # Create a counter.
    sum_of_numbers = 0

    # Iterate through the list.  Add each number to the counter.
    for number in numbers:
        sum_of_numbers = sum_of_numbers + number

    return sum_of_numbers




def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    # Check if list is empty.  If it is, return 1.
    if numbers == []:
        return 1

    # Create a counter.
    product_of_numbers = 1

    # Iterate through the list.  Multiply the counter by each number.
    for number in numbers:
        product_of_numbers = product_of_numbers * number

    return product_of_numbers




def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    # Check if words is an empty list.  If so, return an empty string.
    if words ==[]:
        return ''

    # Create an empty string.
    joined_strings = ''
    
    # Iterate through the list of words and concatenate.
    for word in words:
        joined_strings = joined_strings + word

    return joined_strings




def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    # Checking if the list is empty.
    if numbers == []:
        return "No defined answer."

    # Completing the function with a for loop.
    # Create a counter for the sum of the numbers in the list.
    # Iterate over the list and sum the numbers.
    number_sum = 0

    for number in numbers:
        number_sum = number_sum + number

    average_of_numbers = number_sum / float(len(numbers))

    return average_of_numbers


     # Completing the function without a for loop.
    average_of_numbers_2 = sum(numbers) / float(len(numbers))
    
    return average_of_numbers_2




def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    # Check if words is an empty list.  If so, return an empty string.
    if words ==[]:
        return ''


    # If only one word in list, return that word.
    if len(words) == 1:
        return words[0]

    
    # Begin with string containing first element of list.
    # Iterate through the list of words and concatenate separated by a comma.
    comma_joined_strings = words[0]
    for i in range(1, len(words)):
        comma_joined_strings = comma_joined_strings + ", " + words[i]

    return comma_joined_strings




def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    # Complete the function using a for loop.
    # Create an empty list.
    reversed_list = []

    for i in range(len(items) - 1, -1, -1):
        reversed_list.append(items[i])

    return reversed_list


    # Complete the function using list slicing.
    reversed_list_2 = items[::-1]

    return reversed_list_2




def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    for i in range(len(items) - 1):
        popped_item = items.pop(0)
        items.append(popped_item)

    return items


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """

    return []


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    return []

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
