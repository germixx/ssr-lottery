const {

    checkNumbers,

} = require('../../../../../functions/api/US/FL/fantasy5/functions')

export default async function checkWinningNumbers(req, res) {

    const { method } = req

    const checkNumber = req.body.checkNumber

    switch (method) {
        case 'GET':
            break
        case 'POST':
            res.send(await checkNumbers(checkNumber))
            break
        default:
            res.setHeader('Allow', ['POST'])
            res.status(405).end(`Method ${method} Not Allowed`)
            res.end()
    }
}