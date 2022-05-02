#!/usr/bin/node

/*
* A script that searches the second biggest integer in the list of arguments
* You can assume all arguments can be converted to integer
* If no argument passed, print 0
* If the number of arguments is 1, print 0
* You must use console.log(...) to print all output
* You are not allowed to use var
*/

const args = process.argv;
let big = 0;
let secondBig = 0;
arr = [];

if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    arr.push(parseInt(args[i]));
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > big) {
      secondBig = big;
      big = arr[i];
    } else if (big > arr[i] && arr[i] > secondBig) {
      secondBig = arr[i];
    }
  }
  console.log(secondBig);
}
