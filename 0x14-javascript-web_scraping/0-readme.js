#!/usr/bin/node

//The first argument is the file path
const fs = require('fs');
// The content of the file must be written in utf-8
fs.readFile(process.argv[2], 'utf8', function (err, data) {
	if (err) {
		console.log(err);
	} else {
		process.stdout.write(data);
	}
});
