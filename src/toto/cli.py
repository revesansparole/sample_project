from sys import argv


def main():
    """Example script, print stuff, return passed argument
    If one exists on the command line.

    Author: myself
    """
    if len(argv) > 1:
        a = int(argv[1])
    else:
        a = -1
    
    print "execution script"
    print "a", a
    return a * 10
