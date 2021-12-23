let arr = [1,-2, 4, 5, 5]

let largest = Number.MIN_SAFE_INTEGER;
let smallest = Number.MAX_SAFE_INTEGER;

console.log(largest,smallest)

for (ele of arr) {
    if (ele > largest) {
        largest = ele;
    } else if (ele < smallest) {
        smallest = ele;
    }
}

console.log(largest,smallest)