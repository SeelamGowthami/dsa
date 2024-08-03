def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left=0
        for right in range(0,len(nums)):
            if (nums[right])%2==0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums