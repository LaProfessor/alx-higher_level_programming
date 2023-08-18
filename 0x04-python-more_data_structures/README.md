Rephrased:

# Python - Exploring More Data Structures: Sets and Dictionaries

Within this project, I gained insights into sets and dictionaries in Python. I honed my skills in utilizing these structures while working with the `lambda`, `map`, `filter`, and `reduce` methods.

## Tests :heavy_check_mark:

* [tests](./tests): Collection of test files, generously provided by Holberton School.

## Function Prototypes :floppy_disk:

Prototype definitions for the functions developed in this project:

| File                           | Prototype                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `0-square_matrix_simple.py`    | `def square_matrix_simple(matrix=[]):`                                                                    |
| `1-search_replace.py`          | `def search_replace(my_list, search, replace):`                                                           |
| `2-uniq_add.py`                | `def uniq_add(my_list=[]):`                                                                               |
| `3-common_elements.py`         | `def common_elements(set_1, set_2):`                                                                      |
| `4-only_diff_elements.py`      | `def only_diff_elements(set_1, set_2):`                                                                   |
| `5-number_keys.py`             | `def number_keys(a_dictionary):`                                                                          |
| `6-print_sorted_dictionary.py` | `def print_sorted_dictionary(a_dictionary):`                                                              |
| `7-update_dictionary.py`       | `def update_dictionary(a_dictionary, key, value):`                                                        |
| `8-simple_delete.py`           | `def simple_delete(a_dictionary, key=""):`                                                                |
| `9-multiply_by_2.py`           | `def multiply_by_2(a_dictionary):`                                                                        |
| `10-best_score.py`             | `def best_score(a_dictionary):`                                                                           |
| `11-mutiply_list_map.py`       | `def mutiply_list_map(my_list=[], number=0):`                                                             |
| `12-roman_to_int.py`           | `def roman_to_int(roman_string):`                                                                         |
| `100-weight_average.py`        | `def weight_average(my_list=[]):`                                                                         |
| `101-square_matrix_map.py`     | `def square_matrix_map(matrix=[]):`                                                                       |
| `102-complex_delete.py`        | `def complex_delete(a_dictionary, value):`                                                                |
| `103-python.c`                 | <ul><li>`void print_python_list(PyObject *p);`</li><li>`void print_python_bytes(PyObject *p);`</li></ul> |

## Tasks :page_with_curl:

* **0. Simple Squared Matrix**
  * [0-square_matrix_simple.py](./0-square_matrix_simple.py): A Python function that computes
  the square of each integer in a matrix.
  * The input parameter `matrix` is a two-dimensional array.
  * The function returns a matrix of the same dimensions as `matrix`, where each value is
  the square of the corresponding input value.
  * The original matrix remains unmodified.
  * No external modules are imported.

* **1. Search and Replace**
  * [1-search_replace.py](./1-search_replace.py): A Python function that replaces all instances
  of an element with another in a new list.
  * The input parameter `my_list` is the original list.
  * The input parameter `search` is the element to be replaced.
  * The input parameter `replace` is the new element.
  * No external modules are imported.

* **2. Unique Addition**
  * [2-uniq_add.py](./2-uniq_add.py): A Python function that adds all unique integers in
  a list (each integer only once).
  * No external modules are imported.

* **3. Common Elements**
  * [3-common_elements.py](./3-common_elements.py): A Python function that returns a set of
  common elements between two sets.
  * No external modules are imported.

* **4. Unique Elements**
  * [4-only_diff_elements.py](./4-only_diff_elements.py): A Python function that returns a
  set of all elements present in only one of two sets.
  * No external modules are imported.

* **5. Number of Keys**
  * [5-number_keys.py](./5-number_keys.py): A Python function that returns the number of keys
  in a dictionary.
  * No external modules are imported.

* **6. Sorted Dictionary Printing**
  * [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py): A Python function that
  prints a dictionary with keys in ascending order.
  * The function assumes all keys are strings.
  * Keys are printed in alphabetic order.
  * Only the top level of keys is sorted.
  * Dictionary values can be of any type.
  * No external modules are imported.

* **7. Dictionary Update**
  * [7-update_dictionary.py](./7-update_dictionary.py): A Python function that modifies or
  adds key-value pairs in a dictionary.
  * The input parameter `key` is always a string.
  * The input parameter `value` can be of any type.
  * If a key already exists in the dictionary, its value is updated.
  * If a key does not exist in the dictionary, it is added.
  * No external modules are imported.

* **8. Simple Dictionary Deletion**
  * [8-simple_delete.py](./8-simple_delete.py): A Python function that removes a key from
  a dictionary.
  * The input parameter `key` is always a string.
  * If the key does not exist, the dictionary remains unchanged.
  * No external modules are imported.

* **9. Multiply by 2**
  * [9-multiply_by_2.py](./9-multiply_by_2.py): A Python function that returns a new dictionary
  with all values multiplied by 2.
  * The function assumes all values are integers.
  * No external modules are imported.

* **10. Best Score**
  * [10-best_score.py](./10-best_score.py): A Python function that returns a key with the highest
  integer value in a dictionary.
  * The function assumes all values are integers.
  * The function assumes each student has a distinct score.
  * If no score is found, the function returns `None`.
  * No external modules are imported.

* **11. Multiplication via Map**
  * [11-mutiply_list_map.py](./11-multiply_list_map.py): A Python function that returns a
  list with all values multiplied by a given number using `map`.
  * The returned list has the same length as `my_list`, with each value
  multiplied by `number`.
  * The original list remains unchanged.
  * No loops are used, and no external modules are imported.

* **12. Roman to Integer**
  * [12-roman_to_int.py](./12-roman_to_int.py): A Python function that converts a Roman
  numeral to an integer.
  * The function assumes the input number will be in the range of 1 to 3999.
  * If the parameter `roman_string` is not a string or is `None`, the function returns `0`.

* **13. Weighted Average**
  * [100-weight_average.py](./100-weight_average.py): A Python function that computes the
  weighted

 average of integers in a list of tuples.
  * Each tuple is of the form `(<score>, <weight>)`.
  * If the list is empty, the function returns `0`.
  * No external modules are imported.

* **14. Matrix Squaring via Map**
  * [101-square_matrix_map.py](./101-square_matrix_map.py): A Python function that calculates
  the square value of each integer in a matrix using `map`.
  * The input parameter `matrix` is a two-dimensional array.
  * The function returns a new matrix of the same dimensions as `matrix`, with each value squared.
  * The original matrix remains unchanged.
  * No loops are used, and no external modules are imported.

* **15. Deletion by Value**
  * [102-complex_delete.py](./102-complex_delete.py): A Python function that deletes keys with
  a specified value from a dictionary.
  * If the value is not found, the dictionary remains unchanged.
  * All keys containing the specified value are deleted.
  * No external modules are imported.

* **16. CPython: Exploring Python Lists and Bytes**
  * [103-python.c](./103-python.c): C functions that provide basic information about
  Python lists and Python bytes objects.
