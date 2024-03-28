const connection = require('../../../../../../util/db')

// FL Fantasy5 / endpoint
const getResult = async () => {

    function fixDate(date) {
        console.log(date)
        // console.log(date)

        return date
    }

    return new Promise((resolve, reject) => {

        try {
            connection.query('SELECT * FROM FLPick3Day WHERE id=(SELECT max(id) FROM FLPick3Day)', [], (err, rows) => {

                if (err) throw err

                resolve({
                    success: true,
                    result: {
                        date: fixDate(rows[0].date),
                        sequence: rows[0].sequence,
                        numbers: {
                            n1: rows[0].firstNum,
                            n2: rows[0].secondNum,
                            n3: rows[0].thirdNum,
                            FB: rows[0].fireBall,

                        },
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

const checkNumbers = () => {

}

async function listAll() {
    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM FLPick3Day', [], (err, rows) => {
            if (err) throw err

            resolve({ status: true, rows })
        })
        // resolve(true)
    })
}

async function getResultsByCount(numb = 18) {

    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM (SELECT * FROM FLPick3Day ORDER BY id DESC LIMIT ? ) sub ORDER BY id ASC', [parseInt(numb)], (err, rows) => {

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
    checkNumbers
}