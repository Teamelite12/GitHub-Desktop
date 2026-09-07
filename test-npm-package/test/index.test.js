const test = require('node:test');
const assert = require('node:assert/strict');
const greeting = require('../index');

test('greeting returns predictable default message', () => {
  assert.equal(greeting(), 'Hello, world!');
});

test('greeting interpolates provided name', () => {
  assert.equal(greeting('npm'), 'Hello, npm!');
});
