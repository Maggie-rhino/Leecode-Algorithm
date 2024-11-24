package JA.leecode75;

import java.util.Stack;

public class RemovingStarsFromString {
    // Example 1:
    // Input: s = "leet**cod*e"
    // Output: "lecoe"
    // Explanation: Performing the removals from left to right:
    // - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
    // - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
    // - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
    // There are no more stars, so we return "lecoe".
    
    // Example 2:
    // Input: s = "erase*****"
    // Output: ""
    // Explanation: The entire string is removed, so we return an empty string.

    // Constraints:
    // 1 <= s.length <= 105
    // s consists of lowercase English letters and stars *.
    // The operation above can be performed on s.

    public String removeStars(String s) {
        StringBuilder res = new StringBuilder() ;
        Stack<Character> reStack = new Stack<Character>();
        for(int i =0;i< s.length();i++){
            reStack.push(s.charAt(i));
        }

        int startFlag = 0;
        while(!reStack.isEmpty()){
            if(reStack.peek() =='*'){
                startFlag +=1;
                reStack.pop();
            }else if (
                reStack.peek() !='*' && startFlag >0
            ){
                reStack.pop();
                startFlag -=1;
            }else{
                res.insert(0, reStack.pop());
            }
        
        }
        return res.toString();
    }

    public static void main(String[] args) {
        RemovingStarsFromString solution = new RemovingStarsFromString();
        String s = "erase*****";
        System.out.println(solution.removeStars(s));
    }
}
