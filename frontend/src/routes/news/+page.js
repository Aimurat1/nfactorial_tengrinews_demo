// import { PUBLIC_BACKEND_URL } from '$env/static/public'
const backendUrl = import.meta.env.VITE_PUBLIC_BACKEND_URL;
const PUBLIC_BACKEND_URL = backendUrl

import { writable } from 'svelte/store';

export async function load({data, fetch, url}){

    let page = url.searchParams.get("page") || 1;
    let tags = url.searchParams.get("tags");

    let searchParams = {
        page: String(page)
    }

    if (tags){
        searchParams['tags'] = tags
    }

    let response = await fetch(`${PUBLIC_BACKEND_URL}/api/news/?` + new URLSearchParams(searchParams), {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
    })

    if (response.ok){
        let news = await response.json()
        news.results = writable(news.results)
        return {
            ...news
        }
    }
}