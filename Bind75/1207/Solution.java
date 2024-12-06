import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        boolean flag = true;
        // step 1
        HashMap<Integer,Integer> cntMap = new HashMap<>();
        for(int num:arr){
            int v=1;
            if(cntMap.containsKey(num)){
                v = cntMap.get(num)+1;
            }
            cntMap.put(num, v);
        }

        // step 2:
        Set<Integer> set = new HashSet<>(cntMap.values());
        if(set.size()< cntMap.size()){flag=false;}
        return flag;
    }
}