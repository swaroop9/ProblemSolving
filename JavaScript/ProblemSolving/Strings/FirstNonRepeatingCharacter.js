let s = 'aaabcccdeeffg'


/*
* Method 1 : O(n)
*/
function firstNonRepeatingChararcter_1(s) {

    for (i = 0; i < s.length; i++) {
        // console.log(s, s.indexOf(s[i]), s.lastIndexOf(s[i]));
        if (s.indexOf(s[i]) == s.lastIndexOf(s[i])) {
            return s[i];
        }
    }

    return '_';
}

console.log(firstNonRepeatingChararcter_1(s));



/*
* Method 2
*/
function firstNonRepeatingChararcter_2(s) {

    let charArray = new Array(26).fill(0);
    // console.log('c'.charCodeAt(0) - 'a'.charCodeAt(0))
    for (char of s) {
        // console.log(char);
        // console.log(charArray[char.charCodeAt(0) - 'a'.charCodeAt(0)]);
        charArray[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }

    // console.log(charArray);


    for (char of s) {
        if (charArray[char.charCodeAt(0) - 'a'.charCodeAt(0)] == 1) return char;
    }
    return '_';
}

console.log(firstNonRepeatingChararcter_2(s));



/*
* Method 3 : O(n)
*/
function firstNonRepeatingChararcter_3(s) {

    for (let i = 0; i < s.length; i++) {
        let count =0;
        for (let j = 0; j < s.length ;j++) {

       if (s[i] == s[j] ) {
           count++;
        }        
    }
    if (count == 1) return s[i];
}

    return '_';
}

console.log("O(n*n)",firstNonRepeatingChararcter_3(s));



/*
* Method 4 
*/
function firstNonRepeatingChararcter_4(s) {

    let obj = {a: 0, b: 0, c: 0, d: 0, e: 0, f: 0, g: 0}

    for (char of s) {
        if (char in obj){
            obj[char]++;
        }
    }

    // console.log(charArray);


    for (key of Object.keys(obj)) {
        if (obj[key] == 1) {
            return key;
        }
        
    }
    return '_';
}

console.log("4", firstNonRepeatingChararcter_4(s));