# Open a file in write mode with UTF-8 encoding
with open('output.txt', 'w', encoding='utf-8') as file:
    # String containing characters to be written
    text = "Hello, 你好, स्वागत हैं, বাংলা ভাষা"

    # Write the string to the file
    file.write(text)

print("Characters have been written to 'output.txt' using UTF-8 encoding.")