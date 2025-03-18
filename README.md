# Where Is My Money

## Project Overview

"Where Is My Money" is a financial tracking application designed to help users manage their expenses efficiently.

## Repository Structure

- **api** - Backend powered by FastAPI (Python)
- **app** - Frontend built with Remix

## Setup API Local Development Environment

### 1. Set Up Virtual Environment

Run the following commands in the root directory:

```sh
python -m venv ./api/venv
source ./api/venv/bin/activate  # On macOS/Linux
./api/venv/Scripts/activate     # On Windows
```

### 2. Install Dependencies

```sh
pip install -r ./api/requirements.txt
```

### 3. Create Environment File

Create a `.env` file in the `api` directory:

```sh
touch ./api/.env
```

Add the following variables to the `.env` file:

```
DEV_MODE=True
```

### 4. Start Development Server

Ensure the virtual environment is activated, then run:

```sh
cd api && fastapi dev
```

## Stopping Development

To deactivate the virtual environment, run:

```sh
deactivate
```

Model Changes with Alembic

Once updated models, run

```sh
# Generate migration
alembic revision --autogenerate -m "description of changes"

# Apply migration
alembic upgrade head
```

### todo

category
subscription
shortcut

stat
