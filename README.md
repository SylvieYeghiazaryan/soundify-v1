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
