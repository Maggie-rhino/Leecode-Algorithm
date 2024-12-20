package Bind75

import java.util.Stack;

.394;

public class Solution {
    public String decodeString(String s) {
        Stack<String> strStack = new Stack<>();
        Stack<Integer> cntStack = new Stack<>();
        StringBuilder curStr = new StringBuilder();
        int curNum =0;
        for(Character c : s.toCharArray()){
            if(Character.isDigit(c)){
                curNum = curNum*10+(c-'0');
            }else if(c =='['){
                // start the decompression
                strStack.push(curStr.toString());
                cntStack.push(curNum);
                curStr =new StringBuilder();
                curNum =0;
            } else if (c ==']'){
                String preStr = strStack.pop();
                int repeatCnt = cntStack.pop();
                
            }
        }

    }
}
