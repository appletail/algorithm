function solution(A,B){
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);

    return A.reduce((acc, _, idx) => acc + A[idx] * B[idx], 0);
}