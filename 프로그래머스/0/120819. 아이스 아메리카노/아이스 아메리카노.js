function solution(money) {
    const canBuy = ~~(money / 5500)
    var answer = [canBuy, money - (5500 * canBuy)];
    return answer;
}