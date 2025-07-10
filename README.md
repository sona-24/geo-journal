# 🌍 GeoJournal API — A Location-Aware Serverless Journaling App

GeoJournal is a RESTful journaling API built with **FastAPI** and deployed **serverlessly** on **AWS Lambda** using **AWS SAM**. It lets users create geotagged journal entries, filter them by location, and auto-detect coordinates using IP.

> Ideal for travel logs, personal reflections, field research notes, and more.

---

## 🚀 Features

- ✍️ Create notes with title, content, tags
- 📍 Attach geolocation manually or auto-detect via IP
- 🌐 IP-based location fallback using `ipapi.co`
- 🔍 Filter notes by nearby radius (Haversine formula)
- 📄 RESTful endpoints with Swagger UI
- ☁️ Serverless deployment via AWS Lambda + API Gateway
- ⚙️ CI/CD enabled with GitHub Actions + AWS SAM

---

## 📦 Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Serverless**: AWS Lambda + API Gateway
- **Deployment**: AWS SAM CLI
- **CI/CD**: GitHub Actions

---

## 📁 Endpoints

| Method | Endpoint         | Description |
|--------|------------------|-------------|
| `POST` | `/notes`         | Create a new journal note (IP-based fallback) |
| `GET`  | `/notes`         | List all notes |
| `GET`  | `/notes/nearby`  | Get notes near a lat/lon within a radius (km) |

---

## 🧪 Example Note (POST `/notes`)

```json
{
  "title": "Hiking in Yosemite",
  "content": "Waterfalls were roaring today!",
  "tags": "hiking,nature,california"
}

## 🛠 CI/CD with GitHub Actions

This project includes a GitHub Actions workflow to enable **automatic deployment** to AWS Lambda using the AWS SAM CLI.

### ✅ What it does:

- Triggers on every push to `main`
- Builds your FastAPI app using `sam build`
- Deploys using `sam deploy` with pre-configured parameters

### 🗂 Workflow File: `.github/workflows/deploy.yml`

```yaml
name: Deploy to AWS Lambda

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install aws-sam-cli
        sam --version

    - name: Build app
      run: sam build

    - name: Deploy app
      run: sam deploy --no-confirm-changeset --no-fail-on-empty-changeset --stack-name geo-journal-api --capabilities CAPABILITY_IAM --region us-east-1
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

📦 How to Run Locally
python -m venv .venv
.venv\Scripts\activate  # or source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

☁️ How to Deploy with AWS SAM
sam build
sam deploy --guided
