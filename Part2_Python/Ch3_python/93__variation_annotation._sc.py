from typing import List


def numMatchingSubseq(S: str, words: List[str]) -> int:
    matched_count = 0

    for word in words:
        pos = 0
        for i in range(len(word)):
            found_pos = S[pos:].find(word[i])
            if found_pos < 0:  # if word[i] not in S[pos:] : return -1
                matched_count -= 1  # in below, finally plus 1 to matched_count
                break
            else:
                pos += found_pos + 1
        matched_count += 1

    return matched_count



S = 'abanananpple'
words = ['apple','banana']

print(numMatchingSubseq(S, words))