export const initialState = {
    user: { loggedin: false },
    userLocation: { latitude: null, longitude: null }
}

function reducer(state, action) {

    switch (action.type) {
        case 'TEST':
            console.log('test ius t')
            return {
                ...state,
                cats: { num: 5555 }
            }
            break;
        case 'AUTHENTICATE_USER':
            return {
                ...state,
                user: action.data,
                loggedin: true
            }
        case 'REFRESH':
            return {
                ...state,
                user: action.data,
                loggedin: true

            }
        case 'LOGOUT':
            return {
                user: { loggedin: false },
                userLocation: { latitude: null, longitude: null }
            }
        default:
            return state;
            break;
    }
}

export default reducer;
