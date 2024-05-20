import textwrap


def wrap(string, max_width):
    list_string = textwrap.wrap(string, max_width)
    # Wrap a single paragraph of text, returning a list of wrapped lines
    result = ""
    for x in list_string:
        result += x + '\n'
    return result


print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))

# output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ