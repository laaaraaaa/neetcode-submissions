class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1

        while left <= right:

            if not s[left].isalnum():
                left = left + 1
            #the above code checks if there is any blank space present and if there is a blank space then it skips the blank space

            elif not s[right].isalnum():
                right = right - 1
            # does the same function but for the right part

            elif s[left].lower() != s[right].lower():
                return False
            
            else:
                left += 1
                right -= 1
            #if both left and right are same then move forward
            
        return True


            

            
        