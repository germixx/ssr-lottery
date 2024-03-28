import Head from 'next/head'

import LOGIN from '../components/login'

function login() {
    return (
        <div>
            <Head>
                <title>Login</title>
                <meta name="description" content="Draw Effects" />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <LOGIN />
        </div>
    )
}

export default login