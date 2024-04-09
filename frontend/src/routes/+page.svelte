<script>
// @ts-nocheck

	import { Button, Heading, Mark } from 'flowbite-svelte';
	import { ArrowRightOutline} from 'flowbite-svelte-icons';
	import { Section, HeroHeader, Cta } from 'flowbite-svelte-blocks'

	import demo from "$lib/images/demo.png";
	import docker_logo from "$lib/images/docker_logo.png";
	
	// import { PUBLIC_BACKEND_URL } from '$env/static/public'
	const backendUrl = import.meta.env.VITE_PUBLIC_BACKEND_URL;
	const PUBLIC_BACKEND_URL = backendUrl
	
	console.log(PUBLIC_BACKEND_URL)

</script>

<div class="flex justify-center items-center ">
	<div class="container w-4/5 pt-20 pb-20">

		<!-- <Heading>Hello!</Heading> -->
		
		<Section name="ctawithimg">
			<Cta ctatype="image">
			<svelte:fragment slot="img">
				<img class="w-full border-2 rounded-lg border-green-700 border-solid " src={demo} alt="dashboard" />
			</svelte:fragment>
			<svelte:fragment slot="h2">
				<Heading class="mb-4" style="line-height: 1.2em">
					Клон TengriNews by <Mark>Aimurat Zhetkizgenov</Mark>.
				</Heading>
			</svelte:fragment>
			<p class="mb-6 font-light text-gray-500 md:text-lg dark:text-gray-400">
				Данный проект является тестовым заданием для <Mark class="bg-red-700 dark:bg-red-700">nFactorial Incubator</Mark>
			</p>
			<Button href="/news" color="blue">
				Перейти к новостям
				<ArrowRightOutline class="w-3.5 h-3.5 ms-2" />
			</Button>
			</Cta>
		</Section>

		<div style="padding: 40px 0 40px 0;"></div>
		<Section name="logos">
			<HeroHeader >
			  <svelte:fragment slot="h2">Создано с использованием:</svelte:fragment>
			  <div class="mt-8 grid grid-cols-2 gap-8 text-gray-500 sm:gap-12 md:grid-cols-3 lg:grid-cols-5 dark:text-gray-400">
				<a href="/" class="flex flex-col justify-center items-center">
					<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" height="100px" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 98.1 118" style="enable-background:new 0 0 98.1 118;" xml:space="preserve">
						<style type="text/css">
							.st0{fill:#FF3E00;}
							.st1{fill:#FFFFFF;}
						</style>
						<path class="st0" d="M91.8,15.6C80.9-0.1,59.2-4.7,43.6,5.2L16.1,22.8C8.6,27.5,3.4,35.2,1.9,43.9c-1.3,7.3-0.2,14.8,3.3,21.3  c-2.4,3.6-4,7.6-4.7,11.8c-1.6,8.9,0.5,18.1,5.7,25.4c11,15.7,32.6,20.3,48.2,10.4l27.5-17.5c7.5-4.7,12.7-12.4,14.2-21.1  c1.3-7.3,0.2-14.8-3.3-21.3c2.4-3.6,4-7.6,4.7-11.8C99.2,32.1,97.1,22.9,91.8,15.6"/>
						<path class="st1" d="M40.9,103.9c-8.9,2.3-18.2-1.2-23.4-8.7c-3.2-4.4-4.4-9.9-3.5-15.3c0.2-0.9,0.4-1.7,0.6-2.6l0.5-1.6l1.4,1  c3.3,2.4,6.9,4.2,10.8,5.4l1,0.3l-0.1,1c-0.1,1.4,0.3,2.9,1.1,4.1c1.6,2.3,4.4,3.4,7.1,2.7c0.6-0.2,1.2-0.4,1.7-0.7L65.5,72  c1.4-0.9,2.3-2.2,2.6-3.8c0.3-1.6-0.1-3.3-1-4.6c-1.6-2.3-4.4-3.3-7.1-2.6c-0.6,0.2-1.2,0.4-1.7,0.7l-10.5,6.7  c-1.7,1.1-3.6,1.9-5.6,2.4c-8.9,2.3-18.2-1.2-23.4-8.7c-3.1-4.4-4.4-9.9-3.4-15.3c0.9-5.2,4.1-9.9,8.6-12.7l27.5-17.5  c1.7-1.1,3.6-1.9,5.6-2.5c8.9-2.3,18.2,1.2,23.4,8.7c3.2,4.4,4.4,9.9,3.5,15.3c-0.2,0.9-0.4,1.7-0.7,2.6l-0.5,1.6l-1.4-1  c-3.3-2.4-6.9-4.2-10.8-5.4l-1-0.3l0.1-1c0.1-1.4-0.3-2.9-1.1-4.1c-1.6-2.3-4.4-3.3-7.1-2.6c-0.6,0.2-1.2,0.4-1.7,0.7L32.4,46.1  c-1.4,0.9-2.3,2.2-2.6,3.8s0.1,3.3,1,4.6c1.6,2.3,4.4,3.3,7.1,2.6c0.6-0.2,1.2-0.4,1.7-0.7l10.5-6.7c1.7-1.1,3.6-1.9,5.6-2.5  c8.9-2.3,18.2,1.2,23.4,8.7c3.2,4.4,4.4,9.9,3.5,15.3c-0.9,5.2-4.1,9.9-8.6,12.7l-27.5,17.5C44.8,102.5,42.9,103.3,40.9,103.9"/>
					</svg>
					<p class="mt-3 font-bold text-black md:text-lg dark:text-gray-400 "
						style="font-size: 25px">SvelteKit</p>
				</a>
				<a href="/" class="flex flex-col justify-center items-center">
					<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt=""
						style="height:110px">
					<p class=" font-bold text-black md:text-lg dark:text-gray-400 "
						style="font-size: 25px">Python</p>
				</a>
				<a href="/" class="flex flex-col justify-center items-center">
					<svg height="100px" viewBox="0 0 256 326" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin meet"><g fill="#2BA977"><path d="M114.784 0h53.278v244.191c-27.29 5.162-47.38 7.193-69.117 7.193C33.873 251.316 0 222.245 0 166.412c0-53.795 35.93-88.708 91.608-88.708 8.64 0 15.222.68 23.176 2.717V0zm1.867 124.427c-6.24-2.038-11.382-2.717-17.965-2.717-26.947 0-42.512 16.437-42.512 45.243 0 28.046 14.88 43.532 42.17 43.532 5.896 0 10.696-.332 18.307-1.351v-84.707z"/><path d="M255.187 84.26v122.263c0 42.105-3.154 62.353-12.411 79.81-8.64 16.783-20.022 27.366-43.541 39.055l-49.438-23.297c23.519-10.93 34.901-20.588 42.17-35.327 7.61-15.072 10.01-32.529 10.01-78.445V84.261h53.21zM196.608 0h53.278v54.135h-53.278V0z"/></g></svg>
					<p class="mt-3 font-bold text-black md:text-lg dark:text-gray-400 "
						style="font-size: 25px">Django</p>
				</a>
				<a href="/" class="flex flex-col justify-center items-center">
					<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tailwind_CSS_Logo.svg/2560px-Tailwind_CSS_Logo.svg.png" alt=""
						style="height: 100px">
					<p class="mt-3 font-bold text-black md:text-lg dark:text-gray-400 "
						style="font-size: 25px">Tailwind CSS</p>
				</a>

				<a href="/" class="flex flex-col justify-center items-center">
					<img src={docker_logo} alt=""
						style="height: 100px">
					<p class="mt-3 font-bold text-black md:text-lg dark:text-gray-400 "
						style="font-size: 25px">Docker</p>
				</a>
				
			  </div></HeroHeader>
		  </Section>
	</div>

</div>

<style>
</style>
	
