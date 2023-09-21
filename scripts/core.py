
import time
import random
import requests

from jikanpy import Jikan
from helper import loader

# initialising an instance of jikan.
jikan = Jikan()


def setup():
    """
    Setting up the console app, introductory phase.
    """

    intro = "**** Welcome to Mittsu! **** Your favourite anime/manga " \
            "recommendation system. We can base recommendations on up to 3 " \
            "of your favourite anime or manga."
    
    # string slicing to print different sections of the introduction at
    # different times.
    print(f'\n{intro[:28]}\n')

    time.sleep(1)
    print(f'{intro[29:78]}\n')

    time.sleep(1)
    print(f'{intro[79:]}\n')

    loader(2)

    while True:
        name = input("Let's get to know each other. What should we call you? ")
        time.sleep(0.5)
        name_correct = input(f'Nice to meet you, {name}. Have we got your '
                             f'name correct? [Yes/No]: ').lower()

        time.sleep(0.5)
        if name_correct == "yes":
            print("\nGreat! Let's get started.\n")
            break
        elif name_correct == "no":
            print("\nI'm sorry. Let's try that again.")

    return name


def get_list(style, name):
    """
    Get and return a list of the user's favourite manga or anime.

    Arguments: 
    style - type of media to base recommendations,
        allowed values: 'anime' or 'manga'.
    name - name of user.
    """

    loader(4)

    print(f'To generate your {style} recommendations, we need a list of '
          f'your favourite {style}. Currently, we can take up to 3 {style}.')
    time.sleep(1)

    while True:
        temp = input(f'So {name}, tell us your favourite {style}! Please '
                     f'separate each {style} by a comma: ')

        # ensure we have 3 or fewer anime/manga.
        if (temp.count(',') + 1) > 3:
            time.sleep(0.5)
            print(f"\nHmmm... it seems you've given us too many {style}. "
                  f"Try that again.")
        else:
            break
    
    loader(2)

    print("We have received your list! Please give us a moment to compile "
          "your recommendations.")
    
    # put the user input into a list.
    # list() and map() inbuilt functions.
    user_list = list(map(str.strip, temp.split(",")))

    return user_list


def recommendations(style, user_list):
    """
    Write 5 anime/manga recommendations to a file based on the user's list
    of favourite anime/manga.

    Arguments:
    style - type of media to base recommendations,
        allowed values: 'anime' or 'manga'.
    user_list - list of user's favourite anime/manga, maximum of 3 titles.
    """

    for i in user_list:
        time.sleep(2)
        # get the info of an anime/manga using the jikanpy module.
        item_search = jikan.search(style, i)

        # put data from the input anime/manga into a dictionary.
        info = dict()

        # anime/manga title, (english title), url, genres and synopsis.
        info['Title'] = item_search['data'][0]['title']

        info['English Title'] = None
        for a in item_search['data'][0]['titles']:
            if a['type'] == 'English':
                info['English Title'] = a['title']

        info['URL'] = item_search['data'][0]['url']

        genres = []
        for e in item_search['data'][0]['genres']:
            genres.append(e['name'])
        info['Genres'] = genres

        info['Synopsis'] = item_search['data'][0]['synopsis']

        # dump the basis anime/manga into a file first.
        with open(f'{style.title()} recommendations based on '
                  f'{i.title()}.md', 'w+') as file:

            file.write(f'\n# Your {style} input: \n\n')
            for key, value in info.items():
                file.write(f'{key}: {value}\n\n')
                
            file.write(f'\n# Your {style} recommendations: \n\n')

        # get recommendations based on the original anime.
        item_id = item_search['data'][0]['mal_id']
        pull = requests.get(f'https://api.jikan.moe/v4/anime/'
                            f'{item_id}/recommendations')
        item = pull.json()

        # get 5 random recommendations for an anime.
        count = 1
        while count < 6:

            # check for a ValueError (e.g. if the pull is empty) or KeyError
            # (e.g. if there's no data / returns
            # an invalid response code).

            try:
                index = random.randint(0, len(item['data']) - 1)
                title = item['data'][index]['entry']['title']
            
            except (ValueError, KeyError):
                with open(f'{style.title()} recommendations based on'
                          f' {i.title()}.md', 'a+') as file:
                    file.write(f"I'm sorry, we cannot currently generate "
                               f"recommendations based on the {style} "
                               f"{title}.")
                    break

            # get info on the randomly chosen anime recommendation based on
            # its title.
            rec_search = jikan.search(style, title)

            # put info into a dictionary.
            rec = dict()
            rec['Title'] = rec_search['data'][0]['title']

            rec['English Title'] = None
            for a in rec_search['data'][0]['titles']:
                if a['type'] == 'English':
                    rec['English Title'] = a['title']

            rec['URL'] = rec_search['data'][0]['url']

            genres = []
            for e in rec_search['data'][0]['genres']:
                genres.append(e['name'])
            rec['Genres'] = genres

            rec['Synopsis'] = rec_search['data'][0]['synopsis']

            with open(f'{style.title()} recommendations based on '
                      f'{i.title()}.md', 'a+') as file:

                # check if the title of a recommendation is already in the
                # file.
                text = file.read()
                if rec['Title'] in text:
                    continue
                
                # dump each recommendation into the og file.
                for key, value in rec.items():
                    file.write(f'{key}: {value}\n\n')
                file.write("\n")

            time.sleep(2)
            count += 1
