#!usr/bin/node

const myVal = process.argv.length - 2;

if (myVal === 0) {
    console.log('No argument`);
}
 else if (myVal === 1) {
    console.log('Argument found');
}
else{
    console.log('Arguments found');
}


