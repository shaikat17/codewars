def string_clean(s):

    """

    Function will return the cleaned string

    """

    return ''.join('' if ch.isdigit() else ch for ch in s)

