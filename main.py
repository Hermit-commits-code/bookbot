def main():
    with open('books/frankenstein.txt') as f:
        text = f.read()
        text = text.lower()
        return text

def count(text):
    return len(text.split())

def count_chars(text):
    occurrences = {}
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet character
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = 1
    return occurrences

def sort_char_count(char_count):
    return sorted(char_count.items(), key=lambda x: x[1], reverse=True)

def generate_report(word_count, sorted_char_count):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{word_count} words found in the document\n\n"
    for char, count in sorted_char_count:
        report += f"The '{char}' character was found {count} times\n"
    report += "--- End report ---"
    return report

text = main()
word_count = count(text)
char_count = count_chars(text)
sorted_char_count = sort_char_count(char_count)
report = generate_report(word_count, sorted_char_count)
print(report)