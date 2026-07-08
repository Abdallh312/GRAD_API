# iVision Backend API 🚀

Welcome to the **iVision Backend API** repository. This project is a robust RESTful API built using Django and Django Rest Framework (DRF). It serves as the backend for the iVision system, designed to handle location tracking, accident and fire detection, servo motor angles, and image processing data.

---

## 👨‍💻 Developer
**Abdallah Shref (Abdallh312)**
- UI/UX Designer
- Backend Developer

---

## 🌟 Features
- **RESTful Endpoints:** Standardized GET, POST, PUT, PATCH, and DELETE operations.
- **Real-time Event Tracking:** Supports logging data such as GPS coordinates (longitude/latitude).
- **Hazard Detection:** Flags for `is_accident` and `is_fire` to monitor critical events.
- **Hardware Integration Data:** Stores `servo_angle` and `target_angle` to interface with hardware components.
- **Image Handling:** Accepts base64 encoded images directly through the API.
- **Predictions:** Stores machine learning prediction flags (`predict`) and textual descriptions (`description`).

---

## 🛠️ Technology Stack
- **Framework:** [Django 5.1](https://www.djangoproject.com/) & [Django Rest Framework 3.15](https://www.django-rest-framework.org/)
- **Database:** PostgreSQL (via `psycopg2-binary`) / SQLite (for local development)
- **Caching & Message Broker:** Redis (`redis`, `django-redis`)
- **Server:** Gunicorn & Whitenoise for static file serving
- **Documentation:** Swagger/OpenAPI (via `drf-yasg`)

---

## 🗄️ Database Model (`delocation`)

The core model of this API is `delocation`, which stores the following fields:
- `longitude` (Float): GPS Longitude
- `latitude` (Float): GPS Latitude
- `images` (Text): Base64 encoded image data
- `is_accident` (Boolean): Flag for accident detection
- `is_fire` (Boolean): Flag for fire detection
- `servo_angle` (Float): Current servo motor angle
- `target_angle` (Float): Target servo motor angle
- `predict` (Boolean): ML prediction status
- `description` (Text): Additional details or logs

---

## 🚀 API Endpoints

### 1. List and Create
`GET /api/`
- Retrieves a list of all data points ordered by their primary key.

`POST /api/`
- Creates a new data point. 
- **Required Body:** JSON containing the fields mentioned in the database model.

### 2. Retrieve, Update, and Delete
`GET /api/<pk>/`
- Retrieves the details of a specific record by its Primary Key (pk).

`PUT /api/<pk>/`
- Updates the complete record of a specific pk.

`PATCH /api/<pk>/`
- Partially updates a specific record.

`DELETE /api/<pk>/`
- Deletes a specific record.

---

## ⚙️ Installation & Setup (Local Environment)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abdallh312/GRAD_API.git
   cd iVision-backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

---

## ☁️ Deployment
This project is configured for deployment on platforms like Vercel and Heroku (includes `vercel.json`, `Procfile`, and `runtime.txt`).

---
*Built with ❤️ by Abdallh312*
