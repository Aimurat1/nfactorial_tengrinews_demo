// import { PUBLIC_BACKEND_URL } from '$env/static/public'
const backendUrl = import.meta.env.VITE_PUBLIC_BACKEND_URL;
const PUBLIC_BACKEND_URL = backendUrl

import { writable } from 'svelte/store';

export async function load({params, data, fetch, url}){

    let news_id = params.news_id

    let response = await fetch(`${PUBLIC_BACKEND_URL}/api/news/${news_id}/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
    })

    if (response.ok){
        let news = await response.json()
        return {
            news
        }
    }
}