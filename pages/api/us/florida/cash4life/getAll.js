const {

    getAlls

} = require('../../../../../functions/api/US/FL/cash4life/functions')


export default async function getAll(req, res) {

    const { method } = req

    switch (method) {
        case 'GET':
            res.send(await getAlls())
            break
        case 'POST':

            break
        default:
            res.setHeader('Allow', ['POST'])
            res.status(405).end(`Method ${method} Not Allowed`)
            res.end()
    }


}