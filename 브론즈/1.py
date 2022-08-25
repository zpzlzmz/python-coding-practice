def twoSum(nums: list[int], target: int) -> list[int]:
     for i in range(len(nums)):
         for j in range(len(nums)-1):
            if(nums[i]+nums[j]) == target:
                print("[",i,",",j,"]",sep="")
                return


twoSum([2,7,11,15],9)
