my_list = [7,4,8,2,5,9,1,0]
sorted_list = []
#my version with no copy list coz who cares about that right ? 

def sorting(my_list,sorted_list):
    if not my_list:
        return sorted_list
    else:
        sorted_list.append(min(my_list))
        my_list.remove(min(my_list))

        return sorting(my_list,sorted_list)

print(sorting(my_list,sorted_list))


#gemini version with safe list copying very cool
def sorting(src_list, result_list):
    # Base case: if source is empty, we are done!
    if not src_list:
        return result_list
    
    # Find the smallest
    smallest = min(src_list)
    result_list.append(smallest)
    
    # Create a copy of the list WITHOUT the smallest element
    # We don't need [1:] because we are actually removing an element
    remaining_list = src_list.copy()
    remaining_list.remove(smallest)
    
    return sorting(remaining_list, result_list)

print(sorting(my_list, sorted_list))

    