#!/usr/bin/python3

import os

def automate_python():

    for i in range(20):

        os.system("./../Python/PythonHeterodyning.py >> ../output/PythonHeterodyningBenchMark.txt ")

    clean_benchmark_output_python()


def clean_benchmark_output_python():

    lines = list()

    with open("../output/PythonHeterodyningBenchMark.txt", "r") as f:

        lines = f.readlines()


    with open("../output/CleanPythonHeterodyningBenchMark.txt", "w") as f:

        for i in lines:

            if "Elapsed" in i:

                f.write(i)

def automate_c_unthreaded():


    for i in range(20):

        os.system("cd ../C/; make clean; make; make run >> ../output/CHeterodyningBenchmarkUnthreaded.txt")
        #os.system("pwd")

    clean_benchmark_output_c_unthreaded()


def clean_benchmark_output_c_unthreaded():

    lines = list()

    with open("../output/CHeterodyningBenchmarkUnthreaded.txt", "r") as f:

        lines = f.readlines()

    with open("../output/CleanCHeterodyningBenchmarkUnthreaded.txt", "w") as f:

        for i in lines:

            if "Time" in i:

                f.write(i)


def automate_c_threaded():

    for i in range(20):

        os.system("cd ../C/; make clean; make threaded; make run_threaded >> ../output/CHeterodyningBenchmarkThreaded_32_threads.txt")

    clean_benchmark_output_c_threaded()


def clean_benchmark_output_c_threaded():

    lines = list()

    with open("../output/CHeterodyningBenchmarkThreaded_32_threads.txt", "r") as f:

        lines = f.readlines()

    with open("../output/CleanCHeterodyningBenchmarkThreaded_32_threads.txt", "w") as f:

        for i in lines:

            if "Time" in i:

                f.write(i)


def automate_c_optimazation():

    for i in range(20):

        os.system("cd ../C/; make clean; make; make run >> ../output/CHeterodyningBenchmark_fp16_O1_funroll.txt")


if __name__ == "__main__":

    #os.system()
    #automate_python()
    #automate_c_unthreaded()
    #automate_c_threaded()
    automate_c_optimazation()
