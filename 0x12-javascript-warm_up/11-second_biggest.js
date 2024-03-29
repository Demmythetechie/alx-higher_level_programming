#!/usr/bin/node

// This script searches the second biggest integer in the list of arguments.

function mergeSort (arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const middle = Math.floor(arr.length / 2);
  const leftHalf = arr.slice(0, middle);
  const rightHalf = arr.slice(middle);

  const sortedLeft = mergeSort(leftHalf);
  const sortedRight = mergeSort(rightHalf);

  return merge(sortedLeft, sortedRight);
}

function merge (left, right) {
  const result = [];
  let leftIndex = 0;
  let rightIndex = 0;

  while (leftIndex < left.length && rightIndex < right.length) {
    if (Number(left[leftIndex]) < Number(right[rightIndex])) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }

  return result.concat(left.slice(leftIndex), right.slice(rightIndex));
}

const array = process.argv.slice(2);
const sortedArray = mergeSort(array);
if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(sortedArray[sortedArray.length - 2]);
}
