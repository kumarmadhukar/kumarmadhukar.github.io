# -*- coding: utf-8 -*-
"""L-08.ipynb

Automatically generated by Colab.

"""


"""##Towers of Hanoi"""

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
# Driver code
N = 3
# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')


"""## Checking trace of function calls"""

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    print(f"Calling ToH({n-1},{from_rod}, {aux_rod}, {to_rod})")
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    print(f"Calling ToH({n-1},{aux_rod}, {to_rod}, {from_rod})")
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
# Driver code
N = 3
# A, C, B are the name of rods
print(f"Calling ToH({N},'A', 'C', 'B')")
TowerOfHanoi(N, 'A', 'C', 'B')

"""##Longest common subsequence"""

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


lcs("AGGTAB", "GXTXAYB", 6, 7)


"""##Number of occurences of a specific character in a string"""

def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
string = input("Enter string:")
ch = input("Enter character to check:")
print("Count is:")
print(check(string,ch))

"""##Number of common characters in two strings"""

def count_common_chars(s1, s2):
    # Base case: if either string is empty, no common characters
    if not s1 or not s2:
        return 0

    # Check if the first character of s1 is in s2
    if s1[0] in s2:
        # Remove the character from s2 to avoid counting it again
        new_s2 = s2.replace(s1[0], '', 1)
        # Count this character and recurse with the rest of s1
        return 1 + count_common_chars(s1[1:], new_s2)
    else:
        # Skip this character and recurse with the rest of s1
        return count_common_chars(s1[1:], s2)

# Example usage
s1 = "apple"
s2 = "pineapple"
print(count_common_chars(s1, s2))