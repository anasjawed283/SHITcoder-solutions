def decode_pin(encoded_pin):
    decoded_pin = ""
    
    for pin in encoded_pin:
        # Calculate the cumulative sum of digits
        cumulative_sum = sum(int(digit) for digit in pin)
        while cumulative_sum >= 10:
            cumulative_sum = sum(int(digit) for digit in str(cumulative_sum))
        
        # Replace odd numbers with corresponding alphabets
        if cumulative_sum % 2 != 0:
            decoded_pin += chr(ord('a') + cumulative_sum - 1)
        else:
            decoded_pin += str(cumulative_sum)
    
    return decoded_pin

# Get input from the user
input_pins = input().split()

# Process the input and print the result
output_pin = decode_pin(input_pins)
print(output_pin)
