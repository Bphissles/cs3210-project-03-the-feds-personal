# Vue 3 + Python Application

A modern web application with a Vue 3 frontend using Bootstrap 5.3 and SASS, connected to a Python Flask backend API.

## Project Structure

```
vue-python-app/
├── backend/             # Python Flask backend
│   ├── app.py           # Main Flask application
│   └── requirements.txt # Python dependencies
└── frontend/            # Vue 3 frontend
    ├── public/          # Static assets
    ├── src/             # Vue source code
    │   ├── assets/      # Images and other assets
    │   ├── components/  # Vue components
    │   ├── router/      # Vue router
    │   ├── styles/      # SASS styles
    │   ├── views/       # Vue views
    │   └── App.vue      # Main application component
    ├── package.json     # Node.js dependencies
    └── vite.config.js   # Vue configuration
```

## Prerequisites

Before running this application, you need to have the following installed:

- **Node.js** (v14.x or later)
- **npm** (v6.x or later)
- **Python** (v3.8 or later)
- **pip** (Python package manager)

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Start the Flask server:
   ```
   python3 app.py
   ```
   The backend will run on http://localhost:5000

6. To shut down the Flask server:
   ```
   Press CTRL+C in the terminal
   ```

### Frontend Setup

The project includes a modern frontend built with Vue 3, Vite, Bootstrap 5.3, and SASS.

1. Navigate to the frontend directory:
   ```
   cd frontend-new
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the Vite development server:
   ```
   npm run dev
   ```
   The frontend will run on http://localhost:8080

## Using the Application

1. Open your browser and navigate to http://localhost:8080
2. Click the "Fetch Message from API" button to retrieve the "Hello World" message from the backend API

## API Endpoints

- `GET /api/hello`: Returns a JSON response with a "Hello World" message

## Development

### Frontend

- Vue 3 with Composition API and script setup syntax
- Vite for fast development and building
- Bootstrap 5.3 for styling
- SASS for custom styles
- Axios for API requests

### Backend

- Flask for the REST API
- Flask-CORS for handling Cross-Origin Resource Sharing

## Building for Production

### Frontend

```
cd frontend-new
npm run build
```

The built files will be in the `frontend-new/dist` directory.

### Backend

```
pip install gunicorn
gunicorn app:app
```
