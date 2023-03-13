# Docker Test

Containorise a Python application using Docker.

**To run Python API application locally:**

1. `uvicorn main:app --reload`

**To run docker container:**

1. `docker-compose up` - to build and run (use for changes too)
2. or detached mode: `docker-compose up -d`
   1. then stop using `docker-compose down`
