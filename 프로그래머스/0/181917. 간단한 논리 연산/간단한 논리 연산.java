class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        return n(v(x1, x2), v(x3, x4));
    }
    
    public boolean v(boolean x, boolean y) {
        if (x || y) return true;
        return false;
    }
    
    public boolean n(boolean x, boolean y) {
        if (x && y) return true;
        return false;
    }
}