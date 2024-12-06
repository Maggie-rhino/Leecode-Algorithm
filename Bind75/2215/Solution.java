import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>>  res =new ArrayList<>();
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        for(int num:nums1){set1.add(num);}
        for(int num:nums2){set2.add(num);}

        Set<Integer> left = new HashSet<>(set1);
        left.removeAll(set2);
        Set<Integer> right = new HashSet<>(set2);
        right.removeAll(set1);
        res.add(new ArrayList<>(left));
        res.add(new ArrayList<>(right));
        return res;
    }
}