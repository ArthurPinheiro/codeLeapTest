# Career API

The **Career API** is a simple RESTful web service built with **Django** and **Django REST Framework (DRF)**. It allows full CRUD operations on career data, such as username, job title, and content/stack.

The API also includes validation logic to prevent updating immutable fields like `username`, `id` and `created_datetime`.

---

## 🧠 Features

- Create new career records (`POST`)
- Retrieve all careers (`GET`)
- Partially update career records (`PATCH`)
- Delete a career (`DELETE`)
- Validation: Prevents updates to `username`, `id` and `created_datetime` via `PATCH`

---

## 📌 API Endpoints

### 🔹 Create a new career

**Body JSON:**
```json
{
  "username": "Arthur",
  "title": "Backend Developer",
  "content": "Python"
}
```

#### Response 201 Created

### 🔹 List all careers

GET /careers/

#### Response: 200 OK

### 🔹 Partially update a career

PATCH /careers/<id>/
**Body JSON:**
```json
{
  "title": "Software Engineer",
  "content": "Python"
}
```

🚫 Immutable fields: username, id, created_datetime

```json
{
  "created_datetime": "2025-05-04"
}

```

#### Response: 400 Bad Request

### 🔹 Delete a career

DELETE /careers/<id>/

#### Response: 204 No content

🛠️ How to Run the Project
🔹 Requirements
* Docker
* Docker Compose

```json
docker-compose up --build
```

Access: http://localhost:8000/careers/

✅ Running the Tests 
```
pytest
```
