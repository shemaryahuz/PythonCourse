

# n = int(input())
#
# if n > 0 :
#     print("The if of the term")
#     is_sum = 1
#     for i in range(n + 1):
#         is_sum += i
#         print(f"Iteration number {i} the sum is {is_sum}")
#     print(is_sum)
#
# else:
#     print("The else of the term")

# def process_string(s):
#     print(f"Entering process_string with input: {s}")
#     reversed_str = s[::-1]
#     print(f"Exiting process_string with result: {reversed_str}")
#     return reversed_str
#
# def count_vowels(s):
#     print(f"Entering count_vowels with input: {s}")
#     vowels = "aeiou"
#     vowel_count = sum(1 for char in s if char.lower() in vowels)  # Count vowels
#     print(f"Exiting count_vowels with result: {vowel_count}")
#     return vowel_count
#
# def analyze_list(strings):
#     print(f"Entering analyze_list with input: {strings}")
#     result = []
#     for i, s in enumerate(strings):
#         print(f"Processing string at index {i}: {s}")
#         reversed_str = process_string(s)
#         vowel_count = count_vowels(reversed_str)
#         result.append((i, reversed_str, vowel_count))
#     print(f"Exiting analyze_list with result: {result}")
#     return result
#
# strings_list = ["apple", "banana", "cherry"]
# print("Starting program execution...")
# analysis_result = analyze_list(strings_list)
#
# print("\nFinal Results:")
# for index, reversed_str, vowel_count in analysis_result:
#     print(f"Index: {index}, Reversed: {reversed_str}, Vowel Count: {vowel_count}")

