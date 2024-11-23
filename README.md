BookNest
BookNest is a Django-based web application designed for managing books, categories, and their rental or sale statuses. The application allows users to add, update, delete, and filter books based on their category and status. Additionally, it provides features for managing categories and viewing statistics about books, including total books, rental status, and revenue details.

Features
CRUD Operations:
Create, Read, Update, and Delete books.
Add and manage book categories.
Filtering and Search:
Filter books by status: Available, Rented, or Sold.
Search for books by title.
Revenue Tracking:
View cumulative revenue from rented and sold books.
User Management:
Displays basic user information (like username).
Responsive Design:
Fully responsive layout for desktop and mobile devices.
Technologies Used
Backend: Django
Frontend: HTML, CSS (Bootstrap), JavaScript, jQuery, Chart.js
Database: SQLite (default, configurable to other databases)
Libraries: Font Awesome, AdminLTE
Setup and Installation
Clone the Repository
To set up the project locally, follow these steps:

Clone the repository:
bash
Copy code
git clone <repository_url>
cd BookNest
Install Dependencies
Install the required dependencies using pip:
bash
Copy code
pip install -r requirements.txt
Database Setup
Apply the migrations to set up the database:
bash
Copy code
python manage.py migrate
Create Superuser
Create a superuser to access the Django admin panel:
bash
Copy code
python manage.py createsuperuser
Run the Development Server
Start the development server:
bash
Copy code
python manage.py runserver
Your app will be accessible at http://127.0.0.1:8000/.

Directory Structure
lms_app/: Main application containing models, views, and forms.
templates/: HTML files for the frontend views.
base.html: The main template file, used across all pages.
index.html: Homepage with a dashboard of books and categories.
books.html: Displays a list of books with options to search and filter.
update.html: Page for editing a book's details.
delete.html: Confirmation page for deleting a book.
sidebar.html: Sidebar navigation with links to different book management sections.
footer.html: Footer with copyright and social media links.
nav.html: Navigation bar with links to home and search functionality.
static/: Contains static files like images, CSS, and JavaScript.
media/: Stores uploaded media files (e.g., book and author photos).
Admin Panel
Access the Django admin panel at http://127.0.0.1:8000/admin/ to manage books, categories, and other content.

