"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from a dictionary."""

    def __init__(self, path):
        """Read dictionary and report the number of items read.

        Args:
            path (str): The path to the dictionary file.
        """
        # Open the dictionary file
        dict_file = open(path)

        # Parse the file and store the words in self.words
        self.words = self.parse(dict_file)

        # Print the number of words read
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file and return a list of words.

        Args:
            dict_file (file): The file object representing the dictionary.

        Returns:
            list: A list of words parsed from the file.
        """
        # Strip leading and trailing whitespaces for each word in the file
        return [w.strip() for w in dict_file]

    def random(self):
        """Return a random word from the list of words.

        Returns:
            str: A random word.
        """
        # Use random.choice to select a random word from the list
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments."""

    def parse(self, dict_file):
        """Parse dict_file and return a list of words, skipping blanks/comments.

        Args:
            dict_file (file): The file object representing the dictionary.

        Returns:
            list: A list of words parsed from the file, excluding blanks/comments.
        """
        # Skip blank lines and comments (lines starting with '#')
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]