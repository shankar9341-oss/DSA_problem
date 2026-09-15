class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        left = 0
        for right in range(1,len(arr)):
            if arr[left] != arr[right]:
                left += 1
                arr[left] = arr[right]
        return left + 1