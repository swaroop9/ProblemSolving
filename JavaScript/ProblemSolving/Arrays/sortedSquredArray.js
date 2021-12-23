// const array = [-6, -4, -1, 1, 2, 3, 5, 8]


// // Method # 1
// const newArray =  new Array();

// for (let i=0;i<array.length;i++) {
//     let sqr = array[i] * array[i];
//     newArray[i] = sqr;
   
// }


// console.log(newArray.sort());


// // --

function sortSquares(arr)
    {
        let n = arr.length;
 
        // First convert each array elements
        // into its square
        for (let i = 0; i < n; i++)
            arr[i] = arr[i] * arr[i];
 
        // Sort an array using "inbuild sort function"
        // in Arrays class.
        return arr.sort((a, b) => a - b);
    }
 
// Driver Code
    let arr = [ -6, -3, -1, 2, 4, 5 ];

    console.log(sortSquares(arr));


// method # 2

function sortSquares_2(arr)
    {
        const n = arr.length;
        let left =0 ;
        let right = n-1;
 
        // First convert each array elements
        // into its square
        for (let i = n-1; i < 0; i--) {
            if (Math.abs(arr[left]) >  Math.abs(arr[right])) {
                arr[i] = arr[left] * arr[left];
                left++;
            } else {
                arr[i] = arr[right] * arr[right];
                right --;
            }

        }
 
        // Sort an array using "inbuild sort function"
        // in Arrays class.
        return arr;
    }
 
// Driver Code
    // let arr = [ -6, -3, -1, 2, 4, 5 ];

    console.log(sortSquares_2(arr));
