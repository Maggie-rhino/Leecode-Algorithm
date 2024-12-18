/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
    let stack = [];
    for(let i =0;i< asteroids.length;i++){
        if(stack.length ===0){
            stack.push(asteroids[i]);
        }else{
            let explosion =false;
            while(stack.length >0 && asteroids[i]<0 && 0<stack[stack.length-1]){
                let s = asteroids[i] + stack[stack.length-1];
                if(s ==0){
                    stack.pop();
                    explosion =true;
                    break
                }else if(s >0){
                    explosion = true;
                    break;
                }else{
                    stack.pop();
                    explosion =false;
                }
            }
            if(explosion ==false){
                stack.push(asteroids[i]);
            }
        }
    }
    return stack;
};