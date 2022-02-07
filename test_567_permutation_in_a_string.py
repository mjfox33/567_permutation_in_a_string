import code_567_permutation_in_a_string as c

def test_example_1():
    s = c.Solution()
    assert s.checkInclusion("ab", "eidbaooo") == True

def test_example_2():
    s = c.Solution()
    assert s.checkInclusion("ab", "eidboaoo") == False