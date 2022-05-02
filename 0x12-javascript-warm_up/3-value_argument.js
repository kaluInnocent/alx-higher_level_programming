#!/usr/bin/node

/**
 * A script that prints the first argument
 * If no arguments are passed to are passed to tge script, print 'No argument'
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You are not allowed to use length
*/

const arg = process.argv.slice(2);
if (arg){
	for (args in arg){
		console.log(args);
	}
} else{
	console.log('No argument');
}
