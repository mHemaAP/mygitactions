'''
    This file has the test code for the functionality and actions written in the session6.py file . 

1.  This file contains 4 tests that validate a closure that takes a function and then check whether 
    the function passed has a docstring with more than 50 characters. 50 is stored as a 
    free variable

2.  2 tests are written to verify a closure that gives you the next Fibonacci number

3.  6 tests were written to validate the functionality of a closure that counts how many times a function 
    was called. These tests also include the cases which validate the functionality that can keep track 
    of how many times add/mul/div functions were called, and update a global dictionary 
    variable with the counts

4.  6 tests are written to verify the functionality of the above functions when we pass in different 
    dictionary variables to update different dictionaries 

5.  Once done, upload the code to Git Hub, run actions, and then proceed to answer S6 - Assignment QnA. 

6.  No readme or no docstring for each function, or no test cases (4, 2, 6, 6, >7 = 25 tests), then 0. 
    Write at least 7 test cases to check boundary conditions that might cause your code to fail. 
    Scores = Total Tests * 5 + Total Cleared Tests * 5

'''
import pytest
import random
import string
import os
import inspect
import re
import math
import time
import session6
from session6 import doc_string_check, fibonacci_closure, function_call_count_closure, function_call_count_closure_ext_dict, fn_called

'''
**********************************************************************************************************
                                        GENERIC TEST CASES
**********************************************************************************************************
'''

README_CONTENT_CHECK_FOR = [
    "fibonacci",
    "docstring",
    "closure",
    "count",
    "decorator"
    ]

def test_readme_exists():
    '''
    To check if ReadMe exists
    '''
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    '''
    To check if ReadMe includes important "Keywords"
    '''
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 250, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    '''
    To check if author has provided sufficient description
    '''
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    '''
    To check if author has used Markdown editing format or not
    '''
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    '''
    To check if function name contains any capital letter or camelcase
    '''
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


'''
**********************************************************************************************************
                                    DOCSTRING CHECKER TEST CASES
**********************************************************************************************************
'''

def test_doc_strings_without_docstring():
    '''
    Checks if function caches if no docstring present
    '''
    with pytest.raises(SyntaxError, match=r".*no docstring*"):
        def add_with_num_no_doc(a, b):
            return(a+b)
        fn_test = doc_string_check(add_with_num_no_doc)
        fn_test(2,3)

def test_doc_string_check():
    '''
    Check if number of words in docstring is less than 50
    '''
    with pytest.raises(SyntaxError, match=r".*at least 50 words*"):
        def add(a, b):
            '''
            This function adds two numbers and returns sum
            '''
            return (a+b)
        fn_test = doc_string_check(add)
        fn_test(4, 5)


def test_doc_string_no_exception():
    '''
    Check if number of words in docstring is less than 50
    '''
    def add_with_long_doc(a, b):
        '''
        This function adds two numbers and returns the sum. The purpose of this function
        is to demonstrate the addition of two integers or floats. The result of the 
        addition will be returned as the output of this function. This docstring is 
        deliberately made long to satisfy the requirement of having at least fifty words.
        '''
        return (a+b)
    fn_test = doc_string_check(add_with_long_doc)
    try:
        fn_test(1, 2)
    except:
        pytest.fail("test_doc_string_check raised exception unexpectedly")


def test_doc_strings_without_letter():
    '''
    Check docstring contains only numbers
    '''
    with pytest.raises(SyntaxError, match=r".*at least a few characters*"):
        def add_with_num_only_doc(a, b):
            '''
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            '''
            return(a+b)
        fn_test = doc_string_check(add_with_num_only_doc)
        fn_test(2,3)

# Define functions with various docstrings for testing
@doc_string_check
def function_with_sufficient_docstring():
    """
    This is a sample function with a sufficiently long docstring that has more than
    fifty words. The purpose of this docstring is to ensure that the function's
    behavior, inputs, outputs, and any other relevant information is well-documented.
    This ensures that the docstring meets the minimum word requirement set by the
    doc_string_check decorator.
    """
    pass

@doc_string_check
def function_with_insufficient_docstring():
    """
    Short docstring.
    """
    pass

@doc_string_check
def function_with_no_docstring():
    pass

@doc_string_check
def function_with_non_alphabetic_docstring():
    """
    123 456 789 123 456 789 123 456 789 123 456 789 123 456 789 123 456 789 123 456
    """
    pass

def test_function_with_sufficient_docstring():
    function_with_sufficient_docstring()

def test_function_with_insufficient_docstring():
    with pytest.raises(SyntaxError, match="Docstring must contain at least 50 words"):
        function_with_insufficient_docstring()

def test_function_with_no_docstring():
    with pytest.raises(SyntaxError, match="contains no docstring"):
        function_with_no_docstring()

def test_function_with_non_alphabetic_docstring():
    with pytest.raises(SyntaxError, match="Docstring must contain at least 50 words"):
        function_with_non_alphabetic_docstring()


'''
**********************************************************************************************************
                                FIBONACCI NUMBER GENERATOR TEST CASES
**********************************************************************************************************
'''

def test_fibonacci_closure():
    fib_gen = fibonacci_closure()
    assert fib_gen(2) == 1, "Fibonacci series function is not working"
    assert fib_gen(7) == 13, "Fibonacci series function is not working"
    assert fib_gen(10) == 55, "Fibonacci series function is not working"
    assert fib_gen(13) == 233, "Fibonacci series function is not working"
    assert fib_gen(15) == 610, "Fibonacci series function is not working"
    assert fib_gen(20) == 6765, "Fibonacci series function is not working"

def test_fibonacci_closure_large():
    fib_gen = fibonacci_closure()
    assert fib_gen(30) == 832040, "Fibonacci series function is not working"
    assert fib_gen(50) == 12586269025, "Fibonacci series function is not working"

def test_fibonacci_closure_negative():
    fib_gen = fibonacci_closure()
    with pytest.raises(ValueError, match="Fibonacci series is defined only for positive integers"):
        fib_gen(-1)

def test_fibonacci_closure_string():
    fib_gen = fibonacci_closure()
    with pytest.raises(ValueError, match="Fibonacci series is defined only for integers"):
        fib_gen("abc")


def test_fibonacci_closure_float():
    '''
    Checks if the fibonacci series handles negative numbers
    '''
    with pytest.raises(ValueError, match=r".*Fibonacci series is defined only for integers*"):
        fib_gen = fibonacci_closure()
        fib_gen(1.1)

def test_fibonacci_closure_complex():
    '''
    Checks if the fibonacci series handles complex numbers
    '''
    with pytest.raises(ValueError, match=r".*Fibonacci series is defined only for integers*"):
        fib_gen = fibonacci_closure()
        fib_gen(2+5j)

def test_fibonacci_closure_no_args():
    '''
    Checks if the fibonacci series handles call with no arguments
    '''
    fib_gen = fibonacci_closure()
    assert fib_gen() == 0, "Fibonacci series function is not working"

'''
**********************************************************************************************************
                                    FUNCTION CALLED COUNT TEST CASES
**********************************************************************************************************
'''
def test_fun_call_cnt_closure_add():
    '''
    Checks if the function called counting is working correctly
    '''
    @function_call_count_closure
    def add(a, b):
        return(a+b)
       
    return_val = add(2, 3)
    check_dictionary = {'add':1}
    assert check_dictionary == return_val, "Function counting not working properly"

def test_fun_call_cnt_closure_add_twice():
    '''
    Checks if the function called counting is working correctly
    '''
    @function_call_count_closure
    def add(a, b):
        return(a+b)
       
    _ = add(2, 3)
    return_val = add(2, 3)
    check_dictionary = {'add':3}
    assert check_dictionary == return_val, "Function counting not working properly"

def test_fun_call_cnt_closure_add_sub():
    '''
    Checks if the function called counting is working correctly by adding 
    a new function
    '''
    @function_call_count_closure
    def add(a, b):
        return(a+b)
    
    @function_call_count_closure
    def sub(a, b):
        return(a-b)
       
    _ = add(2, 3)
    return_val = sub(2, 3)
    
    check_dictionary = {'add':4, 'sub':1}
    assert check_dictionary == return_val, "Function counting not working properly"

def test_function_call_counter_multiple_functions():
    @function_call_count_closure
    def add(a, b):
        return a + b

    @function_call_count_closure
    def mul(a, b):
        return a * b

    add(1, 2)
    add(2, 3)
    mul(2, 3)
    assert fn_called['add'] == 6
    assert fn_called['mul'] == 1

def test_function_call_counter_reset():
    @function_call_count_closure
    def div(a, b):
        return a / b

    div(4, 2)
    div(6, 3)
    div(8, 4)
    assert fn_called['div'] == 3

def test_function_call_counter_boundary():
    @function_call_count_closure
    def boundary_test():
        pass

    for _ in range(1000):
        boundary_test()

    assert fn_called['boundary_test'] == 1000

def test_fun_call_cnt_closure_no_args():
    '''
    Checks if the function called counting is working correctly
    by calling a function without arguments
    '''
    @function_call_count_closure
    def random_fn():
        pass

    return_val = random_fn()
  
    check_dictionary = {'add':6, 'sub':1, 'mul': 1, 'div': 3, 'boundary_test': 1000, 'random_fn' : 1}
    print(return_val)
    print(check_dictionary)    
    assert check_dictionary == return_val, "Function counting not working properly"

def test_fun_call_cnt_closure_mem_clear():
    '''
    Checks if we can clear the count and restart the counting
    '''
    fn_called.clear()

    @function_call_count_closure
    def add(a, b):
        return(a+b)

    @function_call_count_closure
    def sub(a, b):
        return(a-b)

    _ = add(2, 3)
    return_val = sub(2, 3)
    
    check_dictionary = {'add':1, 'sub':1}
    assert check_dictionary == return_val, "Function counting not working properly"

'''
**********************************************************************************************************
                                FUNCTION CALLED COUNT TEST CASES - EXT DICT
**********************************************************************************************************
'''
ext_dict = {}

def test_fun_call_cnt_closure_ext_dict_add():
    '''
    Checks if the function called counting is working correctly
    '''
    global ext_dict
    @function_call_count_closure_ext_dict(ext_dict)
    def add(a, b):
        return(a+b)
       
    ext_dict = add(2, 3)
    check_dictionary = {'add':1}
    assert check_dictionary == ext_dict, "Function counting (external dict) not working properly"


def test_fun_call_cnt_closure_ext_dict_twice():
        '''
        Checks if the function called counting is working correctly
        '''
        global ext_dict
        @function_call_count_closure_ext_dict(ext_dict)
        def add(a, b):
            return(a+b)
        
        _ = add(2, 3)
        ext_dict = add(2, 3)
        check_dictionary = {'add':3}
        assert check_dictionary == ext_dict, "Function counting (external dict) not working properly"

def test_fun_call_cnt_closure_ext_dict_sub():
        '''
        Checks if the function called counting is working correctly by adding 
        a new function
        '''
        global ext_dict
        @function_call_count_closure_ext_dict(ext_dict)
        def add(a, b):
            return(a+b)
        
        @function_call_count_closure_ext_dict(ext_dict)
        def sub(a, b):
            return(a-b)
        
        _ = add(2, 3)
        ext_dict = sub(2, 3)
        
        check_dictionary = {'add':4, 'sub':1}
        assert check_dictionary == ext_dict, "Function counting (external dict) not working properly"

def test_fun_call_cnt_closure_ext_dict_no_ags():
        '''
        Checks if the function called counting is working correctly
        by calling a function without arguments
        '''
        global ext_dict
        @function_call_count_closure_ext_dict(ext_dict)
        def random_fn():
            pass

        return_val = random_fn()
        
        check_dictionary = {'add':4, 'sub':1, 'random_fn' : 1}
        assert check_dictionary == ext_dict, "Function counting (external dict) not working properly"


def test_fun_call_cnt_closure_ext_dict_mem_clear():
        '''
        Checks if we can clear the count and restart the counting
        '''
        global ext_dict
        ext_dict.clear()

        @function_call_count_closure_ext_dict(ext_dict)
        def add(a, b):
            return(a+b)

        @function_call_count_closure_ext_dict(ext_dict)
        def sub(a, b):
            return(a-b)

        _ = add(2, 3)
        ext_dict = sub(2, 3)
        
        check_dictionary = {'add':1, 'sub':1}
        assert check_dictionary == ext_dict, "Function counting not working properly"

def test_function_call_counter_ext_dict():
    custom_dict = {}

    @function_call_count_closure_ext_dict(custom_dict)
    def add(a, b):
        return a + b

    add(1, 2)
    add(2, 3)
    assert custom_dict['add'] == 2

def test_function_call_counter_ext_dict_multiple_functions():
    custom_dict = {}

    @function_call_count_closure_ext_dict(custom_dict)
    def add(a, b):
        return a + b

    @function_call_count_closure_ext_dict(custom_dict)
    def mul(a, b):
        return a * b

    add(1, 2)
    add(2, 3)
    mul(2, 3)
    assert custom_dict['add'] == 2
    assert custom_dict['mul'] == 1

def test_function_call_counter_ext_dict_separate_dicts():
    dict1 = {}
    dict2 = {}

    @function_call_count_closure_ext_dict(dict1)
    def add(a, b):
        return a + b

    @function_call_count_closure_ext_dict(dict2)
    def mul(a, b):
        return a * b

    add(1, 2)
    add(2, 3)
    mul(2, 3)
    assert dict1['add'] == 2
    assert 'mul' not in dict1
    assert dict2['mul'] == 1
    assert 'add' not in dict2

def test_function_call_counter_ext_dict_reset():
    custom_dict = {}

    @function_call_count_closure_ext_dict(custom_dict)
    def div(a, b):
        return a / b

    div(4, 2)
    div(6, 3)
    div(8, 4)
    assert custom_dict['div'] == 3

def test_function_call_counter_ext_dict_boundary():
    custom_dict = {}

    @function_call_count_closure_ext_dict(custom_dict)
    def boundary_test():
        pass

    for _ in range(1000):
        boundary_test()

    assert custom_dict['boundary_test'] == 1000


'''
**********************************************************************************************************
                                CHECK FOR BOUNDARY CONDITIONS
**********************************************************************************************************
'''

def test_function_call_counter_no_calls():
    custom_dict = {}

    @function_call_count_closure_ext_dict(custom_dict)
    def add(a, b):
        return a + b

    assert 'add' not in custom_dict

def test_function_call_counter_large_number():
    custom_dict = {}

    @function_call_count_closure_ext_dict(custom_dict)
    def add(a, b):
        return a + b

    for _ in range(10000):
        add(1, 2)

    assert custom_dict['add'] == 10000

def test_fibonacci_closure_large_boundary():
    fib_gen = fibonacci_closure()
    assert fib_gen(65) == 17167680177565, "Fibonacci series function is not working"

def test_fibonacci_closure_zero():
    fib_gen = fibonacci_closure()
    assert fib_gen(0) == 0, "Fibonacci series function is not working"

def test_doc_string_check_empty():
    with pytest.raises(SyntaxError, match="empty_docstring contains no docstring"):
        @doc_string_check
        def empty_docstring():
            pass
        empty_docstring()

def test_doc_string_check_non_string_docstring():
    with pytest.raises(SyntaxError, match="non_string_docstring contains no docstring"):
        @doc_string_check
        def non_string_docstring():
            12345
        non_string_docstring()

