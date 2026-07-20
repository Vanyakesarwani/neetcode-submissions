from typing import List


def sort_words(words: List[str]) -> List[str]:
    for i in range(len(words)):
        for j in range(0,len(words)-i-1):
            w1 = words[j]
            w2 = words[j+1]
            if w1 > w2:
                words[j], words[j+1] = words[j+1],words[j]
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        for j in range(0,len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1],numbers[j]
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    for i in range(len(numbers)):
        for j in range(0,len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1],numbers[j]
    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))