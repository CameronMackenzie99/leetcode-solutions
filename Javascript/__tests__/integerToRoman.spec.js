const intToRoman = require('../integertoroman');

const { expect } = require('@jest/globals');

describe('Convert Int to Roman Numeral', () => {
  it('should return "III" for intToRoman(3)', () => {
    expect(intToRoman(3)).toEqual('III');
  });

  it('should return "LVIII" for intToRoman(58)', () => {
    expect(intToRoman(58)).toEqual('LVIII');
  });

  it('should return "MCMXCIV" for intToRoman(1994)', () => {
    expect(intToRoman(1994)).toEqual('MCMXCIV');
  });

  it('should return "MMMCMXCIX" for intToRoman(3999)', () => {
    expect(intToRoman(3999)).toEqual('MMMCMXCIX');
  });
});
