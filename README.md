BookNest

BookNest is a web application built with Django that allows users to manage books, categories, and their rental or sale statuses. The application features CRUD operations, a dynamic filtering system, revenue tracking, and a user-friendly interface to add, update, and manage books.

Features

Book Management:

Add new books with details like title, author, price, rental price, status, and category.
Edit and delete existing books.
Display book details such as title, status (Sold, Rented, Available), price, and category.

Category Management:

Create and manage book categories.
Each book can be assigned to a specific category.

Filtering and Search:

Search for books by title.
Filter books by their status (Sold, Rented, Available) or category.

Revenue Tracking:

Display cumulative revenue from rented and sold books.
Interactive Charts:

Use Chart.js to display bar and pie charts visualizing revenue and book status statistics.

Responsive Design:

Fully responsive and mobile-friendly layout.

Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS (Bootstrap), JavaScript, jQuery, Chart.js
Database: SQLite (default, configurable to other databases such as PostgreSQL)
Libraries: Font Awesome, AdminLTE
Installation & Setup
Follow these steps to get the project running on your local machine:

1. Clone the Repository
Clone the repository to your local machine:


git clone https://github.com/yourusername/BookNest.git
cd BookNest

2. Set Up a Virtual Environment
Create a virtual environment to manage dependencies:


python -m venv venv
Activate the virtual environment:

Windows:

venv\Scripts\activate
Mac/Linux:

source venv/bin/activate

3. Install Dependencies
Install the required dependencies:


pip install -r requirements.txt
4. Set Up the Database
Run the migrations to set up the database:


python manage.py makemigrations
python manage.py migrate

5. Create a Superuser
Create a superuser account to access the Django admin panel:


python manage.py createsuperuser

6. Run the Development Server
Start the Django development server:

python manage.py runserver
Your app will be accessible at http://127.0.0.1:8000/.

Directory Structure
lms_app/: The main application that contains models, views, forms, and templates for managing books and categories.

models.py: Defines the Book and Category models.
views.py: Contains views for handling book management, category management, and filtering.
forms.py: Contains forms for creating and editing books and categories.
admin.py: Registers models for the Django admin panel.
templates/: Contains HTML templates for rendering views.

base.html: Base template with the overall structure (navbar, sidebar, footer).
index.html: Homepage displaying book statistics, revenue, and forms for adding new books and categories.
books.html: Displays a list of books with search and filter options.
update.html: Form for updating a book’s details.
delete.html: Confirmation page for deleting a book.
sidebar.html: Sidebar navigation for the app.
footer.html: Footer with copyright and social media links.
nav.html: Navigation bar with links to the homepage and search functionality.
static/: Contains static files such as CSS, JavaScript, and images.

css/: Custom styles and external libraries (Bootstrap, AdminLTE).
js/: JavaScript files for handling dynamic content and interactions.
images/: Image files for book covers, user avatars, etc.
media/: Stores uploaded media files like book photos and author photos.

Admin Panel
Access the Django admin panel at http://127.0.0.1:8000/admin/ to manage books, categories, and other content.

Admin username: The one you set up when creating the superuser.
Admin password: The password you chose during the superuser creation.
Functionality Breakdown
1. Home Page (index.html)
Displays overall statistics, including:
Total number of books.
Cumulative revenue from rented and sold books.
Add new books and categories via forms.
2. Books List Page (books.html)
Displays all books with options to:
Search by book title.
Filter by book status (Sold, Rented, Available).
Edit or delete books.
3. Update Book (update.html)
Provides a form for updating an existing book's details, such as title, author, price, and rental price.
4. Delete Book (delete.html)
Confirms the deletion of a book with a confirmation prompt before permanently removing it from the database.
5. Sidebar and Navigation
The sidebar includes links for managing books, categories, and filtering by status.
The navigation bar provides easy access to the homepage and search functionality.
JavaScript and Interactivity
Dynamic Filtering: Books can be filtered by category or status (Available, Rented, Sold) using JavaScript/jQuery.
Revenue Calculation: Automatically calculates and displays total rental and sales revenue.
Chart.js: Used to generate pie and bar charts visualizing book statistics, such as rental and sales profit.
Deployment
Prepare for Production
Set DEBUG = False in settings.py.
Configure the database (e.g., PostgreSQL) for production.
Set up static file handling (e.g., using Amazon S3 or DigitalOcean Spaces).
Deploy the application to a platform such as Heroku, DigitalOcean, or AWS.
