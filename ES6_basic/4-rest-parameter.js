// This function returns the number of arguments passed to it
export default function returnHowManyArguments(...args) {
  return args.length; // Return the length of the args array
}

// Example usage of the function
console.log(returnHowManyArguments(1, 2, 3)); // Output: 3
console.log(returnHowManyArguments('a', 'b')); // Output: 2
console.log(returnHowManyArguments()); // Output: 0
