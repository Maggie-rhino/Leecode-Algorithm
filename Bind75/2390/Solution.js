/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    let res  =[];
    for(let i =0;i<s.length;i++){
        let c = s[i];
        if (c ==="*"){
            if(res.length>0){
                res.pop();            }
        }
        else{
            res.push(c)
        }
    }
    return res.join("");

};