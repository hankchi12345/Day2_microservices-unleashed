const mysql = require('mysql2');
const express = require('express');
const app = express();

const conn = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: process.env.DB_NAME
});

app.get('/users', (req, res) => {
  conn.query('SELECT * FROM users', (err, results) => {
    if (err) return res.status(500).send(err.toString());
    res.json(results);
  });
});

app.listen(3000, () => {
  console.log('Dev01 Service running on port 3000');
});
