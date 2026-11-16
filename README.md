# AirBnB Clone v2

A Python implementation of core components of an AirBnB clone.

## Technologies

- Python 3
- Flask
- SQLAlchemy
- MySQL
- HTML5 and CSS3
- Fabric
- Nginx
- Puppet
- Bash

## Getting Started

### Requirements

- Python 3
- MySQL (required for database-backed storage)
- Required Python packages: Flask, SQLAlchemy, and a MySQL database driver.
- Fabric 1.x for the deployment scripts.

### Installation

Clone the repository:

```bash
git clone https://github.com/adoraa/AirBnB_clone_v2.git
```

Navigate to the project directory:

```bash
cd AirBnB_clone_v2
```

Install the Python dependencies:

```bash
pip install Flask SQLAlchemy mysqlclient
```

### Running the Console

Start the interactive console:

```bash
./console.py
```

The console supports the following commands:

| Command | Description |
|---|---|
| `create` | Creates a new instance of a model |
| `show` | Displays a specific instance |
| `all` | Lists all instances or instances of a specified class |
| `update` | Updates an instance's attributes |
| `destroy` | Deletes an instance |
| `count` | Counts instances of a specified class |
| `quit` | Exits the console |

Example:

```text
(hbnb) create User
(hbnb) all User
(hbnb) quit
```

### Storage Configuration

The project supports two storage engines.

**File storage**

File storage is used by default when `HBNB_TYPE_STORAGE` is not set to `db`. Objects are serialized to `file.json`.

**Database storage**

To use MySQL storage, configure the following environment variables:

```bash
export HBNB_TYPE_STORAGE=db
export HBNB_MYSQL_USER=your_mysql_user
export HBNB_MYSQL_PWD=your_mysql_password
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=your_database_name
```

The repository includes SQL scripts for setting up development and test databases.

## Static Webpages

The `web_static/` directory contains the HTML and CSS files used to build an AirBnB-inspired interface.

The pages progressively introduce layout elements, filters, property listings, and styling.

## Deployment Scripts

The repository includes scripts for automating static website deployment:

- `0-setup_web_static.sh` – Installs and configures Nginx.
- `1-pack_web_static.py` – Creates a compressed archive of the static website.
- `2-do_deploy_web_static.py` – Transfers and deploys an archive to configured servers.
- `3-deploy_web_static.py` – Combines packaging and deployment operations.
- `100-clean_web_static.py` – Removes older deployment archives.
- `101-setup_web_static.pp` – Defines Nginx and directory configuration using Puppet.

These scripts are deployment exercises and require environment-specific configuration before use.

## Project Structure

| File or Directory | Description |
|---|---|
| `console.py` | Interactive command-line console |
| `models/` | Base model and application data models |
| `models/engine/` | File and database storage implementations |
| `tests/` | Unit tests for the console, models, and storage |
| `web_flask/` | Flask applications and HTML templates |
| `web_static/` | Static HTML pages, stylesheets, and images |
| `setup_mysql_dev.sql` | Development database setup |
| `setup_mysql_test.sql` | Test database setup |
| `versions/` | Generated static website archives |
| `0-setup_web_static.sh` | Nginx setup script |
| `1-pack_web_static.py` | Static website packaging script |
