class Solution:
    def isPalindrome1(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        is_palindrome = True

        while left < right and is_palindrome:
            left_alnum = s[left].isalnum()
            right_alnum = s[right].isalnum()
            
            if left_alnum and right_alnum:
                if s[left].lower() != s[right].lower():
                    is_palindrome = False
                else:
                    left += 1
                    right -= 1
            else:
                if not left_alnum:
                    left += 1
                if not right_alnum:
                    right -= 1
        
        return is_palindrome
    

    def isPalindrome2(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        is_palindrome = True

        while left < right and is_palindrome:
            # First find valid alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            
            if left < right:
                # Compare the two values
                if s[left].lower() != s[right].lower():
                    is_palindrome = False
                else:
                    left += 1
                    right -= 1

        return is_palindrome
    

    def isPalindrome3(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(s) - 1
        is_palindrome = True

        while left < right and is_palindrome:
            if s[left] != s[right]:
                is_palindrome = False
            left += 1
            right -= 1
        
        return is_palindrome

    # fastest solution, but uses MORE memory
    def isPalindrome4(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        
        return s == s[::-1]

# Time comparison
if __name__ == "__main__":
    from timeit import timeit

    string = "A man, a plan, a canal: Panama"
    sol =  Solution()
    print(sol.isPalindrome1(string))
    print(sol.isPalindrome2(string))
    print(sol.isPalindrome3(string))
    print(sol.isPalindrome4(string))

    SETUP_CODE = "from __main__ import Solution"

    for i in range(1, 4 + 1):
        TEST_CODE = f'''
string = "A man, a plan, a canal: Panama"
sol =  Solution()
sol.isPalindrome{i}(string)'''
        # timeit.repeat statement
        print(timeit(setup=SETUP_CODE,
                    stmt=TEST_CODE,
                    number=100000))

