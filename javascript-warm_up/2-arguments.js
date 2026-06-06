#!/usr/bin/node
const say  = process.argv.length;
if (say === 2) {
  console.log('No argument');
} else if (say === 3) { 
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
