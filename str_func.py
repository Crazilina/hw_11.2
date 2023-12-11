def capitalize_all(input_string):
    """
    Capitalizes all letters in the input string.
    """
    return input_string.upper()


def capitalize_first_letters(input_string):
    """
    Capitalizes the first letter of each word in the input string.
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
