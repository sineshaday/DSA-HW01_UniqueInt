#!/usr/bin/python3

"""
Entry point of the main program
"""
import time
import os
import sys
from utils import selection_sort, readAndProcessFile, writeFile, runtime_log, BASE

def main():
    if len(sys.argv) < 2:
        input_directory = os.path.join(BASE, "data/sample_data_input")
        output_directory = os.path.join(BASE, "data/sample_data_result")

        for file in os.listdir(input_directory):
            file_path = os.path.join(input_directory, file)
            if os.path.isfile(file_path):
                process_file(file_path, output_directory)
        print("DONE..")
    else:
        file_path = sys.argv[1]
        if os.path.isfile(file_path):
            output_directory = os.path.join(BASE, "data/argument_data_result")
            process_file(file_path, output_directory)
        else:
            print("Please provide a correct path to a file...")

def process_file(file_path, output_directory):
    start_time = time.time()
    file_name = os.path.basename(file_path)

    integers = list(readAndProcessFile(file_path))
    selection_sort(integers)
    output_file_path = os.path.join(output_directory, f"{file_name}_result.txt")
    writeFile(integers, output_file_path)

    end_time = time.time()
    run_time = end_time - start_time

    runtime_log(runtime=run_time, file=file_name)
    print(f"Memory Usage and runtime for file {file_name}:\nmem_Usage: #TODO\nRun_Time: {run_time * 1000:.2f} ms\n")

if __name__ == "__main__":
    main()
