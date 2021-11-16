# Changelog

### 16/09/21
* Initial Commit
* Created test file - Fahad

10/18/2021 - refer to the comments in the commit , 

## 10/19/2021- Jared M.
* Website allows navigation around website
* Create account allows user to create account and then log in.
* Book appointmentr does not work, view results does not show appointments, only allows user to see first and last names of appointments


## 10/28/2021 - Jared M
* Book appointment page can alllow user to create entry in table ,(makes appointment)
* View rersult page allows user to see all information submitted by the user in the form


### 31/10/21 (Suveer R.)
* Created Covid-19 Advisory, About Us (infopage.html) and FAQ Pages
* Layout of various pages changed for better readability
Additions were made to the `url.py` and `views.py` to accommodate the new pages.
The About Us page, has a carousel which can be utilized in the future to contain anchor tags to take the user to various parts of the website. Currently the visiblity of the text is low due to the colours of the pictures and text, this would be changed in the future.
The FAQ page has an accordion to be visually appealing and interactive to the user. 

11/1/2021 - Jared - 1. The book appointment page has better headings for the form entry but still no calendar and clock to select the appointment time to request 
                    2. THe user now "requests" an appointment instead of books it immediately from the website.
                    3. The admin page is now easier to use and makes more sense for the staff/admin user trying to operate the website. Now the staff or admin will have to
                    select the appoiintment and manually check whether or not the appointment has been denied or accpeted ,then if the test results are ready or not, then if the 
                    results are positivbe or not the website will indicate that , in the future , the website will not show this info , an email will be sent to the user on the 
                    email they selected of their results.
                    4. Split appointment date and time into two seperate data entry fields in the appointment request form
                    
### 5/11/2021(Sadie E.)
* `Logo` in Navbar not clickable for less redundancy between Home and the logo
    -Navigational bar extended to fit entire page
* Text added to various pages for users to better understand each page
    -`FAQ` updated with 10 General Questions and Answers persons may ask
* `index.html`stores the update for the `Welcome message` that is to be added to the home page(I cannot find page)


6/11/2021 - Jared Mohansingh - Cleaned up repository


### 10/11/2021(Sadie E.)
* Text added to various pages for users to better understand each page
    * -`Welcome message` added to `homesignup.html`
    * -`covidadvisories.html` updated with information by WHO and Trinidad and Tobago's COVID-19 advisories
    * -`viewresult.html` updated for easy viewing by users

### 15/11/2021(Sadie E.)
* `bookappointment.html` updated with additional questions
* `models.py` updated variables due to added questions on `bookappointment.html` page

### 16/11/2021(Jared M.)
* All instancees to view `viewresult` were changed to `viewappointment`
* `models.py` updated variables to remove fields that were not needed
* Converted book appointment view in `views.py` to use a form in `forms.py` instead of the raw fields as described in the view
* Changed account creation form to use a datepicker instead of a raw text input field to enter the date
* Added a button in the bottom of teh view appointments page to allow user to make an appointment if there are no appointments already made 

