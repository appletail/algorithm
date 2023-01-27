const person = (firstname, lastname) => {
    const obj = {
    first: firstname,
    last: lastname
    }
    return obj
}
const someone = person('김', '가네')
console.log(someone)