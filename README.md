# Employee Asset Management 

Employee asset management system allows one to manage assets of a given organization that are assigned to employees. 

With this system, you can be able to add employees, add assets, assign assets to employees, transfer assets between employees, add asset repairs and see asset repair history.

## Set up

1. Create a working folder
2. Open the folder in terminal/cmd
3. Download the zip file into the folder or run git clone `git clone git@github.com:Rovine1999/Employees-asset-management-.git`
4. Then run `cd Employees-asset-management-`
5. Create a virtual environment

    - In windows run `python -m virtualenv venv`

    - In Linux run `python3 -m virtualenv venv`

    N/B: You need to have `virtualenv` installed. To install it run `pip install virtualenv`

6. Activate your environment

    - In windows run `source ./venv/Scripts/activate`

    - In linux run `source ./venv/bin/activate`

7. Install requirements using `pip install -r requirements.txt`
8. Navigate to `assetmod` folder using `cd assetmod`
9. Make migrations and migrate if you don't have `db.sqlite3` file in your folder tree using `python manage.py makemigrations && python manage.py migrate`
10. Run the server `python manage.py runserver`
11. Open `Postman`
12. Import the `postman collection` in the working folder called `Employee Asset Mgt.postman_collection.json`.
13. Create an environment in postman if one is not created for you and add: 
    - `base_url`: `http://localhost:8000`
    - `token`: `<Update this after using the login endpoint under users module>`

14. You are all set, test out the entire collection **top down**

- Postman doc [here](https://documenter.getpostman.com/view/15444678/2s9YRGxpFi)