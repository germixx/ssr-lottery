const {

    getResult,

} = require('../../../../../../functions/api/US/FL/pick2/eve/functions')

// Gets recent result - add parameter with number of results, if no parameter then send recent

export default async function pick2eve(req, res) {

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