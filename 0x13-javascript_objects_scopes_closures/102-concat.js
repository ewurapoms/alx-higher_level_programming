#!/usr/bin/node
const args = require('args');
const fileA = args.readFileSync(process.argv[2], 'utf8');
const fileB = args.readFileSync(process.argv[3], 'utf8');
args.writeFileSync(process.argv[4], fileA + fileB);
