bcolors = {
        'header': '\033[95m',
        'blue': '\033[94m',
        'green': '\033[92m',
        'red': '\033[91m',
        'yellow': '\033[93m',
        'fail': '\033[91m',
        'end': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m'
}

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


def printc(text, color='blue'):
    print('{0}{1}{2}'.format(bcolors[color], text, bcolors['end']))


def print_colors_names():
    for color in bcolors.keys():
        print(color)


if __name__ == '__main__':
    # print('color the output module')
    pass
