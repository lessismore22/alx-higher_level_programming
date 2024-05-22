#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
    console.error('Please provide the API URL as the first argument.');
    process.exit(1);
}

request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
        console.error('Error making request:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error('Error: Received status code', response.statusCode);
        return;
    }

    const completedTasksByUser = {};

    body.forEach(task => {
        if (task.completed) {
            if (!completedTasksByUser[task.userId]) {
                completedTasksByUser[task.userId] = 0;
            }
            completedTasksByUser[task.userId]++;
        }
    });

    for (const userId in completedTasksByUser) {
        if (completedTasksByUser.hasOwnProperty(userId)) {
            console.log(`User ${userId} has completed ${completedTasksByUser[userId]} tasks`);
        }
    }
});

