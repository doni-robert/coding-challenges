class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        substring_list = s.split()
        new_string = " ".join(reversed(substring_list))

        return new_string