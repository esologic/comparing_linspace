import numpy
import timeit
import functools
import matplotlib.pyplot as plt
import inspect


def basic(start, end, num_steps):
    step_size = (end - start) / num_steps
    current = start
    out = [start]
    for _ in range(num_steps):
        current += step_size
        out.append(int(current))
    return out


def numpy_linspace(start, end, num_steps):
    return numpy.linspace(start, end, num=num_steps + 1)

if __name__ == "__main__":

    sta = 0
    sto = 255
    num_timeits = 5

    testing_functions = [basic, numpy_linspace]

    nums = []
    function_times = {}  # function : times

    for x in range(1, 10000, 100):

        nums.append(x)

        for f in testing_functions:
            timer = timeit.Timer(functools.partial(f, sta, sto, x))
            new_time = timer.timeit(num_timeits)

            try:
                function_times[f].append(new_time)
            except KeyError:
                function_times[f] = [new_time]

    plt.figure(figsize=(10, 10))
    plt.title("Comparing Linear Space Generation (Smaller is better)")
    plt.xlabel("Number of steps")
    plt.ylabel("Calculation time")

    for function in function_times.keys():
        plt.scatter(nums, function_times[function],  label=function.__name__)

    plt.legend(loc='lower right')

    plt.show()
