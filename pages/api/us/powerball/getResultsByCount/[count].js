
const {

    getResultsByCount,

} = require('../../../../../functions/api/US/FL/powerball/functions')

export default async function powerball(req, res) {

    const { method } = req

    const pa = req.query

    const count = pa.count

    switch (method) {
        case 'GET':
            res.send(await getResultsByCount(count))
            break
        case 'POST':
            break
        default:
            res.setHeader('Allow', ['POST'])
            res.status(405).end(`Method ${method} Not Allowed`)
            res.end()
    }
}