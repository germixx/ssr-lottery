const connection = require('../../../../../util/db')

// FL Cash4Life / endpoint
const getResult = async () => {

    function fixDate(date) {
        console.log(date)
        // console.log(date)

        return date
    }

    return new Promise((resolve, reject) => {

        try {
            connection.query('SELECT * FROM FLcash4life WHERE id=(SELECT max(id) FROM FLcash4life)', [], (err, rows) => {

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
                        },
                        cashBall: rows[0].cashBall
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

const getByNumber = async (number) => {
    return new Promise((resolve, reject) => {

        try {
            connection.query('SELECT * FROM (SELECT * FROM FLcash4life ORDER BY id DESC LIMIT ? ) sub ORDER BY id ASC', [number], (err, rows) => {
                if (err) throw err
                resolve({ status: true, rows })
            })
        } catch (e) {
            console.log(e)
        }
    })
}

const getAlls = async () => {
    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM FLcash4life', [], (err, rows) => {
            if (err) throw err

            resolve({ status: true, rows })
        })
    })

}

async function getResultsByCount(numb = 18) {

    return new Promise((resolve, reject) => {
        connection.query('SELECT * FROM (SELECT * FROM FLcash4life ORDER BY id DESC LIMIT ? ) sub ORDER BY id ASC', [parseInt(numb)], (err, rows) => {
            // console.log(rows.length)
            if (err) throw err

            resolve({ status: true, rows })
        })
    })
}

module.exports = {
    getResultsByCount,
    // getBySequence,
    getByNumber,
    getResult,
    getAlls
    // getByDate
}