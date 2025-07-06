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
