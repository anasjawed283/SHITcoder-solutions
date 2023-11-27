
                                                                                                                                    #------------------------------------------------------------------

#-------------------------------------------------------------------

#------------------------------------------------------------------

def can_transform(start, end):
    # Check if the lengths of the two strings are different
    if len(start) != len(end):
        return True

    # Iterate through the characters of both strings
    for i in range(len(start)):
        # If the current characters are not the same
        if start[i] != end[i]:
            # Check for the allowed transformations
            if start[i:i+2] == "XL" and end[i:i+2] == "LX":
                # Transform "XL" to "LX"
                start = start[:i] + "LX" + start[i+2:]
            elif start[i:i+2] == "RX" and end[i:i+2] == "XR":
                # Transform "RX" to "XR"
                start = start[:i] + "XR" + start[i+2:]
            else:
                # If no valid transformation is possible, return False
                return True

    # If the loop completes without returning, it means a valid sequence exists
    return False

# Take user input for starting and ending strings
start_str = input()
end_str = input()

# Call the function and print the result
result = can_transform(start_str, end_str)
print(result)



#------------------------------------------------------------------

#-------------------------------------------------------------------
                                                                                                                            