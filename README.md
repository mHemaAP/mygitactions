[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/z8haBqsC)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15331559&assignment_repo_type=AssignmentRepo)
# epai5session6

# ReadMe

## Assignment 6 Description

This project/assignment contains a collection of functions that serve various purposes such as checking the presence and length of docstrings, generating Fibonacci numbers, and counting function calls. Below is a detailed description of each function and its usage.

### Functions

1.  **doc_string_check**
    
    This function is a decorator that checks if the docstring of a given function contains at least 50 words. It raises a `SyntaxError` if the docstring is absent or does not meet the word count requirement.
    
    **Parameters:**
    
    -   `fn` (function): The function whose docstring is to be checked.
    
    **Usage:** 
    ```{python}
    @doc_string_check def some_function(): 
	    """A sufficiently long docstring with more than 50 words.""" 
	    pass
	```
    
2.  **fibonacci_closure**
    
    This function returns a closure that generates the next Fibonacci number based on a given index. The Fibonacci series is generated using the formula: Fn = Fn-1 + Fn-2.
    
    **Returns:**
    
    -   A closure that generates the next Fibonacci number.
    
    **Usage:** 
    ```{python}
    fib = fibonacci_closure() 
    print(fib(5)) 
    # Output: 5
    ```
    
3.  **function_call_count_closure**
    
    This function is a decorator that counts how many times a given function is called. It uses a global dictionary to keep track of the counts.
    
    **Parameters:**
    
    -   `fn` (function): The function whose call count is to be tracked.
    
    **Usage:** 
    ```{python}
    @function_call_count_closure 
    def some_function(): 
	    pass 
    
    some_function() 
    print(fn_called) 
    # Output: {'some_function': 1}
    ```
4.  **function_call_count_closure_ext_dict**
    
    This function is a decorator that counts how many times a given function is called. It uses an external dictionary to keep track of the counts.
    
    **Parameters:**
    
    -   `fn` (function): The function whose call count is to be tracked.
    
    **Usage:** call_dict = {}
    ```{python}
    @function_call_count_closure_ext_dict 
    def some_function(): 
	    pass
    
    some_function(call_dict) 
	print(call_dict) 
	# Output: {'some_function': 1}
    ```

### Dependencies

This project does not have any external dependencies. It is written in pure Python.

### License

This project is licensed under the MIT License.

Feel free to modify and use the code as per your requirements