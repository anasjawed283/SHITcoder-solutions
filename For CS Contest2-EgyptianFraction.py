def egyptian_fraction(numerator, denominator):
    result = []
    
    while numerator > 0:
        unit_fraction_denominator = -(-denominator // numerator)  # Equivalent to ceil(denominator / numerator)
        result.append(unit_fraction_denominator)
        numerator = numerator * unit_fraction_denominator - denominator
        denominator = denominator * unit_fraction_denominator

    return result

# User input
numerator = int(input())
denominator = int(input())

# Call the function to get the result
result = egyptian_fraction(numerator, denominator)

# Output
# print(" ".join(map(str, result)))
print("\n".join(map(str, result)))