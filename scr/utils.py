"""
Useful custom functions and class for the program
"""
import os

file = os.path.abspath(__file__)
current_dir = os.path.dirname(file)
BASE = os.path.dirname(current_dir)

class CheckDouble:
    """
    Class to check for duplicate entries in the file
    """
    def __init__(self):
        self.check = {}

    def add(self, element):
        """
        Adding element and keeping track of its count
        :param element:
        """
        if element not in self.check:
            self.check[element] = 1
        else:
            self.check[element] += 1

    def get_value(self, element):
        """
        Getting the current count of the element
        :param element:
        :return count of element:
        """
        return self.check.get(element, 0)

def readAndProcessFile(file_path: str):
    """
    Reading the content of the file and generating
    it on demand to reduce memory usage by not storing all the items
    :param file_path:
    :return:
    """
    seen = CheckDouble()
    with open(file_path, "r") as file:
        for line in file:
            integer = line.rstrip('\n')
            try:
                integer = int(integer)
            except ValueError:
                continue
            seen.add(integer)
            if seen.get_value(integer) == 1:
                yield integer

def selection_sort(arr, reverse=False):
    """
    Custom sorting function implementing the selection sort algorithm
    to sort the array of integers
    :param arr: List of integers to sort
    :param reverse: Boolean to indicate sorting order
    """
    for i in range(len(arr)-1):
        index = i
        for j in range(i+1, len(arr)):
            if reverse:
                if arr[j] > arr[index]:
                    index = j
            else:
                if arr[j] < arr[index]:
                    index = j
        if index != i:
            arr[i], arr[index] = arr[index], arr[i]

def writeFile(integers, output_file_path: str) -> None:
    """
    Writing the integers to the corresponding output file
    :param integers: List of integers to write
    :param output_file_path: Path to the output file
    """
    with open(output_file_path, "w") as f:
        for integer in integers:
            f.write(f"{integer}\n")

def runtime_log(runtime, file, mode="a"):
    """
    Logging the runtime of the process
    :param runtime: The runtime duration
    :param file: The file being processed
    :param mode: The mode for opening the log file
    """
    path = os.path.join(BASE, "Info.txt")
    with open(path, mode) as f:
        f.write(f"Memory Usage and runtime for file {file}:\nmem_Usage: #TODO\nRunTime: {runtime*1000} milli secs\n\n")
