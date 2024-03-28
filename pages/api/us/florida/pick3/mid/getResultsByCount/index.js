
const {

    getResultsByCount,

} = require('../../../../../../../functions/api/US/FL/pick3/mid/functions')

export default async function pick3m(req, res) {

    const { method } = req
    const pa = req.params

    switch (method) {
        case 'GET':
            res.send(await getResultsByCount())
            break
        case 'POST':
            break
        default:
            res.setHeader('Allow', ['POST'])
            res.status(405).end(`Method ${method} Not Allowed`)
            res.end()
    }
}