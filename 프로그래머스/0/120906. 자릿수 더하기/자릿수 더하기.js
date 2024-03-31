function solution(n) {
    return n.toString().split('').reduce((acc, num) => acc + Number(num), 0);
}