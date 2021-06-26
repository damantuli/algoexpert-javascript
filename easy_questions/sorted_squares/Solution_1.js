function sortedSquaredArray(array) {
	let sortedSquares = [];
	
	for (let item of array) {
		sortedSquares.push(item*item)
	}
  return sortedSquares.sort((a, b) => a-b) || [];
}