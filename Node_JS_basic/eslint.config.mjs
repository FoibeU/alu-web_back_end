// eslint.config.mjs
import { Linter } from 'eslint';

/** @type {Linter.Config} */
export default {
  env: {
    node: true,
    es2021: true,
  },
  extends: [
    'eslint:recommended',
  ],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
  rules: {
    'no-multiple-empty-lines': 'error',
    'eol-last': 'error',
  },
};
