# Soundify (Synthetic Data Version) 🎧

**LLM-Powered Music Recommendation System – Synthetic Prototype**

Soundify is a prototype full-stack music recommendation system that uses large language models (LLMs) to generate song suggestions based on simulated user behavior and preferences. Built for safe development and testing, this version uses **synthetic data** to validate the system architecture and prompt engineering before integrating with real-world APIs.

---

## 🧪 Purpose

This version was designed as a **testing environment** for:

* Verifying system logic and LLM response structure
* Testing frontend-backend communication
* Engineering prompts for song recommendation tasks
* Displaying structured music recommendations using mock listening data

---

## ✨ Features

### Frontend:

* Built with **React.js**
* Displays LLM-generated song recommendations
* Simulates filter and search-based discovery
* Real-time updates with Redux Toolkit
* Clean, structured UI with Ant Design components

### Backend:

* Built with **Django**
* Receives synthetic user listening histories and request parameters
* Constructs prompts for OpenAI’s **GPT-4**
* Returns structured JSON responses with recommended songs

---

## 🧰 Tech Stack

### Frontend:

* React.js
* Redux Toolkit
* Axios (for API requests)
* Ant Design

### Backend:

* Django
* Django REST Framework
* Python 3.9+
* OpenAI GPT-4 API

---

## 🧑‍🔬 Synthetic Dataset

* **1,000 synthetic songs**:

  * Attributes: `track_name`, `artist_name`, `genre`, `mood`, `popularity_score`
* **100 synthetic users**:

  * Each user has a simulated listening history
  * Listening history includes time-of-day context for morning/afternoon/evening recommendations

---

## 🔄 User Flow (Simulated)

1. Select a synthetic user profile and simulate a login
2. The frontend sends the user’s mock listening history and time of day to the backend
3. Backend formats the input as a prompt and sends it to the GPT-4 API
4. LLM returns 20 recommended songs in structured JSON
5. Frontend displays results with song names, artists, genres, and mock artwork

---

## 📡 API Endpoints

### `POST /recommendations`

Generate 20 song recommendations based on synthetic listening history and time of day.

**Request:**

```json
{
  "time_of_day": "Evening",
  "listening_history": [
    {"track_name": "Fake Love", "artist_name": "Mock Artist"},
    {"track_name": "Imaginary", "artist_name": "Synth Pop"}
  ]
}
```

**Response:**

```json
{
  "recommendations": [
    {"track_name": "Dreamwave", "artist_name": "Mock Artist", "genre": "Pop"},
    {"track_name": "Skyline", "artist_name": "Chill Beats", "genre": "Lo-fi"}
  ]
}
```

---

## 🔍 Filtered and Natural Language Queries

* You can test **genre/mood filters** (e.g., `"Jazz"`, `"Energetic"`)
* You can test **free-form prompts** like:

  > *"Give me some calm music to focus with."*

LLM generates diverse and context-aware responses even with simulated input.

---

## 🎯 Goals of This Version

✅ Validate system architecture
✅ Test LLM response quality and format
✅ Develop robust prompting strategies
✅ Prototype frontend and backend interaction
✅ Avoid external API limits during early testing

---

## 🛠 Future Integration

This prototype serves as the foundation for integrating real user data via Spotify or other platforms. Once system reliability was validated using synthetic data, it was upgraded to a real-time, production-ready version.

---

## Setup Instructions

### Frontend Setup (React.js)

To set up the **frontend** and run the React.js application, follow these steps:

1. **Install Dependencies:**
   Navigate to the **frontend** directory and run the following command to install the necessary node modules:

   ```bash
   npm install
   ```

2. **Start the Application:**
   Once the dependencies are installed, run the following command to start the React application:

   ```bash
   npm start
   ```

   This will start the React development server, and you can view the app in your browser at `http://localhost:3000`.

---

### Backend Setup (Django)

To set up the **backend** and run the Django server, follow these steps:

1. **Navigate to the Backend Directory:**
   Go to the **backend** directory where the `manage.py` file is located.

2. **Configure Python Interpreter:**
   Ensure that your Python interpreter is configured to the correct version (Python 3.9+). If you're using an IDE like PyCharm, you can set the interpreter there.

3. **Create a Virtual Environment:**
   It's a good practice to use a virtual environment. Create one by running:

   ```bash
   python -m venv venv
   ```

   Then activate it:

  * On **Windows**:

    ```bash
    venv\Scripts\activate
    ```

  * On **MacOS/Linux**:

    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies:**
   Install the required libraries from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Backend:**
   To start the Django development server, run the following command:

   ```bash
   python manage.py runserver
   ```

   The backend server will now be running at `http://127.0.0.1:8000`.

---

Now, the frontend and backend should be running, and you can interact with the synthetic data-driven music recommendation system!
