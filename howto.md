# How to start

- Implement the ProblemInput class in problemInput.py file.
- Implement the Solution class in solution.py file.

# How to add an algorithm

- If you want to implement a new algorithm add it to algorithms or generic folder and implement the Algorithm class interface.
  - The generic folder is for generic algorithms that can be extended another time implementing few functions
  - The algorithms folder is for the algorithms that actually solve the problem
- The file and the class of the algorithm need to have the same name.
  
- In to the config.py file you need to add the algorithm name to the algorithms array.

# How to add a preprocess function

- Preprocess functions are written in the preprocess.py file so they can be added as functions there.
- In the config of your algorithm you add the attribute `prefunction : $function_name` 

# How to add a heuristic function

- Heuristic functions are written in the heuristcs.py file so they can be added as functions there.
- In the config of your algorithm you add the attribute `heuristic : $function_name`
- In your algorithm, use `self.call_heuristic(candidates, data)` to call the heuristic, where data a list of candidates.
- Keepn in mind that heuristics, unlikly preprocess functions, are not fully interchangeable

# What you shouldn't modify

- The main.py, config.py and any interface shouldn't be modified.
- Generic algorithms that you aren't developing.