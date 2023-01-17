# FarmZone
### Video Demo: https://youtu.be/IvvzX_RoIIg
### Description: Farmzone is a farm management software specifically for crop production. Tech stack used are Bootstrap, Flask and SQLITE. Users are able to register and sign in. Validation with flash messages are included for incomplete sign up or log in details. Once logged in, the user lands on the farm page where they can create their farms, with summarry details. The app features a crop database in where the user can create and store the crops they would be planting on the their farms. In the farms page, the user can got to the 'farm details' route to view and input more details about their farm. Details include the type of crops (based on the crop database), the planting and projected harvest dates, the number of crop stands and the land area. A log out link is provided to log the user our and return to the login page


## Files and Folders Description: 


### flaskr folder: Contains the main application folders, as well as the python files for the routes

### instance: Contains the flaskr.sqlite database. 4# tables are contained in the database: users, crops, farms and plantdetails. Foreign keys are used to communicate between databases

#### _init.py_: Entry point for application containing the __main__ . An application factory function was used for the configuration, rather than using a global Flask instance, to ensure that project can be scaled in future. A blueprint is used to link the different routes to the _init.db_ file

#### users.py: This handles all routes related to user authentication/authorization (sign in,register, logout, loginrequired)

#### farms.py: Handles routes related to the farm dashboard and creation of new farms

#### crops.py: Handles routes related to crops database population

#### db.py: Contains the configuration details for the database

#### farmdetails.py: Handles the farm details routes

#### templates: Contains the Jinja templates which render all the view. Content files are related to to the respective routes shown above

##### crops.html: Renders the crops list and new crops pages

##### farms.html: Rebders the farm dashboard and allows for additon of new farms

##### farmdetails.html: Renders the page that displays the details of the farm

##### layout.html: Contains base page data that is reused across pages e.g navbar, flash

##### login.html: Renders page for loging in of users

##### newcrop.html: Renders form for creating new crop

##### newfarm.html: Renders form for creating new farm

##### register.html: Renders page to register new user


#### static: Contains the css and javascript files employed


