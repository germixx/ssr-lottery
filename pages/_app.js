import 'bootstrap/dist/css/bootstrap.css'
import '../styles/globals.css'

import { useEffect, useState } from "react"

import { useRouter } from 'next/router'

import { StateProvider } from '../Context/StateProvider'

import reducer, { initialState } from '../Context/Reducer'

function MyApp({ Component, pageProps }) {
    console.log('_app.js')
    const router = useRouter()

    const [currentGameView, setCurrentGameView] = useState('')

    const changeGame = (e) => {

        setCurrentGameView(e)

        router.push({ pathname: `/profile/play/${e}` })

    }

    useEffect(() => {
        import("bootstrap/dist/js/bootstrap")





    }, [])
    return <StateProvider initialState={initialState} reducer={reducer} >
        <Component {...pageProps} changeGame={changeGame} currentGameView={currentGameView} />
    </StateProvider>

}

export default MyApp
