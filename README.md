# Changelog

### 16/09/21
* Initial Commit
* Created test file - Fahad

10/18/2021 - refer to the comments in the commit , 

10/19/2021- "Ok so now the website has basic navigation functionality and the feel that you are actually logged in . Rn if you create your account it prompts you to log into the account that you just created , this is kinda bad but its not necessary that it be fixed. There is still no  real book appointment option , and the view results doesnt really work weeither , its just a for loop showing the first and last name 
of all appointments made . Dev plan as of right now is to get the appointment system working , then the view result system working , then maybe a staff page(not admin page)" - Jared


10/28/2021 - The book appointment page now has an appointment form that can be filled out and submitted. The viewresults page allows you to see the booked appointment and the date+time as well as all the other information that you submitted in the form. It does not allow you to delete or update/change the appointment in any way . The date+time selector is very difficult to use on the bookappointment page . It definitely needs a better entry method . The phone number entry fields could use some checcks as well. There is still no staff page and the admin page still has the word django on it .
-Jared 

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
    -`Welcome message` added to `sitebase.html`
    -`FAQ` updated with 10 General Questions and Answers persons may ask
* `index.html`stores the update for the `Welcome message` that is to be added to the home page(I cannot find page)