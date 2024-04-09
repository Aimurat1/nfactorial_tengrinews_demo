<script>
// @ts-nocheck

	import { Card, Button, Toggle, Breadcrumb, BreadcrumbItem, Heading, Badge, Input, Pagination, Mark} from 'flowbite-svelte';
	import { ArrowRightOutline, SearchOutline, ChevronLeftOutline, ChevronRightOutline} from 'flowbite-svelte-icons';
	import {goto} from '$app/navigation'
	import {page} from '$app/stores'
	import { formatDate } from '$lib/utils/formatDate'
	// import { PUBLIC_BACKEND_URL } from '$env/static/public'
	const backendUrl = import.meta.env.VITE_PUBLIC_BACKEND_URL;
	const PUBLIC_BACKEND_URL = backendUrl

	export let data;

	$: totalItems = data.count
	$: currentPage = Number($page.url.searchParams.get('page')) || 1;
	$: news = data.results

	$: search_tag = $page.url.searchParams.get("tags") || undefined
	
	let totalPages = data.total_pages

	let pages = []

	for (let i = 0; i < Number(totalPages); i++){
		pages.push({
			name: i+1,
			href: `?page=${i+1}`
		})
	}

	$: {
		pages.forEach((page) => {
		if (page.name == currentPage) {
			page.active = true;
		} else {
			page.active = false;
		}
		});
		pages = pages;
	}

	const previous = () => {
		if (currentPage-1 >= 1){
			goto(`?page=${currentPage-1}`)
		}
	};
	const next = () => {
		if (currentPage+1 <= totalPages){
			goto(`?page=${currentPage+1}`)
		}
	};

	function limitWordLength(str, limit = 30) {
		const words = str.split(/\s+/); // Split string into words based on whitespace
		if (words.length > limit) {
			return words.slice(0, limit).join(' ') + '...'; // Join the first 30 words and append '...'
		}
		return str; // Return original string if it doesn't exceed the limit
	}

	function handleSearchNews(event){

		async function fetchSearchedNews(search){
			let response = await fetch(`${PUBLIC_BACKEND_URL}/api/news/?` + new URLSearchParams({
				search: String(search),
				page_size: 50
			}), {
				method: 'GET',
				headers: {
				'Content-Type': 'application/json',
				},
			})

			let news = await response.json()
			return {
				...news
			}
		}

		let search = event.target.value

		if (search == ""){
			goto(`/news?page=${currentPage}`)
		}
		fetchSearchedNews(search).then(({results}) => {
			$news = results
		})

	}

	

</script>

<div class="flex justify-center items-center ">
	<div class="container w-4/5 pb-20">

		<Breadcrumb aria-label="Solid background breadcrumb example" solid>
			<BreadcrumbItem href="/" home>Главная</BreadcrumbItem>
			<BreadcrumbItem>Новости</BreadcrumbItem>
		</Breadcrumb>
		  
		  

		<div class="text-center">
			<Heading tag="h1" class="p-10" customSize="text-3xl font-extrabold  md:text-4xl lg:text-4xl">Новостной портал - <Mark class="bg-green-700 dark:bg-green-700">TengriNews</Mark></Heading>
		</div>

		<div class = "pb-5">
			<div class="flex justify-between">
				<div class="flex gap-3">
					<Heading tag="h2" class="" customSize="text-2xl font-extrabold  md:text-2xl lg:text-2xl">{search_tag ? `Поиск по тегу "${search_tag}"` : "Все новости"}</Heading>
					{#if search_tag}
						 <!-- content here -->
						 <Button size="sm" color="blue" href={`/news?page=${currentPage}`} outline>Сбросить</Button>
					{/if}
				</div>
				<div class="flex">
					<Button color="none" data-collapse-toggle="mobile-menu-3" aria-controls="mobile-menu-3" aria-expanded="false" class="md:hidden text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5 me-1">
					  <SearchOutline class="w-5 h-5" />
					</Button>
					<div class="hidden relative md:block">
					  <div class="flex absolute inset-y-0 start-0 items-center ps-3 pointer-events-none">
						<SearchOutline class="w-4 h-4" />
					  </div>
					  <Input on:input={handleSearchNews} id="search-navbar" class="ps-10" placeholder="Поиск новостей" />
					</div>
				</div>
			</div>
			
		</div>

		<div class="grid gap-x-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-3 " style="row-gap: 30px">
			
			{#each $news as news_instance}
			<div class="space-y-4">
				<div class="max-w-md bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
					<a href={`/news/${news_instance.id}/`}>
						<img class="rounded-t-lg" src={news_instance.image_url} alt="" style="width: 28rem; height: 220px; object-fit: cover;"/>
					</a>

					<div class="p-5">
						<div class="mb-4 flex flex-wrap flex-row gap-2">
							{#each news_instance.tags as tag}
							<Badge href={`/news?tags=${tag.tag}`} color="dark">
								{tag.tag}
							</Badge>
							{/each}
							

						</div>

						<div class="mb-4 flex flex-wrap flex-row gap-2">
							<Badge color="green">
								{formatDate(news_instance.datetime)}
							</Badge>
						</div>
						<a class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white hover:text-green-900" href={`/news/${news_instance.id}/`} style="line-height: 1.8rem">{news_instance.title}</a>
						<p class="mt-3 mb-3 font-sm text-gray-700 dark:text-gray-400 leading-tight">{limitWordLength(news_instance.annotation)}</p>
						<Button color="green" href={`/news/${news_instance.id}/`}>
						Полная статья <ArrowRightOutline class="w-3.5 h-3.5 ms-2 text-white" />
						</Button>
						
						
						
					</div>
					
				</div>
			</div>
			{/each}

			
		</div>

		<div class="mt-5 pagination">
			<Pagination {pages} large on:previous={previous} on:next={next} icon>
				<svelte:fragment slot="prev">
				  <span class="sr-only">Назад</span>
				  <ChevronLeftOutline class="w-3 h-3" />
				</svelte:fragment>
				<svelte:fragment slot="next">
				  <span class="sr-only">Вперед</span>
				  <ChevronRightOutline class="w-3 h-3" />
				</svelte:fragment>
			  </Pagination>
		</div>
	</div>

</div>

<style>
	.pagination{
		display: flex; justify-content: flex-end
	}
</style>
	
