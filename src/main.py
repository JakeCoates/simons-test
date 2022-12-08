import itertools
import math
import os


class problem_1():
    def __init__(self, path_to_file, items_to_sum, target):
        """_summary_

        :param path_to_file: path to the input file
        :param items_to_sum: amount of numbers you want to be in the combination
        :param target: the number you want the combination to achieve
        """
        self.path_to_file: str = path_to_file
        self.items_to_sum: int = items_to_sum
        self.target: int = target
        
    def load_data(self):
        """
        Take a text file and output the lines as an array of ints

        :return: return an array of ints based on the input text file
        """
        if not os.path.exists(self.path_to_file):
            raise Exception("file does not exist")

        if not self.path_to_file.lower().endswith('.txt'):
            raise Exception("invalid file type")

        with open(self.path_to_file) as f:
            return [int(line.strip()) for line in f.readlines()]

    def solve(self):
        """
        A function to solve problem 1, both a and b variants

        :return: return array that contains all products of possible combinations
        """
        data = self.load_data()
        combinations = [
            combinations
            for combinations in itertools.combinations(data, self.items_to_sum)
            if sum(combinations) == self.target
        ]
        return [math.prod(combination) for combination in combinations]


class problem_2():
    def __init__(self, path_to_file: str, range: bool = True):
        """_summary_

        :param path_to_file: path to the input file
        :param range: the basic option to complete either a range or
                    this not that check, defaults to True
        """
        self.path_to_file: str = path_to_file
        self.range: bool = range
        
    def load_data(self):
        """
        Take a text file and output the lines as an array of strings
        
        :return: return an array of strings based on the input text file
        """
        if not os.path.exists(self.path_to_file):
            raise Exception("file does not exist")

        if not self.path_to_file.lower().endswith('.txt'):
            raise Exception("invalid file type")

        with open(f"{self.path_to_file}") as f:
            return [line.strip() for line in f.readlines()]

    def prepare_data(self):
        """
        A function to prepare the data to be easier to read

        :return: return array that contains formatted data such as
                min, max, the character and the string to compare
        """
        data = self.load_data()
        split_data = [tuple(data.split(" ")) for data in data]
        prepared_data = [
            (list(map(int, a[0].split("-"))), a[1].replace(":", ""), a[2].replace(":", ""))
            for a in split_data
        ]
        return prepared_data

    def solve(self):
        """
        A function to solve problem 2, both a and b variants
        
        :return: array of all the matches and the data
        """
        prepared_data = self.prepare_data()
        matches = []
        for minmax, char, string in prepared_data:
            if self.range:
                count = string.count(char)
                if count >= minmax[0] and count <= minmax[1]:
                    matches.append((minmax, char, string))
            else:
                if (
                    len(string)
                    and minmax[1]
                    and string[minmax[0] - 1] == char
                    and string[minmax[1] - 1] != char
                ):
                    matches.append((minmax, char, string))
        return matches
