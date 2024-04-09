<script>
	import '../app.css';
	import {Navbar, NavBrand, NavHamburger, NavLi, NavUl} from 'flowbite-svelte'
	import { DarkMode } from 'flowbite-svelte';
	let darkmodebtn =
		'text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-lg p-2.5 fixed right-4 top-2 z-50';
</script>

<Navbar  >
	<NavBrand href="/">
	  <img src="https://tengrinews.kz/tengri_new/img/logo.svg" class="me-3 h-6 sm:h-9" alt="TengriNews Logo" />
	</NavBrand>
	<NavHamburger  />
	<NavUl >
	  <NavLi href="/">Главная страница</NavLi>
	  <NavLi href="/news">Новости</NavLi>
	  <NavLi><DarkMode/></NavLi>
	</NavUl>
  </Navbar>


<slot />
