
class Solution {
    public String mergeAlternately(String word1, String word2) {
        String res = "";
        int l1 = word1.length();
        int l2 = word2.length();
        int s1 = 0;
        int s2 =0;
        while (true){
            if(s1 <l1){
                res =res + word1.charAt(s1);
            }
            if(s2 <l2){
                res = res + word2.charAt(s2);
            }
            if (s1 >=l1 && s2>=l2){
                break;
            }
            s1++;
            s2++;
        }
        return res;
    }


    public static void main(String[] args) {



        
    }
}