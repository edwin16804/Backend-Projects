## Weather API with FastAPI + Redis Caching

This project is a **FastAPI** backend that fetches weather data from the [Visual Crossing API](https://www.visualcrossing.com/) and uses **Redis** to cache responses, reducing API calls and improving performance.

Features
- Fetch weather data for a given city.
- Cache results in **Redis** for 1 hour to avoid unnecessary API calls.
- Simple and fast REST API built with **FastAPI**.
- `.env` support for secure API key management.

Run command: `uvicorn weather-api:app --reload`
