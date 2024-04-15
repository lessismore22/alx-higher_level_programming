#!/usr/bin/node

const myVal0 = parseInt(process.argv[2]);


if (myVal0) {
    console.log('My number' + myVal0);
}
else {
    console.log('Not a number');
}
