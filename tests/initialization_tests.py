from .test_utils import *
from copy import deepcopy

def initialize_parameters_zeros_test(target):
    layer_dims = [3, 2, 1]
    expected_output = {'W1': np.array([[0., 0., 0.],
                                       [0., 0., 0.]]),
                       'b1': np.array([[0.],
                                       [0.]]),
                       'W2': np.array([[0., 0.]]),
                       'b2': np.array([[0.]])}

    test_cases = [
        {
            "name": "datatype_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Datatype mismatch"
        },
        {
            "name": "shape_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong shape"
        },
        {
            "name": "equation_output_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong output"
        }
    ]

    multiple_test(test_cases, target)


def initialize_parameters_random_test(target):
    layer_dims = [3, 2, 1]
    expected_output = {'W1': np.array([[17.88628473, 4.36509851, 0.96497468],
                                       [-18.63492703, -2.77388203, -3.54758979]]),
                       'b1': np.array([[0.],
                                       [0.]]),
                       'W2': np.array([[-0.82741481, -6.27000677]]),
                       'b2': np.array([[0.]])}

    test_cases = [
        {
            "name": "datatype_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Datatype mismatch"
        },
        {
            "name": "shape_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong shape"
        },
        {
            "name": "equation_output_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong output"
        }
    ]

    multiple_test(test_cases, target)


def initialize_parameters_he_test(target):
    layer_dims = [3, 1, 2]
    expected_output = {'W1': np.array([[1.46040903, 0.3564088, 0.07878985]]),
                       'b1': np.array([[0.]]),
                       'W2': np.array([[-2.63537665], [-0.39228616]]),
                       'b2': np.array([[0.], [0.]])}

    test_cases = [
        {
            "name": "datatype_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Datatype mismatch"
        },
        {
            "name": "shape_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong shape"
        },
        {
            "name": "equation_output_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong output"
        }
    ]

    multiple_test(test_cases, target)

def multiple_test(test_cases, target):
    success = 0
    for test_case in test_cases:
        try:
            test_input = deepcopy(test_case['input'])
            target_answer = target(*test_input)
        except:
            print('\33[30m', "Error, interpreter failed when running test case with these inputs: " +
                  str(test_input))
            raise AssertionError("Unable to successfully run test case.".format(target.__name__))

        try:
            if test_case['name'] == "datatype_check":
                success += datatype_check(test_case['expected'],
                                      target_answer, test_case['error'])
            if test_case['name'] == "equation_output_check":
                success += equation_output_check(
                    test_case['expected'], target_answer, test_case['error'])
            if test_case['name'] == "shape_check":
                success += shape_check(test_case['expected'],
                                   target_answer, test_case['error'])
        except:
            print('\33[30m', "Error: " + test_case['error'])

    if success == len(test_cases):
        print("\033[92m All tests passed.")
    else:
        print('\033[92m', success, " Tests passed")
        print('\033[91m', len(test_cases) - success, " Tests failed")
        raise AssertionError(
            "Not all tests were passed for {}. Check your equations and avoid using global variables inside the function.".format(target.__name__))