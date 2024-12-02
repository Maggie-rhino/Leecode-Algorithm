

var a  =function(word1,word2){
    let res ="";
    let l1 = word1.length;
    let l2 = word2.length;
    let s1 =0;
    let s2=0;
    while (true){
        if(s1 <l1){
            res +=word1[s1];
        }
        if(s2<l2){
            res +=word2[s2];
        }
        if(s1 >=l1 && s2>=l2){break;}
        s1++;
        s2++;
    }
    return res;
}