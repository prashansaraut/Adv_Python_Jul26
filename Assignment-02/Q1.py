
def count_characters(text):
    frequency = {}

    text = text.lower()

    for ch in text:
        if ch.isalpha():
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

    sorted_freq = {}
    for key in sorted(frequency.keys()):
        sorted_freq[key] = frequency[key]

    return sorted_freq

text = input("Enter a string:")
print(count_characters(text))