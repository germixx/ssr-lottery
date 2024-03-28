const {

    getResult,

} = require('../../../../../../functions/api/US/FL/pick4/mid/functions')

// Gets recent result - add parameter with number of results, if no parameter then send recent

export default async function pick4m(req, res) {

    const { method } = req

    switch (method) {
        case 'GET':
            res.send(await getResult())
            break
        case 'POST':
            break
        default:
            res.setHeader('Allow', ['POST'])
            res.status(405).end(`Method ${method} Not Allowed`)
            res.end()
    }
}