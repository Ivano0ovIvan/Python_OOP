def choice_pattern():
    pattern = input('Choice type of pattern ->\n -Triangle\n -Rhombus\n -Square\nPattern choice: ')
    pattern_size = int(input('Enter pattern size: '))

    return pattern, pattern_size


def print_pattern_data(space_data, stars_data):
    print(' ' * space_data + '* ' * stars_data)


def get_pattern_data(*data):
    pattern, size = data

    if pattern == 'Rhombus':
        for x in range(size):
            space_data = size - x - 1
            stars_data = x + 1
            print_pattern_data(space_data, stars_data)

        for x in range(size - 2, -1, -1):
            space_data = size - x - 1
            stars_data = x + 1
            print_pattern_data(space_data, stars_data)

    elif pattern == 'Triangle':
        for x in range(size):
            stars_data = x + 1
            print_pattern_data(0, stars_data)

    elif pattern == 'Square':
        for x in range(size):
            print_pattern_data(0, size)


get_pattern_data(*choice_pattern())  # with * returns list of pattern and pattern_size

