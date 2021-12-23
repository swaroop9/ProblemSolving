let arr =[-2, 2, 5, -11, 6]

function arrayMaxConsucutiveSum(arr) {
    let max_sum =0, cur_sum = 0;
    // console.log(max_sum);
   // console.log(cur_sum);

    for (i = 0; i < arr.length ; i++) {
        let cur_sum = 0;
        for (j = i; j < arr.length; j++) {
            cur_sum += arr[j];
            if (cur_sum > max_sum) {
                max_sum = cur_sum
            }
        }
    }
    return max_sum;
    
}

console.log(arrayMaxConsucutiveSum(arr));