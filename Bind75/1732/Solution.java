
class Solution {
    public int largestAltitude(int[] gain) {
        int highestAltitude =0;
        int current =0;
        for(int i =0;i<gain.length;i++){
            current +=gain[i];
            if(current>highestAltitude){
                highestAltitude =current;
            }
        }
        return highestAltitude;
    }
}