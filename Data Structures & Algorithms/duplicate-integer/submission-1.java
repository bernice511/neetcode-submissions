class Solution {
    public boolean hasDuplicate(int[] nums) {
     HashMap<Integer, Integer> duplicates = new HashMap();

     for(int num: nums){
        if(duplicates.containsKey(num)){
            return true;
        }
        else{
            duplicates.put(num, 1);
        }
     }
     return false;   
    }
}