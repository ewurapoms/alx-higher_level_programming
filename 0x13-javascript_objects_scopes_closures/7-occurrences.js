#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numO = 0;

  for (let count = 0; count <= list.length; count++) {
    if (list[count] === searchElement) {
      numO++;
    }
  }
  return numO;
};
