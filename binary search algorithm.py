from typing import List, Union, Optional

def binary_search(arr: List[int], target: int, method: str = 'iterative') -> Union[int, None]:
    
    def binary_search_iterative(arr: List[int], target: int) -> Optional[int]:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return None

    def binary_search_recursive(arr: List[int], target: int, left: int, right: int) -> Optional[int]:
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
    
    if not arr:
        print("Error: The input array is empty.")
        return None
    
    if method == 'iterative':
        return binary_search_iterative(arr, target)
    elif method == 'recursive':
        return binary_search_recursive(arr, target, 0, len(arr) - 1)
    else:
        print("Error: Invalid method. Use 'iterative' or 'recursive'.")
        return None

if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search_target = 7

    index_iterative = binary_search(sorted_array, search_target, method='iterative')
    if index_iterative is not None:
        print(f"Element {search_target} found at index {index_iterative} using iterative method.")
    else:
        print(f"Element {search_target} not found using iterative method.")

    index_recursive = binary_search(sorted_array, search_target, method='recursive')
    if index_recursive is not None:
        print(f"Element {search_target} found at index {index_recursive} using recursive method.")
    else:
        print(f"Element {search_target} not found using recursive method.")
