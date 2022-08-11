const readFileSync = require("fs").readFileSync
const data = readFileSync('./input.txt', 'utf-8')

let correctCount = 0;

data.split('\n').map(row => {
  let passphrases = row.split(' ');
  let setOfPhrases = new Set(passphrases);
  setOfPhrases.size == passphrases.length ? correctCount++ : "Skip"
})

console.log('Total correct: ', correctCount);