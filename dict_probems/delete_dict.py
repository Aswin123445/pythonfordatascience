max_valu=5

#outer loop
for x in range(max_valu):
    #inner loop
    y=max_valu-x
    while(y>=1):
        print(y,end=' ')
        y-=1
    print()

def st(strin):
    count=len([x for x in strin if x in ('a','e','i','o','u')])
    return count


print(st('aswin'))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      max_length = 0
      left = 0
      right = 0
      char_index = {}

      while right < len(s):
          char = s[right]
          if char in char_index and char_index[char] >= left:
              left = char_index[char] + 1
          char_index[char] = right
          max_length = max(max_length, right - left + 1)  

          right += 1
      print(char_index)
      return max_length
cl=Solution()
print(cl.lengthOfLongestSubstring('123abc123'))

nums=[1,2,3,4,4,5,3,4,6,]
val=4
nums= list(filter(lambda x:  x != val,list(nums)))
print(nums)




