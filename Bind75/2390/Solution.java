import java.util.ArrayList;

class Solution {
    public String removeStars(String s) {
        ArrayList<Character> res = new ArrayList<>();
        
        for(int i =0;i<s.length();i++){
            char c = s.charAt(i);
            if (c =='*'){
                if(!res.isEmpty()){
                    res.remove(res.size()-1);
                }
            }else{
                res.add(c);
            }
        }
        
        StringBuilder r = new StringBuilder();
        for(char c :res){
            r.append(c);
        }
        return r.toString();
    }
}