def vowel_indices(word):
	# your code here
    ans = []
    
    for i, ch in enumerate(word):
        if ch in "aeuioyAEYUIO":
            ans.append(i+1)
            
    return ans