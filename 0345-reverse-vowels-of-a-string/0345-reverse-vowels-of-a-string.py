class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_indices = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        length = len(list_indices) // 2
        s_list = list(s)
        for j in range(length):
            s_list[list_indices[j]], s_list[list_indices[-j - 1]] = s_list[list_indices[-j - 1]], s_list[list_indices[j]]
        return ''.join(s_list)


        