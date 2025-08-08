# Hostinator - Refactored Flask Application

## Overview
This is a refactored version of the Hostinator deployment management system, restructured following Python best practices with proper separation of concerns.

## Project Structure

\`\`\`
hostinator/
├── app.py                 # Main application entry point
├── config.py             # Configuration management
├── database.py           # Database connection and management
├── ssh_manager.py        # SSH connection handling
├── deployment_service.py # Deployment logic
├── marketplace_data.py   # Marketplace app definitions
├── utils.py              # Utility functions
├── routes/               # Route blueprints
│   ├── auth.py          # Authentication routes
│   ├── dashboard.py     # Dashboard routes
│   ├── marketplace.py   # Marketplace routes
│   ├── deployments.py   # Deployment management routes
│   └── health.py        # Health check routes
├── templates/           # HTML templates (unchanged)
├── static/             # CSS and static files (unchanged)
└── requirements.txt    # Python dependencies
\`\`\`

## Key Improvements

### 1. **Modular Architecture**
- Separated concerns into logical modules
- Used Flask blueprints for route organization
- Created service classes for business logic

### 2. **Configuration Management**
- Centralized configuration in `config.py`
- Environment-based configuration support
- Secure credential handling

### 3. **Database Layer**
- Dedicated `DatabaseManager` class
- Connection pooling management
- Query execution with proper error handling

### 4. **Service Layer**
- `DeploymentService` for deployment operations
- `SSHManager` for remote server communication
- Clear separation of business logic

### 5. **Route Organization**
- Blueprints for different functional areas
- Consistent authentication decorators
- Proper error handling and logging

## Installation & Setup

1. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. **Set up environment variables:**
   Create a `.env` file with your configuration:
   \`\`\`
   DB_HOST=your_db_host
   DB_PORT=3306
   DB_ROOT_USER=your_db_user
   DB_ROOT_PASSWORD=your_db_password
   SECRET_KEY=your_secret_key
   \`\`\`

3. **Run the application:**
   \`\`\`bash
   python app.py
   \`\`\`

## Features Maintained

- ✅ All original functionality preserved
- ✅ HTML templates unchanged
- ✅ CSS styles unchanged
- ✅ Database schema unchanged
- ✅ API endpoints unchanged

## Benefits of Refactoring

1. **Maintainability**: Code is now organized into logical modules
2. **Testability**: Each component can be tested independently
3. **Scalability**: Easy to add new features without affecting existing code
4. **Readability**: Clear separation of concerns makes code easier to understand
5. **Reusability**: Services can be reused across different parts of the application

## Running the Application

The application will start on `http://localhost:5000` with the same functionality as before, but now with a much cleaner and more maintainable codebase.

Default login credentials:
- Username: `admin`
- Password: `admin`
