const connection = require('../../../../../util/db')

function fixDate(date) {
    console.log(date)
    // console.log(date)

    return date
}
// FL Fantasy5 / endpoint
const getResult = async () => {

    function fixDate(date) {
        console.log(date)
        // console.log(date)

        return date
    }

    return new Promise((resolve, reject) => {

        try {
            connection.query('SELECT * FROM FLFantasy5 WHERE id=(SELECT max(id) FROM FLFantasy5)', [], (err, rows) => {

                if (err) throw err

                resolve({
                    success: true,
                    result: {
                        date: fixDate(rows[0].date),
                        sequence: rows[0].sequence,
                        numbers: {
                            n1: rows[0].n1,
                            n2: rows[0].n2,
                            n3: rows[0].n3,
                            n4: rows[0].n4,
                            n5: rows[0].n5,
                        },
                        jackpot: rows[0].jackpot
                    },
                })
            })
        }

        catch (error) {
            console.log(error)
        }

    })

}

const getBySequence = () => {
    return new Promise((resolve, reject) => {



    })
}

const getByDate = () => {
    return new Promise((resolve, reject) => {



    })
}

const checkNumbers = (checkNumber) => {
    return new Promise((resolve, reject) => {

        try {
            connection.query('SELECT date FROM FLFantasy5 WHERE sequence=?', [checkNumber], (err, rows) => {

                if (err) throw err
                console.log(rows, ' is rows ')

                if (rows.length > 0) {
                    resolve({
                        success: true,
                        date: rows[0].date
                    })
                } else {
                    resolve({ success: false })
                }

            })
        }

        catch (error) {
            console.log(error)
        }

    })
}

async function listAll() {
    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM FLFantasy5', [], (err, rows) => {
            if (err) throw err

            resolve({ status: true, rows })
        })
        // resolve(true)
    })
}

async function getResultsByCount(numb = 18) {

    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM (SELECT * FROM FLFantasy5 ORDER BY id DESC LIMIT ? ) sub ORDER BY id ASC', [parseInt(numb)], (err, rows) => {

            if (err) throw err

            resolve({ status: true, rows })
        })
    })
}

const getAlls = async () => {
    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM FLFantasy5', [], (err, rows) => {
            if (err) throw err

            resolve({ status: true, rows })
        })
    })

}

module.exports = {
    getBySequence,
    getResult,
    getResultsByCount,
    getByDate,
    getAlls,
    checkNumbers
}