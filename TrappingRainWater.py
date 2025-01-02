
class Solution:

    def trappingWater(arr):


        arr1 = arr[0:(arr.index(max(arr)))+1]
        arr2 = arr[(arr.index(max(arr))):len(arr)]
        arr2 = arr2[::-1]

    
        start  = arr1[0]
        counter = 1
        Water_b = 0
        
        while counter < len(arr1):
        
            if arr1[counter] <= start:
                Water_b = Water_b + (start - arr1[counter])
                counter += 1
            
            else:
                start = arr1[counter] 
                counter+=1
        start  = arr2[0]
        counter = 1
    
        while counter < len(arr2):
        
            if arr2[counter] <= start:
                Water_b = Water_b + (start - arr2[counter])
                counter += 1
            
            else:
                start = arr2[counter] 
                counter+=1
                
        return Water_b
