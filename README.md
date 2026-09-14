# **Library Management System**
A console-based Management System built with sqlalchemy & python

The application helps library admin to keep record of all borrowing, returning and overdue books, search within library's catalogue and add register new books

## **Stack**
- Python 3.13+
- SQLAclemy
- SQLite
- Poetry

## **Installation guide**
1. **Clone the repository to local directory**

`git clone https://github.com/GorbatovNikita/lib-console`

2. **Move to created directory**

`cd lib-console`

3. **Create virtual environment** 

**Make sure that python is installed on computer and added into PATH**

`python3 -m venv .venv`

4. **Activate virtual environment**

MacOs/Linux

`source .venv/bin/Activate`

Windows

`.venv/scripts/Activate`

5. **Install poetry and dependencies**

`pip install poetry`

`poetry install`

6. **Run main.py**

App will automatically create database, no preliminary actions needed

App uses SQLite3 but it can be switched to heavier and more complex DBMS by simply changing the link in database/connection.py and installing required drivers

## **Application operation cycle**
**Main menu**
- Book management(navigate to book menu)
- User management(navigate to user menu)

**Book menu**
- Add book(adding book to the database)
- Remove book(removing book from the database)
- Search by title/author/ISBN(searching for book with given parameters)
- Show all books(shows all books that exist in the library)
- Borrow / return(navigate to borrow menu)
- Return to main menu(navigate to main menu)

**Borrow menu**
- Show available books(shows all books that are available for users)
- Borrow book(lets you borrow book from the system by user id and book id)
- Return book(lets you return book to the system by user id and book id)
- View overdue books(lets you view all books that are overdue)
- Return to main menu(navigate to main menu)

**User menu**
- Add user(lets you add new user to the system)
- Remove user(lets you remove user from the system)
- Show users(shows all users)
- Return to main menu(navigate to main menu)

## **Licence**
The application was created for educational purposes by a student as part of the admission process for a Kotlin development course.

---

<sub>

I am certain that my console application's processing system could be significantly improved

I apologize for this to whoever will be evaluating my program. :D

Ngl I was having fun

Also sorry for having everything pushed through single commit, i know its bad

I stole console part from one of my repos(you can find it in my profile, its called "energy-register") and redesigned it a lot
</sub>




