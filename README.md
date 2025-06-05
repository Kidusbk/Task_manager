# Django To-Do API

A simple To-Do List API built with Django and Django REST Framework.

## Features

*   **GET /api/tasks/** — Return all tasks
*   **POST /api/tasks/** — Add a new task
*   **GET /api/tasks/:id/** — Retrieve a specific task
*   **PUT /api/tasks/:id/** — Mark a task as completed (or update other fields)
*   **DELETE /api/tasks/:id/** — Delete a task
*   Simple HTML page at the root URL (`/`) indicating the API is running.

## API Endpoints

*   **`GET /api/tasks/`**
    *   Returns a list of all tasks.
*   **`POST /api/tasks/`**
    *   Adds a new task.
    *   Request Body (JSON):
        ```json
        {
            "title": "My New Task",
            "description": "Optional details about the task."
        }
        ```
*   **`GET /api/tasks/<id>/`**
    *   Retrieves a specific task by its ID.
*   **`PUT /api/tasks/<id>/`**
    *   Updates an existing task. Can be used to mark a task as completed.
    *   Request Body (JSON):
        ```json
        {
            "title": "Updated Task Title",
            "description": "Updated description",
            "completed": true
        }
        ```
*   **`PATCH /api/tasks/<id>/`** (Also supported for partial updates)
    *   Partially updates an existing task. Useful for just changing one field, like `completed`.
    *   Request Body (JSON):
        ```json
        {
            "completed": true
        }
        ```
*   **`DELETE /api/tasks/<id>/`**
    *   Deletes a specific task by its ID.
