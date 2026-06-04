
# CST8919 Lab 1 – Flask Authentication with Auth0

## Overview

This project demonstrates how to integrate Auth0 authentication into a Flask web application.

Features:

* Login with Auth0
* Logout with Auth0
* Protected route (/protected)
* Session-based authentication

## Requirements

* Python 3.x
* Auth0 Account
* Flask
* Authlib
* Python-Dotenv

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd CST8919-Lab1
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
AUTH0_DOMAIN=YOUR_AUTH0_DOMAIN
AUTH0_CLIENT_ID=YOUR_CLIENT_ID
AUTH0_CLIENT_SECRET=YOUR_CLIENT_SECRET
APP_SECRET_KEY=YOUR_SECRET_KEY
```

## Running the Application

```bash
python app.py
```

Open:

http://localhost:3000

## Features Implemented

* Auth0 Login
* Auth0 Logout
* Protected Page
* Redirect unauthenticated users to login

## Demo Video

YouTube Link:
https://youtu.be/ghtllSDxOD4

## What I Learned

* How OAuth/OpenID Connect authentication works
* How Auth0 integrates with Flask
* How to protect routes using session authentication
* How to manage user login and logout securely
=======
# lab1-cst8919
>>>>>>> 14e8770bc1c975bef7df632b172df52bdc1be932
