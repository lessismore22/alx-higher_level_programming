#!/usr/bin/node

/**
 * this module writes to a file
 *
*/
const fs = require('fs');
const filename = process.argv[2];

fs.readfile(filename, 'utf-8', (error, content) => {
	if (error) {
	  console.log(error);
	} else {
	  console.log(data.toString('utf-8'));
	}
      });	
