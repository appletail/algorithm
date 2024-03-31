function solution(my_string, letter) {
    return my_string.split('').reduce((acc, elem) => elem !== letter ? acc += elem : acc, '')
}