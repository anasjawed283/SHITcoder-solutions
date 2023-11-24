def check_good_password(passwords):
    passwords.sort()

    for i in range(len(passwords) - 1):
        if passwords[i + 1].startswith(passwords[i]):
            return f"BAD PASSWORD"

    return "GOOD PASSWORD"

# User input
passwords = input().split()

# Call the function to check if it's a good password
result = check_good_password(passwords)

# Output
print(result)
