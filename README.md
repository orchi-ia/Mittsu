# Mittsu

**Japanese:**

三つ 【みっつ】

*number, noun*
* meaning: three (3).
* also written as: 3つ.

Mittsu is a console application app that uses the Jikan API[[1](#Ref1)] to recommend anime/manga to users based on up to 3 anime/manga they know and love.

For this project the Jikan API was used for recommendation purposes, however its capabilities extend to receiving data on characters, clubs, producers, reviews and seasons among other categories.


## Features

• Receives up to 3 anime from a user and returns 5 recommendations (per anime input) for other anime they may love in file format.

• Receives up to 3 manga from a user and returns 5 recommendations (per manga input) for other manga they may love in file format.


## Dependencies

This application requires the `time`[[2](#Ref2)], `sys`[[3](#Ref3)], `random`[[4](#Ref4)], `requests`[[5](#Ref5)] and `jikanpy v4`[[6](#Ref6)] Python modules. All dependencies can be installed into a Python environment using the Anaconda platform (`conda`) and/or from PyPi (via `pip`) according to:

```python
conda install <module>
```

or

```python
pip install <module>
```

### More on the modules used

The `time` module provides numerous functions that allow the user to perform time-related tasks. This module was helpful to stagger the information shown to the user and to avoid rate limit errors from the API.

The `sys` module allowed for the interaction with the interpreter. This module was used to flush the output and to avoid moving to a new line in the `loader()` function.

The `random` module generates psuedo-random numbers which helped to limit the number of recommendations made to the user.

The `requests` module works in tandem with APIs as it allows for making calls to and receiving data from an API that can be reformatted using `.json()`[[7](#Ref7)].

The `jikanpy v4` module is a Python wrapper (code to modify/extend the capabilities of an existing function) for the Jikan API. This was used to search for anime/manga by name (and return its My Anime List (MAL)[[8](#Ref8)] ID) according to the user input as the Jikan API returns information based on a MAL ID.

## Instructions

To use this app, clone the Mittsu repository onto your desktop using the GitHub Desktop application or using the git `clone` command:

```python
git clone https://github.com/orchi-ia/Mittsu.git
```


Navigate into the scripts folder within your terminal and run the `app.py` file with the python command, for example:

```python
python app.py
```

or

```python
python3 app.py
```

• Note: If running the app from the global terminal, ensure you have Python installed in the global environment. Otherwise, run Mittsu from the terminal of a virtual Python environment.


## References

1. <a name="Ref1"></a>[https://docs.api.jikan.moe](https://docs.api.jikan.moe)
2. <a name="Ref2"></a>[https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)
3. <a name="Ref3"></a>[https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)
4. <a name="Ref4"></a>[https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)
5. <a name="Ref5"></a>[https://requests.readthedocs.io](https://requests.readthedocs.io)
6. <a name="Ref6"></a>[https://jikanpy.readthedocs.io](https://jikanpy.readthedocs.io)
7. <a name="Ref7"></a>[https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON#](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON#)
8. <a name="Ref8"></a>[https://myanimelist.net](https://myanimelist.net)

