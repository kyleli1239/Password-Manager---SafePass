# SafePass - Password manager

The SafePass application allows a single user to securely store their credentials inside the vault. The user must be authenticated before accessing the vault and all data is hashed or encrypted

## Setup instruction

### 1. Download Dependencies and Python Packages

This project requires Python (preferably a later version like Python 3.9 or higher) and the following packages to be installed

* **'tkinter'** – For the GUI interface (usually included with Python standard library)
* **'cryptography'** – For encryption and decryption
* **'bcrypt'** – For password hashing
* **'sqlite3'** – For database management (usually included with Python standard library)

You can install packages using **'pip install cryptography bcrypt'**

### 2. Run the main program 'main.py'. This will automatically create the database.

## Sample Input for Testing

* Run `python main.py` on a terminal. If this does not work, open the main.py file and directly run it for example, in Visual Studio and run in dedicated terminal.

### 1. Create a new master password

* On the signup page, enter your master password **'Password123'**.
* Click the **'submit'** button.

### 2. Login using same master password

* On the login page, enter the master password **'Password123'**.
* Click the **'submit'** button.

### 3. Access the vault and view/delete/add entries

* On the vault page, click the **'+'** button.
* On the add entry page, enter **'website1'** in the website entry, enter **'username1'** in the username entry and enter **'password1'** in the password entry.
* Click the **'Save Entry'** button.
* Entries should now be displayed on the vault page.
* If you want, click the **'Delete button'** next to the entry.
* This will delete that row.

### 4. Viewing the database

* To view the data inside the database, use a SQLite viewer, for example **' https://inloop.github.io/sqlite-viewer/ '**.
* Drag the database file called **'SafePass_database'** inside the file called **'data'** into the website.
* You can now view the data inside the database.
* You can switch which table you want to view: **'master_password'** and **'password_vault'**
* Data inside the tables are encrypted 
