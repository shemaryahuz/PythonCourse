def process_string(s):
    print(f"Entering process_string with input: {s}")
    reversed_str = s[::-1]
    print(f"Exiting process_string with result: {reversed_str}")
    return reversed_str

def count_vowels(s):
    print(f"Entering count_vowels with input: {s}")
    vowels = "aeiou"
    vowel_count = sum(1 for char in s if char.lower() in vowels)  # Count vowels
    print(f"Exiting count_vowels with result: {vowel_count}")
    return vowel_count

def analyze_list(strings):
    print(f"Entering analyze_list with input: {strings}")
    result = []
    for i, s in enumerate(strings):
        print(f"Processing string at index {i}: {s}")
        reversed_str = process_string(s)
        vowel_count = count_vowels(reversed_str)
        result.append((i, reversed_str, vowel_count))
    print(f"Exiting analyze_list with result: {result}")
    return result

strings_list = ["apple", "banana", "cherry"]
print("Starting program execution...")
analysis_result = analyze_list(strings_list)

print("\nFinal Results:")
for index, reversed_str, vowel_count in analysis_result:
    print(f"Index: {index}, Reversed: {reversed_str}, Vowel Count: {vowel_count}")

"""
Output:
Starting program execution...
Entering analyze_list with input: ['apple', 'banana', 'cherry']
Processing string at index 0: apple
Entering process_string with input: apple
Exiting process_string with result: elppa
Entering count_vowels with input: elppa
Exiting count_vowels with result: 2
Processing string at index 1: banana
Entering process_string with input: banana
Exiting process_string with result: ananab
Entering count_vowels with input: ananab
Exiting count_vowels with result: 3
Processing string at index 2: cherry
Entering process_string with input: cherry
Exiting process_string with result: yrrehc
Entering count_vowels with input: yrrehc
Exiting count_vowels with result: 1
Exiting analyze_list with result: [(0, 'elppa', 2), (1, 'ananab', 3), (2, 'yrrehc', 1)]

Final Results:
Index: 0, Reversed: elppa, Vowel Count: 2
Index: 1, Reversed: ananab, Vowel Count: 3
Index: 2, Reversed: yrrehc, Vowel Count: 1
"""