# SUS-ENE-TRAD Backend

A FastAPI-powered backend service for user authentication and management.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/<your-username>/sus-ene-trad.git
cd sus-ene-trad
```

Create a virtual environment:

```bash
python -m venv venv
```

For Windows:

```bash
venv\Scripts\activate
```

For Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory with the following contents:

```env
ENVIRONMENT=dev
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
```

Start the application:

```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for API testing.

## Database Migrations

Generate a new migration:

```bash
alembic revision --autogenerate -m "migration message"
```

Apply the migration:

```bash
alembic upgrade head
```