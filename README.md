# Backend-Projects

## Expense Tracker

- Manage expenses through a CLI Expense Tracker by passing the details as CLI arguments
- Usage : `python expense-tracker.py <argument>`
- Commands:
    -  `python expense_tracker.py add --description "Lunch" --amount 20`
    -  `python expense_tracker.py add --description "Dinner" --amount 10`
    -  `python expense_tracker.py list`
    -  `python expense_tracker.py summary`
    -  `python expense_tracker.py delete --id 2`
    -  `python expense_tracker.py summary --month 8`
    -  `python expense_tracker.py update --id 1 --amount 25`

- project URL : https://roadmap.sh/projects/expense-tracker

## Weather API with FastAPI + Redis Caching

This project is a **FastAPI** backend that fetches weather data from the [Visual Crossing API](https://www.visualcrossing.com/) and uses **Redis** to cache responses, reducing API calls and improving performance.

Features
- Fetch weather data for a given city.
- Cache results in **Redis** for 1 hour to avoid unnecessary API calls.
- Simple and fast REST API built with **FastAPI**.
- `.env` support for secure API key management.

Run command: `uvicorn weather-api:app --reload`


## GitHub User Activity
Using GitHub API to fetch user activity and display it in the terminal.

Run command:  `python github-events.py`

Project URL : https://roadmap.sh/projects/github-user-activity
