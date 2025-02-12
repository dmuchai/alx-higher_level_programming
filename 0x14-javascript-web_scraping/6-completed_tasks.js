#!/usr/bin/node
// Script that computes the number of tasks completed by user ID.

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const completedTasks = {};

    data.forEach(task => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    console.log(completedTasks);
  }
});
