import java.util.ArrayList;


class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        ArrayList<Integer> stack = new ArrayList<>();

        for(int asteroid: asteroids){
            if (stack.isEmpty()){stack.add(asteroid);
            }else{
                boolean explosion = false;
                while (stack.size()>0 && asteroid<0 && 0< stack.get(stack.size()-1)){
                    int s = stack.get(stack.size()-1) + asteroid;
                    if (s ==0){
                        explosion =true;
                        stack.remove(stack.size()-1);
                        break;
                    }else if (s >0){
                        explosion =true;
                        break;
                    }else{
                        stack.remove(stack.size()-1);
                    }
                }
                if (explosion ==false){
                    stack.add(asteroid);
                }
            }
        }
        int[] array = stack.stream().mapToInt(Integer::intValue).toArray();
        
        return array;
    }
}