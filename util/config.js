const config = {
    development: {
        //Database
        Host: process.env.DB_HOST,
        User: process.env.DB_USER,
        User2: process.env.DB_USER2,
        Password: process.env.DB_PASSWORD,
        Database: process.env.DB,
        Database2: process.env.DB2,
        //JSON Web Token
        tokenSecretKey: process.env.TOKEN
    },

    production: {
        //Database
        Host: process.env.DB_HOST,
        User: process.env.DB_USER,
        User2: process.env.DB_USER2,
        Password: process.env.DB_PASSWORD,
        Database: process.env.DB,
        Database2: process.env.DB2,
        //JSON Web Token
        tokenSecretKey: process.env.TOKEN
    }
}

module.exports = config;