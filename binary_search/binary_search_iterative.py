"""
Binary search implementation - Iterative Implementation
2020918
ProjectFullStack
"""


def binary_search(sorted_list, search_key):
    left_limit = 0
    right_limit = len(sorted_list) - 1
    middle_index = 0

    while left_limit <= right_limit:
        middle_index = (left_limit + right_limit) // 2

        if sorted_list[middle_index] < search_key:
            left_limit= middle_index + 1
        elif sorted_list[middle_index] > search_key:
            right_limit = middle_index - 1
        else:
            return middle_index
    return -1


# Test Case 1 - Search key exists in search list at index 3
search_list = [5, 23, 37, 42, 53, 61, 73, 85, 96, 101, 112, 126, 131, 142]
search_key = 42
print(f"Test 1: Searching for {search_key} in {search_list}")
result = binary_search(search_list, search_key)
print(f"Result: {result}")

# Test Case 2 - Search key does not exist in search list
search_list = [5, 23, 37, 42, 53, 61, 73, 85, 96, 101, 112, 126, 131, 142]
search_key = 49
print(f"Test 2: Searching for {search_key} in {search_list}")
result = binary_search(search_list, search_key)
print(f"Result: {result}")

# Test Case 3 - Empty list
search_list = []
search_key = 49
print(f"Test 3: Searching for {search_key} in {search_list}")
result = binary_search(search_list, search_key)
print(f"Result: {result}")

# Test Case 4 - List of one element, search key exists
search_list = [49]
search_key = 49
print(f"Test 4: Searching for {search_key} in {search_list}")
result = binary_search(search_list, search_key)
print(f"Result: {result}")

# Test Case 5 - List of one element, search key does not exist
search_list = [53]
search_key = 49
print(f"Test 5: Searching for {search_key} in {search_list}")
result = binary_search(search_list, search_key)
print(f"Result: {result}")