
import time
import sys


def loader(counter):
    """
    Creates a 'Loading...' line that repeats a number of times defined by
    the argument. Uses sys.stdout() to prevent moving to a new line as is
    the case for print().

    Arguments:
    counter - integer limit for repeat.
    """

    count = 0
    while True:
        for i in range(4):
            # carriage return to override content on current line.
            sys.stdout.write(f"\rLoading{'.' * i}")

            # flush the output from the buffer to prevent the system from
            # holding it.
            sys.stdout.flush()
            time.sleep(0.5)

        # clear from cursor to end of line and restart the line.
        sys.stdout.write('\033[K')

        # new string must be at least as long as prev. string or prev.
        # string will peek through.
        sys.stdout.write('\rLoading   ')

        # set break condition for while loop.
        count += 1
        if count == counter:
            sys.stdout.write('\rLoaded!   \n\n')
            time.sleep(0.5)
            break
