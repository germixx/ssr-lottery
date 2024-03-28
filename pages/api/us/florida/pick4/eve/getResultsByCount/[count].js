
const {

    getResultsByCount,

} = require('../../../../../../../functions/api/US/FL/pick4/eve/functions')

export default async function pick4eve(req, res) {

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