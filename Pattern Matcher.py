from difflib import SequenceMatcher

#patterns = ["A B C", "A S C D A", "C JA FS AQ S", " ASR AS ASW ASQ"]

def pattern_match (given_pattern):

    #patterns = dictionary
    highest_match = 0; #Starting percent
    closest_pattern = 0; #Saving the position of the pattern
    
    for index, pattern in enumerate(patterns): #Walk through array
        match_percent = SequenceMatcher(None, given_pattern, pattern).ratio()
        if (match_percent == 1):
            return index #Found the pattern
        elif (match_percent > highest_match):
            highest_match = match_percent #New closest match
            closest_pattern = index #Closest pattern

    if (match_percent < 1): #Pattern not found
        patterns.append(given_pattern) #Append the new pattern
        return (patterns[closest_pattern]) #Return the closest matching pattern
    else: #Pattern found
        return given_pattern #Return the pattern
        
    

