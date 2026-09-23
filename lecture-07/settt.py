def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    len_long = 0
    len_seq = []

    all_L = [word for lst in words for word in lst]

    for i in range(len(all_L)):
        arrl = []
        for j in range(i,len(all_L)):
            if all_L[j] in arrl:
                break
            arrl.append(all_L[j])

            if len_long < len(arrl):
                len_long = len(arrl)
                len_seq = [] +[arrl]
                continue
            
            if len_long == len(arrl):
                len_seq.append(arrl)

    return len_long,len_seq
    pass

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])