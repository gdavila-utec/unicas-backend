# Unicas Backend

This is the backend for the Unicas project, built with Django and Supabase.

## Setup

1. Clone the repository:

   ```
   git clone <repository-url>
   cd unicas-backend
   ```

2. Install dependencies:

   ```
   poetry install
   ```

3. Set up Supabase:

   - Create a Supabase project at https://supabase.com
   - Copy the project URL and API key

4. Configure environment variables:

   - Copy the `.env.example` file to `.env`
   - Fill in the Supabase credentials in the `.env` file:
     ```
     SUPABASE_URL=your_supabase_project_url
     SUPABASE_KEY=your_supabase_api_key
     SUPABASE_DB_NAME=your_supabase_db_name
     SUPABASE_DB_USER=your_supabase_db_user
     SUPABASE_DB_PASSWORD=your_supabase_db_password
     SUPABASE_DB_HOST=your_supabase_db_host
     SUPABASE_DB_PORT=5432
     ```

5. Run migrations:

   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

The API will be available at `http://localhost:8000/`.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process
for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for
details.
