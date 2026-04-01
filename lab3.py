# Exercise 1 --
def create_file(file_name, number_of_lines):
    with open(file_name, 'w') as file:
        for i in range(number_of_lines):
            file.write(f"Line no {i + 1}\n")

# Exercise 2
def count_lines(file_name: str) -> int:
    with open(file_name) as file:
        return len(file.readlines())

# Exercise 3
def lines(file_name: str) -> list[str]:
    with open(file_name) as file:
        return file.readlines()

# Exercise 4
def reversed_lines_file(input_file_name: str, output_file_name:str) -> None:
    file_lines = lines(input_file_name)
    with open(output_file_name, 'w') as output_file:
        for i in range(len(file_lines) - 1, -1, -1):
            output_file.write(file_lines[i])
        print(lines(output_file_name))
reversed_lines_file("test.txt", "test2.txt")

# Exercise 5
def words(file_name: str) -> list[str]:
    with open(file_name) as file:
        file_lines = file.readlines()
        words = [file_lines[i].split(" ") for i in range(len(file_lines))]
        ans = []
        for word in words:
            ans.extend(word)
        print(ans)

# Exercise 6
def reversed_words_order(input_file_name, output_file_name: str) -> None:
    file_lines = lines(input_file_name)
    print(file_lines)
    lines_by_word = [file_lines[i].rstrip("\n").split(' ') for i in range(len(file_lines))]
    for line in lines_by_word:
        line.reverse()

    reversed_lines = [" ".join(lines_by_word[i]) for i in range(len(file_lines))]
    with open(output_file_name, 'w') as output_file:
        for i in range(len(file_lines)):
            output_file.write(reversed_lines[i])
            output_file.write("\n")
    print(lines(output_file_name))

# Exercise 7
def words_counts(input_file_name):


