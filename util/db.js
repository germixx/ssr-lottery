//MySQL
const mysql = require('mysql')

let config = require('./config')['production']

const connection = mysql.createConnection({
    host: config.Host,
    user: config.User,
    password: config.Password,
    database: config.Database
})

connection.connect((err) => {
    if (!err) { console.log('Successful connection to MYSQL database.') }
    else console.log('Main Database connection fail')
})

module.exports = connection