# Flask API Boilerplate
Flask REST API pre-configured with Flask-SQLAlchemy, Flask-Serializer & Logging. This will get you up and running with CRUD operations quickly. Use this starter, boilerplate for all your new Flask projects.

## Requirements
- Python 3
- python3-virtualenv
- python3-pip

## Quick Start
1. Clone the repo
    ```bash
    git clone https://github.com/WMRamadan/flask-api-biolerplate
    cd flask-api-biolerplate
    ```

2. Initialize and activate a virtual environment:
    ```bash
    virtualenv env
    source env/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

4. Run the development server:
    ```bash
    python3 app.py
    ```

5. View the api at http://localhost:5000

6. Perform CRUD Operations:

    Create Note:
    ```bash
    curl -X POST http://localhost:5000/notes -H 'Content-Type: application/json' -d '{"note": "This is a note"}'
    ```

    Get all Notes:
    ```bash
    curl -X GET http://localhost:5000/notes
    ```

    Get Note by ID:
    ```bash
    curl -X GET http://localhost:5000/note/<note_id>
    ```

    Delete Note by ID:
    ```bash
    curl -X DELETE http://localhost:5000/note/<note_id>
    ```

    Update Note by ID:
    ```bash
    curl -X PUT http://localhost:5000/note/<note_id> -d '{"note": "This is an updated note"}'
    ```

