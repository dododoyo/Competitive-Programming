var fizzBuzz = function(n) {
    let arr = new Array(n);
    for (let i = 1 ; i < n+1;i++)
        {
            if (i%15 == 0){arr[i-1] = "FizzBuzz";}
            else if (i%5 == 0){arr[i-1] = "Buzz";}
            else if (i%3 == 0){arr[i-1] = "Fizz";}
            else{ arr[i-1] = i.toString();}
        }
    return arr;
};
