#!/usr/bin/node

const first = parseInt(process.argv[2]);

if (isNaN(first)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < first; i++) {
    let row = '';

    for (let j = 0; j < first; j++) {
      row += 'X';
    }

    console.log(row);
  }
}
