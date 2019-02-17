import json
from multiprocessing import Process, Queue
from problemInput import ProblemInput
from solution import Solution
import importlib


def load_config():
    with open('../config.json') as f:
        return json.load(f)

def instantiate_class(algorithm_name):
    module = importlib.import_module("algorithms.%s" % algorithm_name, algorithm_name.capitalize())
    class_ = getattr(module, algorithm_name.capitalize())
    return class_()


def solve(problem_input):
    global config

    #run the algorithms
    num_algorithms = len(config["algorithms"])

    processes = []
    responses = []

    for i in range(num_algorithms - 1):
        response = Queue()
        solver = instantiate_class(config["algorithms"][i])
        p = Process(target=solver.run, args=(response, problem_input))
        p.start()

        processes.append(p)
        responses.append(response)

    # we use this thread for the last one
    queue_best_response = Queue()
    solver = instantiate_class(config["algorithms"][num_algorithms - 1])
    solver.run(queue_best_response, problem_input)
    
    # we pick the best one
    best_response = queue_best_response.get()
    for queue_response in responses:
        response = queue_response.get()
        if best_response.value() < response.value():
            best_response = response

    # we make sure all the threads correctly exited
    for p in processes:
        p.join()

    return best_response


def main():

    # load the config
    global config
    config = load_config()

    # get input
    problem_input = ProblemInput(config["input_file"])

    # solve the problem
    solution = solve(problem_input)

    # validate the solution
    solution.validate()

    # save the solution
    solution.save()

    # print the solution
    solution.render()
    
main()