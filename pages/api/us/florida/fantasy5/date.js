
const dates = async () => {
    return new Promise((resolve, reject) => {
        resolve(true)
    })
}

export default async function fantasy5(req, res) {
    const { method } = req
    switch (method) {
        case 'GET':
            res.send(await dates())
            break
        case 'POST':
            break
        default:
            res.setHeader('Allow', ['POST'])
            res.status(405).end(`Method ${method} Not Allowed`)
            res.end()
    }
}