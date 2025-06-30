# python-practice

This project is a practice environment for building a Django-based recipe application, containerized with Docker for easy development and deployment.

## Project Structure

- `app/` - Contains the Django project and application code.
- `Dockerfile` - Builds the Docker image for the Django app.
- `docker-compose.yml` - Orchestrates the Docker container for development.
- `requirements.txt` - Lists main Python dependencies for the project.
- `requirements.dev.txt` - Lists development-only dependencies (e.g., linting tools).

## Requirements

- Docker
- Docker Compose

## Python Dependencies

Main dependencies are listed in `requirements.txt`:

```
Django>=5.2.3
Djangorestframework>=3.16.0
```

Development dependencies (for code linting, etc.) are in `requirements.dev.txt`:

```
flake8>=7.3.0
```

## Docker Usage

### Build and Run with Docker Compose

1. Build and start the app:
   ```sh
   docker-compose up --build
   ```
2. The Django development server will be available at [http://localhost:8000](http://localhost:8000).

### Dockerfile Details
- Uses Python 3.12 on Alpine Linux for a small image size.
- Installs dependencies in a virtual environment at `/py`.
- Adds a non-root user (`django-user`) for security.
- Sets up the environment for both production and development (with `DEV` build arg).

### Development
- Code changes in the `app/` directory are reflected live in the running container (thanks to the volume mount in `docker-compose.yml`).
- Lint your code with `flake8` (installed in development mode).

## Next Steps
- Start building your Django recipe app inside the `app/` directory.
- Add more dependencies as needed to `requirements.txt` or `requirements.dev.txt`.
- Update this README as your project evolves.

## Continuous Integration (GitHub Actions)

This project uses a GitHub Actions workflow defined in `.github/workflows/checks.yml` to automate testing and linting on every push.

**Workflow steps:**
- Logs in to Docker Hub (using repository secrets)
- Checks out the code
- Builds the Docker containers with `docker-compose build`
- Runs Django tests with `python manage.py test`
- Runs code linting with `flake8`

This ensures that all code pushed to the repository passes tests and style checks automatically.