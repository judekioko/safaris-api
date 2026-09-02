# Safaris Best Choice Kenya — API

Django + Django REST Framework backend for the [tourisim-](https://github.com/judekioko/tourisim-) frontend (hosted on GitHub Pages). Provides real user accounts, and stores bookings and contact messages in a database, viewable in the Django admin.

## Endpoints

All under `/api/`:

| Method | Path                  | Auth required | Purpose |
|--------|-----------------------|----------------|---------|
| POST   | `/api/auth/register/` | No             | Create an account. Body: `{email, password, full_name}`. Returns `{user, access, refresh}`. |
| POST   | `/api/auth/login/`    | No             | Log in. Body: `{username, password}` — **`username` must be the account's email** (the account's username is set to its email at registration). Returns `{access, refresh}`. |
| POST   | `/api/auth/token/refresh/` | No        | Body: `{refresh}`. Returns a new `access` token. |
| GET    | `/api/auth/me/`       | Yes (Bearer)   | Returns the signed-in user's `{id, email, first_name}`. |
| POST   | `/api/bookings/`      | No (optional)  | Create a booking. If an `Authorization: Bearer <access>` header is sent, the booking is linked to that user; otherwise it's a guest booking. |
| POST   | `/api/messages/`      | No             | Create a contact-form message. |

Bookings and messages are **not** readable through the API by design — view them in `/admin/` instead, so a public site visitor can never list other people's data.

## Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # edit values as needed; defaults work for local dev
python manage.py migrate
python manage.py createsuperuser   # to access /admin/
python manage.py runserver
```

The API will be at `http://127.0.0.1:8000/api/`, admin at `http://127.0.0.1:8000/admin/`.

## Deploying (Render, free tier)

1. Push this repo to GitHub (already done if you're reading this from the repo).
2. On [render.com](https://render.com), **New +** → **Web Service** → connect this repo.
3. Settings:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command:** `python manage.py migrate && gunicorn config.wsgi`
   - **Environment variables** (Render dashboard → Environment): set `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=<your-service>.onrender.com`, `CORS_ALLOWED_ORIGINS=https://judekioko.github.io`.
4. Add a free **PostgreSQL** database in Render (New + → PostgreSQL), then copy its "Internal Database URL" into this web service's `DATABASE_URL` environment variable.
5. Deploy. Render gives you a URL like `https://safaris-api.onrender.com` — that's your `API_BASE` for the frontend.
6. In the `tourisim-` repo, set `API_BASE` in `assets/js/config.js` to that URL and push.

Note: Render's free tier spins the service down after ~15 minutes of inactivity, so the first request after idle time takes 30-60s to "wake up" — this only affects response time, not correctness.

(Railway, Fly.io, and PythonAnywhere work similarly — the constants above are the only pieces specific to Render.)

## Creating an admin user in production

After the first deploy, run once (Render: Shell tab on the service):

```bash
python manage.py createsuperuser
```

Then sign in at `https://<your-service>/admin/` to browse bookings and messages.
