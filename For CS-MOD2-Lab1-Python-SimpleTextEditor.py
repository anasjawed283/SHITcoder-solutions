class CustomStack:
    def __init__(self):
        self.text = ""
        self.operations = []

    def insert(self, value):
        self.text += value
        self.operations.append((1, value))

    def delete_chars(self, value):
        deleted_chars = self.text[-value:]
        self.text = self.text[:-value]
        self.operations.append((2, deleted_chars))

    def get_char(self, index):
        result = self.text[index - 1]
        print(result)
        self.operations.append((3, result))
        return result

    def undo(self):
        if self.operations:
            operation = self.operations.pop()
            if operation[0] == 1:
                self.text = self.text[:-len(operation[1])]
            elif operation[0] == 2:
                self.text += operation[1]

# Main program
def main():
    editor = CustomStack()
    user_input = input()
    commands = user_input.split(',')
    
    for command in commands:
        command, value = command.split()
        if command == "1":
            editor.insert(value)
        elif command == "2":
            editor.delete_chars(int(value))
        elif command == "3":
            editor.get_char(int(value))
        elif command == "4":
            editor.undo()

if __name__ == "__main__":
    main()
