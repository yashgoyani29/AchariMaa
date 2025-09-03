# AchariMaa - Django Web Application

A Django-based web application with user profile management and media handling capabilities.

## Project Structure

```
pickle_pro/
├── manage.py                 # Django management script
├── create_migrations.py      # Custom migration creation script
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── media/                   # User uploaded media files
├── static/                  # Static files (CSS, JS, images)
├── templates/               # HTML templates
├── pickle_pro/              # Main Django project settings
└── userprofile/             # User profile Django app
```

## Features

- Django 5.1.7 framework
- User profile management
- Media file handling
- PostgreSQL database support (psycopg2-binary)
- Interactive Python shell with IPython
- Image processing with Pillow
- Development debugging with ipdb

## Requirements

- Python 3.12+
- PostgreSQL database
- Virtual environment (recommended)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd AchariMaa/acharimaa/pickle_pro
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
Configure your PostgreSQL database settings in `pickle_pro/settings.py`, then run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Dependencies

### Core Framework
- **Django 5.1.7** - Web framework
- **asgiref 3.9.1** - ASGI utilities for Django

### Database
- **psycopg2-binary 2.9.10** - PostgreSQL adapter

### Development Tools
- **ipython 9.4.0** - Enhanced interactive Python shell
- **ipdb 0.13.13** - IPython-enabled debugger
- **jedi 0.19.2** - Code completion library

### Utilities
- **Pillow 11.3.0** - Image processing
- **pytz 2025.2** - Timezone handling
- **sqlparse 0.5.3** - SQL parsing
- **colorama 0.4.6** - Cross-platform colored terminal text

## Development

### Running Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating Custom Migrations
Use the provided `create_migrations.py` script for custom migration creation.

### Static Files
```bash
python manage.py collectstatic
```

### Testing
```bash
python manage.py test
```

## Project Apps

### userprofile
Handles user profile management and related functionality.

## Media Files
User-uploaded media files are stored in the `media/` directory.

## Static Files
CSS, JavaScript, and image assets are stored in the `static/` directory.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

[Add your license information here]

## Support

[Add support/contact information here]
