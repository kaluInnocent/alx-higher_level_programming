#!/usr/bin/node

/*
 * script pribts the addition of two numbers
 * The first argument is the first integer
 * The second argument is the second integer
 */

function add(a, b) {
	a = process.argv[2];
	b = process.argv[3];

	console.log(a + b);
}
