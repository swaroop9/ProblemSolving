let arr = [5, 6, 7, 1, 2, 3, 4];

// let arr = [1, 2, 3, 4];


// // Simple way O(n)
// function findMin_1(arr) {
//     for (let i = 0; i < arr.length ; i++) {
//         if (arr[i] > arr[i+1]) {
//             console.log(arr[i+1]);
//             return arr[i+1];
//         }
//     }
//     return arr[0];
// }


// console.log(findMin_1(arr));


//Binary Search Q(log(n))
function findMin(arr) {
    let min = 0;
    let max = arr.length-1;

    while (min < max) {
        let mid = min + Math.floor((max-min)/2);
        // console.log(mid)
        if (arr[mid] < arr[max] ) {
            max = mid;
            
        } else {
            min = mid + 1;
        }
    }

    return arr[min]
  
}

console.log(findMin(arr));

[5, 6, 7, 1, 2, 3, 4]; mid,value = 3 , 1 , min, max = 0,3
[5,6,7,1] ; mid,value = 3 , 6 , min, max = 2,3
[7,1]  ; mid,value = 0 , 7 , min, max = 3,3