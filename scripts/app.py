
import time
import sys

from helper import typewriter
from core import setup, get_list, recommendations


def run():
    """
    Running Mittsu.
    """

    name = setup()
    time.sleep(0.5)

    running = True

    while running:
        style = input(f"What type of recommendations are you looking for,"
                      f" {name}? [anime/manga]: ").lower()
        time.sleep(0.5)
        if style in ('anime', 'manga'):
            typewriter("\nPlease note that we are always looking to improve "
                       "and scale this application. \nHence, although we "
                       "will do our best to recommend you relevant and "
                       "enjoyable media, we may not be able to make "
                       "recommendations for every anime/manga.\n")
            time.sleep(2)

            # get the user anime/manga list and their recommendations.
            user_list = get_list(style, name)
            recommendations(style, user_list)
            
            typewriter('\nDone!\n')
            time.sleep(1)
            typewriter(f"Please check the local file directory for your"
                       f" {style} recommendations. \n")
            break

        else:
            typewriter("We're sorry... we couldn't understand the input. "
                       "Please try again.\n")
    
    outro = 'Thank you for using Mittsu. \nWe hope to see you again soon!'
    typewriter(outro[:27])
    time.sleep(0.5)

    typewriter(outro[28:])
    sys.exit(0)


run()
