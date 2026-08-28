# Akhil's Django Portfolio and Engineering Blog

[![Django CI](https://github.com/akhil15123/Mypersonalportfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/akhil15123/Mypersonalportfolio/actions/workflows/ci.yml)

A Python/Django portfolio and technical blog for presenting AI, data-engineering, and software projects. It includes database-backed posts, categories, search, project pages, documentation links, and a configurable contact workflow.

## Features

- Blog posts with categories, slugs, images, and pagination
- Search across titles and content
- Portfolio, about, and documentation pages
- Django Admin content management
- Tailwind-powered responsive interface
- Console email locally and environment-based SMTP in production
- Automated Django checks and view tests

## Local setup

```bash
git clone https://github.com/akhil15123/Mypersonalportfolio.git
cd Mypersonalportfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000`.

To rebuild Tailwind styles:

```bash
cd theme/static_src
npm ci
npm run build
```

## Configuration

Application secrets, allowed hosts, and SMTP credentials are read from environment variables. Use `.env.example` as a deployment checklist; never commit real credentials.

## Verify

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```
