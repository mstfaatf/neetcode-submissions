class Solution:

    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1 # initialize left/right pointers

        while l < r: # as long as left is less than right (they dont cross)

            while l < r and not self.isalnumeric(s[l]): # same check and making sure its alphanumeric
                l += 1 # increment left pointer

            while r > l and not self.isalnumeric(s[r]): # same check and making sure its alphanumeric
                r -= 1 # decrement right pointer

            if s[l].lower() != s[r].lower(): # check if right and left not equal
                return False # if they not then false (one time not being equal completely stops it from being a palindrome)

            l, r = l+1, r-1 # increment / decrement the right and left pointers

        return True  # return true if able to pass checks as long as left less than right

    # function to if character is alphanumeric using asicc value ranges
    def isalnumeric(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("a") <= ord(c) <= ord("z") or 
                ord("0") <= ord(c) <= ord("9"))