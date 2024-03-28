
const {

    getResultsByCount,

} = require('../../../../../../functions/api/US/FL/cash4life/functions')

export default async function cash4lifer(req, res) {

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