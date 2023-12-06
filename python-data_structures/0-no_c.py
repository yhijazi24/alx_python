def no_c(my_string):
    filtered_chars = [char for char in my_string if char.lower() != 'c']

    result_string = ''.join(filtered_chars)

    return result_string