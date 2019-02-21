from multiprocessing import Process, Queue
from problemInput import ProblemInput
from solution import Solution
import importlib
from config import Config


def instantiate_class(algorithm_name):
    module = importlib.import_module("algorithms.%s" % algorithm_name, algorithm_name.capitalize())
    class_ = getattr(module, algorithm_name.capitalize())
    return class_()


def solve(problem_input):

    #run the algorithms
    algorithms = Config.get["algorithms"]
    num_algorithms = len(algorithms)

    processes = []
    responses = []

    for i in range(num_algorithms - 1):
        algorithm_name = Config.get_algorithm_name(algorithms[i])
        response = Queue()
        solver = instantiate_class(algorithm_name)
        p = Process(target=solver.run, args=(response, problem_input))
        p.start()

        processes.append(p)
        responses.append(response)

    # we use this thread for the last one
    algorithm_name = Config.get_algorithm_name(algorithms[num_algorithms - 1])
    queue_best_response = Queue()
    solver = instantiate_class(algorithm_name)
    solver.run(queue_best_response, problem_input)

    # we make sure all the threads correctly exited
    for p in processes:
        p.join()

    # we pick the best one
    best_response = queue_best_response.get()
    for queue_response in responses:
        while(len(queue_response)):
            response = queue_response.get()
            if best_response.value() < response.value():
                best_response = response

    return best_response


def main():

    # load the config
    Config.load()

    # get input
    problem_input = ProblemInput(Config.get["input_file"])

    # solve the problem
    solution = solve(problem_input)

    # validate the solution
    solution.validate()

    # save the solution
    solution.save()

    # print the solution
    solution.render()

if __name__ == "__main__":
    main()