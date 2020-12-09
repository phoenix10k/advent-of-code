const {once} = require('events');

(async () => {
  const numbers: number[] = [];

  const lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('src/day-01/input.txt'),
  });

  lineReader.on('line', (line: string) => {
    numbers.push(parseInt(line));
  });

  await once(lineReader, 'close');

  console.log(numbers);
  const combs: number[][] = require('combinations')(numbers, 3, 3);
  for (const comb of combs) {
    if (comb.reduce((a, b) => a + b, 0) == 2020) {
      console.log(comb.reduce((a, b) => a * b, 1));
    }
  }
})().catch((e) => {
  console.error(e);
});
