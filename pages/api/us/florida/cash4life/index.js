const {

    getResult,

} = require('../../../../../functions/api/US/FL/cash4life/functions')

export default async function fantasy5(req, res) {

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