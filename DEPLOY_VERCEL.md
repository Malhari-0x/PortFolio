# Deploy Django Portfolio to Vercel

## 1. Push this project to GitHub

Vercel will deploy from your GitHub repo.

## 2. Create a new Vercel project

- In Vercel Dashboard, click **Add New... > Project**
- Import this repository
- Keep root directory as project root

## 3. Add environment variables in Vercel

Add these in **Project Settings > Environment Variables**:

- `SECRET_KEY`: long random string
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: your custom domain(s), comma separated (optional)
- `CSRF_TRUSTED_ORIGINS`: full https origins, comma separated (optional)

Example values:

- `ALLOWED_HOSTS`: `myportfolio.com,www.myportfolio.com`
- `CSRF_TRUSTED_ORIGINS`: `https://myportfolio.com,https://www.myportfolio.com`

## 4. Deploy

Trigger deploy from Vercel UI, or push a new commit to `main`.

## Notes

- Static files are collected during build using `build_files.sh`.
- This setup uses SQLite and is suitable for mostly static/portfolio pages.
- If you add features that write to database in production, move to Postgres (e.g., Neon/Supabase) and set Django DB config from `DATABASE_URL`.
