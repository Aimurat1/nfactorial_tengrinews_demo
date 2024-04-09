
# Tengrinews Clone - nFactorial Demo task

nFactorial demo task for 2nd round - Tengrinews Clone with parsing.


## Demo

[Демо версия сайта](http://158.160.62.15/) - http://158.160.62.15/

[Админ панель Django](http://158.160.62.15:8000/admin/) - http://158.160.62.15:8000/admin/

- Логин - admin
- Пароль - qwerty 


## Installation

You need to install docker and docker-compose to your local machine! 

Local version use PostgreSQL database from demo website for synchronization of data.

For initial installation:

```bash
  docker-compose up --build
```

For next run 

```bash
  docker-compose up
```
    
## Author

- [Aimurat Zhetkizgenov @Aimurat1](https://github.com/Aimurat1/)


## Tech Stack

**Client:** Svelte, SvelteKit, TailwindCSS

**Server:** Django, Django Rest Framework

**Database:** PostgreSQL

**Scheduled tasks:** Celery, Celery Beat (for dynamic parsing) + Redis
 

## Features

- Dynamic parsing from Tengrinews every 30 minutes
- Sorting by tags of each article
- Responsive interface
- Search of news by keywords
- All-in-one docker container



## Screenshots

Main Page:
![Main page](https://i.imgur.com/9rIDUrc.png)

News Page:
![News page](https://i.imgur.com/PIU4c43.png)

Single Page
![Single page](https://i.imgur.com/B3Oc6V3.png)
