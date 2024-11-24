package JA.leecode75;

import java.util.Arrays;
import java.util.Stack;

public class AsteriodCollision {
    // Example 1:
    // Input: asteroids = [5,10,-5]
    // Output: [5,10]
    // Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
    
    // Example 2:
    // Input: asteroids = [8,-8]
    // Output: []
    // Explanation: The 8 and -8 collide exploding each other.
    
    // Example 3:
    // Input: asteroids = [10,2,-5]
    // Output: [10]
    // Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
    public int[] asteroidCollision(int[] asteroids) {
        // step 1: stack 1
        Stack<Integer> res = new Stack<>();
        // suppose the astroid rotate at right
        for(int a : asteroids){
            while(!res.isEmpty()){
                

            }
            if ( a <0 && !res.isEmpty() && Math.abs(a) >res.peek()){
                res.pop();
                res.push(a);
            } else if(a> 0 || res.isEmpty()){
                res.push(a);
            }            
        }
        int[] result = new int[res.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = res.pop();
        }
        return result;
    }


    public static void main(String[] args) {
        AsteriodCollision solution = new AsteriodCollision();
        int[] asteroids = {10,2,-5};
        int [] res = solution.asteroidCollision(asteroids);
        System.out.println(Arrays.toString(res));
    }
}
