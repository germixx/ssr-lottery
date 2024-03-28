

import { NextResponse, NextRequest } from 'next/server'

// This function can be marked `async` if using `await` inside
export function middleware(request) {
    console.log('middlewarefile')
    let verify = true
    let url = request.url
    console.log(url)
    console.log('asdajdlkajdlkajdlkajkdlajldkjadlkjalkjcxlm,vncm,nfkjldgkfmncv')
    if (verify && url.includes('/profile')) {
        console.log('squirtssssssssss')
        return NextResponse.redirect(new URL('/profile', request.url))
    }

    if (request.nextUrl.pathname.startsWith('/dashboard')) {
        return NextResponse.rewrite(new URL('/profile/', request.url))
    }


}




// See "Matching Paths" below to learn more
export const config = {
    matcher: '/profile',
}