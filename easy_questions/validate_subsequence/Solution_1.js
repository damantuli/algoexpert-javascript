function isValidSubsequence(array, sequence) {
	let i = 0;
		for (let item of array) {
			if (item === sequence[i]) {
					i++;
			}
		}
	return i == sequence.length
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;