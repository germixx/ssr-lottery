const connection = require('../../../../../util/db')

// FL JTP / endpoint
const getResult = async () => {

    function fixDate(date) {
        console.log(date)
        // console.log(date)

        return date
    }

    return new Promise((resolve, reject) => {

        try {
            connection.query('SELECT * FROM FLlotto WHERE id=(SELECT max(id) FROM FLlotto)', [], (err, rows) => {

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
                            n4: rows[0].fourthNum,
                            n5: rows[0].fifthNum,
                            n6: rows[0].sixthNum
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
        connection.query('SELECT * FROM FLlotto', [], (err, rows) => {
            if (err) throw err

            resolve({ status: true, rows })
        })
        // resolve(true)
    })
}

async function getResultsByCount(numb = 18) {

    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM (SELECT * FROM FLlotto ORDER BY id DESC LIMIT ? ) sub ORDER BY id ASC', [parseInt(numb)], (err, rows) => {

            if (err) throw err

            resolve({ status: true, rows })
        })
    })
}

const getAlls = async () => {
    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM FLlotto', [], (err, rows) => {
            if (err) throw err

            resolve({ status: true, rows })
        })
    })

}

module.exports = {
    getAlls,
    getBySequence,
    getResult,
    getResultsByCount,
    getByDate,
    checkNumbers
}