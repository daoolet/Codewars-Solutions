def merge_arrays(arr1, arr2):
    return sorted(dict.fromkeys(arr1 + arr2))
    #return sorted(set(arr1 + arr2)) also works