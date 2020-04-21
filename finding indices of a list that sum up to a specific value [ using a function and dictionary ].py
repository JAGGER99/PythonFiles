# summing two values from a list to get a specific value ..... using a function and a dictionary:

class Solution:
    
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target
    
    def twoSum(self):

        dict = {}               #initialize the dictionary

        for j in range(len(self.nums)):   
            for i in range(len(self.nums)):          #*****dont have to worry about duplicates because you cant assign the same key word to 2 differnt things!****
                    if self.nums[j] + self.nums[i] == self.target:
                        dict[self.nums[i]] = i
                        dict[self.nums[j]] = j
                     
        return(dict)



S = Solution([2,1,8,6,3,11], 9)     # creating an instant of the class Solution and assigning "nums" and "target"
S.twoSum()      
                     # calling twoSum() function
print("\n{value : index,...} ---->\n")    # added "\n" for space!
print(S.twoSum())                    # need to print the function to see what it returns!