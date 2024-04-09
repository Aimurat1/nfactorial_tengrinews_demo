// /** @type {import('@sveltejs/kit').HandleFetch} */
// export async function handleFetch({ request, fetch }) {

// 	console.log(request.url)
// 	request = new Request(
// 		request.url.replace('http://127.0.0.1:8000/', 'http://backend:8000/'),
// 		request
// 	);

// 	return fetch(request);
// }

/** @type {import('@sveltejs/kit').Handle} */
export const handle = async ({ event, resolve }) => {
    const originalFetch = event.fetch;

    event.fetch = async (resource, init) => {

		console.log(resource)
        if (typeof resource === 'string' && (resource.startsWith('http://158.160.62.15:8000') || resource.startsWith('http://127.0.0.1:8000')) ) {
            // Modify the URL here if it matches your criteria
            resource = resource.replace('http://158.160.62.15:8000', 'http://backend:8000');
            // resource = resource.replace('http://127.0.0.1:8000', 'http://backend:8000');

        } else if (resource instanceof Request && (resource.url.startsWith('http://158.160.62.15:8000') || resource.url.startsWith('http://127.0.0.1:8000'))) {
            // For Request objects, modify the URL property
            const newUrl = resource.url.replace('http://158.160.62.15:8000', 'http://backend:8000');
            // const newUrl = resource.url.replace('http://localhost:8000', 'http://backend:8000');
            resource = new Request(newUrl, resource);
        }

        return originalFetch(resource, init);
    };

    return resolve(event);
};
