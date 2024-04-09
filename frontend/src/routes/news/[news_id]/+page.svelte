<script>
    // @ts-nocheck
    
        import { Hr, P, Breadcrumb, BreadcrumbItem, Heading, Badge, Blockquote } from 'flowbite-svelte';
        import {goto} from '$app/navigation'
        import {page} from '$app/stores'
        import { formatDate } from '$lib/utils/formatDate'
    
        export let data;

        let news = data.news

        // console.log(news)
    
</script>

<div class="flex justify-center items-center ">
    <div class="container w-2/3" style="padding: 50px 0 50px 0">

        <Breadcrumb aria-label="Solid background breadcrumb example" class="mb-5" solid>
			<BreadcrumbItem href="/" home>Главная</BreadcrumbItem>
			<BreadcrumbItem href="/news">Новости</BreadcrumbItem>
			<BreadcrumbItem>{news.title}</BreadcrumbItem>
		</Breadcrumb>

        <Heading tag="h1" customSize="text-3xl font-extrabold  md:text-4xl lg:text-5xl">{news.title}</Heading>
        <div class="mb-2 mt-2 flex flex-wrap flex-row gap-2">
							<Badge color="green">
								{formatDate(news.datetime)}
							</Badge>
					</div>
        <Hr/>
        <img class = "pt-5 pb-5" src={news.image_url} alt="" style="width: 100%">
        <P class="md:text-2xl" weight="bold" size="xl" color="text-gray-700 dark:text-gray-400">{news.annotation}</P>
        <Hr/>
        
        <div class="content pt-5 pb-5">
            {@html news.content}
        </div>

        <Hr/>

        <div class="pt-5 flex flex-wrap flex-row gap-2">
            {#each news.tags as tag}
            <Badge href={`/news?tags=${tag.tag}`} large color="green">
                {tag.tag}
            </Badge>
            {/each}
            

        </div>
    </div>

</div>

<style>


    :global(.content > *:not(:last-child)) {
            margin-bottom: 20px;
    }

    :global(.content *) {
        font-size: 20px;
    }

    :global(.content blockquote){
        margin-top: 1rem/* 16px */;
        margin-bottom: 1rem/* 16px */;

        padding: 1rem;
        border-inline-start-width: 4px;
        --tw-bg-opacity: 1;
        background-color: rgb(222 247 236 / var(--tw-bg-opacity));
    }

    :global(.content blockquote p){
        font-style: italic;
    }

    :global(.content blockquote:is(.dark)){
        --tw-border-opacity: 1;
        border-color: rgb(107 114 128 / var(--tw-border-opacity));
    }

    :global(.content a) {
        font-weight: 600;
        color: rgb(3 84 63 / var(--tw-bg-opacity))
    }
</style>
        
