from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base_dict = defaultdict(int)
        n1 = len(s1)
        for current_char in s1:
            base_dict[current_char] += 1

        n2 = len(s2)
        p1 = 0
        p2 = 0
        # i need a sliding window of size n1
        # character frequencies in the window need to match
        # character frequencies in n1
        char_set = defaultdict(int)
        total_char_count = 0
        while p1 < n2:
            current_char = s2[p1]
            char_set[current_char] += 1
            total_char_count += 1
            while char_set[current_char] > base_dict[current_char]:
                char_set[s2[p2]] -= 1
                total_char_count -= 1
                p2 += 1
            p1 += 1
            if n1 == total_char_count:
                return True
        return False
        
            