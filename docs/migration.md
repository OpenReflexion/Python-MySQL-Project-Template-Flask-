# Project Title

## Introduction

This project is a Flask-based API that uses SQLAlchemy for database management and Flask-Migrate for handling database migrations. This guide will walk you through the steps to set up and manage database migrations in this project.

## Prerequisites

- Python 3.6+
- Virtual environment setup
- MySQL database (asynchronous for application operations and synchronous for migrations)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory of the project and add the following environment variables:

   ```env
   ENVIRONMENT=development
   SECRET_KEY=your_secret_key

   # Database config
   DATABASE_URL=mysql+aiomysql://username:password@host:port/database_name
   SYNC_DATABASE_URL=mysql+pymysql://username:password@host:port/database_name

   # JWT config
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   GENERATED_CODE_EXPIRE_MINUTES=15

   # SSO Google auth
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret

   # SMTP Config
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=465
   EMAIL_USERNAME=your-email@example.com
   EMAIL_PASSWORD=your-email-password
   EMAIL_FROM=your-email@example.com

   # SMTP Mailtrap (for testing)
   MAILTRAP_USERNAME=your_mailtrap_username
   MAILTRAP_PASSWORD=your_mailtrap_password
   ```

2. Ensure that the database is running and accessible with the credentials provided in the `.env` file.

## Database Migrations

Flask-Migrate is used to handle database migrations. Follow these steps to manage migrations:

### Initialize Migrations

Before running any migration commands, make sure the application environment is set up correctly:

1. Ensure the `FLASK_APP` environment variable is set to `main.py`:

   ```bash
   export FLASK_APP=main.py  # On Windows use `set FLASK_APP=main.py`
   ```

2. Initialize the migration directory:

   ```bash
   flask db init
   ```

### Create a Migration

Whenever you make changes to your SQLAlchemy models, create a new migration script:

   ```bash
   flask db migrate -m "Description of the changes"
   ```

### Apply the Migration

Apply the migration to the database:

   ```bash
   flask db upgrade
   ```

### View Available Commands

To see all available Flask-Migrate commands, run:

   ```bash
   flask db --help
   ```

## Running the Application

Start the Flask application:

   ```bash
   flask run
   ```

## Troubleshooting

If you encounter issues with migrations or the database connection, check the following:

- Ensure the database server is running and accessible.
- Verify the credentials and database URL in the `.env` file.
- Check the application logs for error messages.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
