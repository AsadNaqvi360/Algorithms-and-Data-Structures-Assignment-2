def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Diving arr into halfs
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # REcursion for the halfs
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # TO MERge the sorted halfs
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index = right_index = 0
    
    # To merge the two arrays together
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Add whatever is remaining from left & from right
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Example:
array_to_sort = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
sorted_array = merge_sort(array_to_sort)
print("The Sorted Array:", sorted_array)
