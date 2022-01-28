const numToReverseString = function (num: number) {
  let string = num.toString();
  let splitString = string.split('');
  let reverse = splitString.reverse();
  let join = reverse.join('');
  return join;
};

type romanSymbols = {
  [key: number]: {
    one: string
    five?: string
  }
}

const symbols: romanSymbols = {
  1: {
    one: 'I',
    five: 'V',
  },
  10: {
    one: 'X',
    five: 'L',
  },
  100: {
    one: 'C',
    five: 'D',
  },
  1000: {
    one: 'M',
  },
};

const getMagnitude = function (digitPosition: number) : number {
  const magnitude: { [key: string] : number } = { 1: 0, 10: 1, 100: 2, 1000: 3 };
  const result = Object.keys(magnitude).find((key) => magnitude[key] === digitPosition);
  return parseInt(result!)
};

const getRoman = function (digit: string, magnitude: number) : string {
  let romanDigit: string;
  switch (digit) {
    case '1':
      romanDigit = symbols[magnitude].one;
      break;
    case '2':
      romanDigit = symbols[magnitude].one.repeat(2);
      break;
    case '3':
      romanDigit = symbols[magnitude].one.repeat(3);
      break;
    case '4':
      romanDigit = symbols[magnitude].one + symbols[magnitude].five;
      break;
    case '5':
      romanDigit = symbols[magnitude].five!;
      break;
    case '6':
      romanDigit = symbols[magnitude].five + symbols[magnitude].one;
      break;
    case '7':
      romanDigit = symbols[magnitude].five + symbols[magnitude].one.repeat(2);
      break;

    case '8':
      romanDigit = symbols[magnitude].five + symbols[magnitude].one.repeat(3);
      break;

    case '9':
      romanDigit = symbols[magnitude].one + symbols[magnitude * 10].one;
      break;

    default:
      romanDigit = ""
  }
  return romanDigit;
};

const intToRoman = (num: number) => {
  let numString: string = numToReverseString(num);
  let output: string = '';
  for (let i = 0; i < numString.length; i++) {
    let char: string = getRoman(numString.charAt(i), getMagnitude(i));
    output = char + output;
    }
  console.log(output);
  return output;
};

module.exports = intToRoman