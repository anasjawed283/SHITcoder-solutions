def caesar_cipher(text, rotation):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + rotation) % 26 + start)
        else:
            result += char
    return result

# Get user input
original_message = input()

# Set the rotation value
rotation_value = 4

# Encrypt the message using the Caesar cipher
encrypted_message = caesar_cipher(original_message, rotation_value)

# Display the encrypted message
print(encrypted_message)
