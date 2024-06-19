# Student affairs Website
## Features

- **Add New Student**: Users can add new students to the system. The student information includes ID, name, date of birth, GPA, gender, level, status (active/inactive), department, email, and mobile number.
- **Update Student Information**: Users can update existing student information. The department field is disabled to prevent editing.
- **Delete Student**: Users can delete existing student data through a delete button in the edit student data page. A confirmation dialogue ensures the action is deliberate.
- **Search Active Students**: Users can search for active students by name. Students with similar names and active status are displayed in a table.
- **Assign Department**: After searching, users can assign a department to a student through a specific page. The page includes student ID, name, a dropdown list for available departments, and a submit button. This action is only applicable if the student’s level is 3; otherwise, an error message is shown.
- **View Students by Status**: Users can view all active or inactive students on a separate page, rendered in a table with related attributes.
- **Change Student Status**: Users can change the status of students from active to inactive or vice versa directly from the table view.
- **Navigation Bar**: The website includes a well-designed navigation bar for easy access to all pages and a home page.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: SQLite3

## 1- install a virtual enviroment
```
python3 -m venv env
```
## 2- clone the repo inside the virtual enviroment directory
## 3- activate virtual environment
```
Scripts\activate
```

## 4- start project 
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
