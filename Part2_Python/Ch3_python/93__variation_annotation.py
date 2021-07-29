

'''
문자열에 매칭된 서브 시퀀스의 개수를 구하는 코드
'''

from typing import List


def numMatchingSubseq(S: str, words: List[str]) -> int:
    matched_count = 0

    for word in words:
        pos = 0
        for i in range(len(word)):
            # Find matching position for each character
            found_pos = S[pos:].find(word[i])
            if found_pos < 0:
                matched_count -= 1
                break
            else: # If found, take step position forward.
                pos += found_pos + 1
        matched_count += 1
    return matched_count


S = 'apllebananancookie'
words = ['apple', 'cookie', 'potato']

print(numMatchingSubseq(S, words))
