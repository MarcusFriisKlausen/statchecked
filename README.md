# Stat Checked: Project for the course Databases and Information Systems

Intended to be a full stack web application specifically making use of SQL databases to present winrates for runes and item builds for champions in League of Legends.

# How to compile and run
First clone or download the public repository "statchecked" from GitHub. Then, to make sure that the application can compile and run, download the required packages, which is flask and flask SQL and pandas, using the following commands in the terminal:
	
    For flask:
	    pip install Flask
    
    For flask SQL:
        pip install flask-sqlalchemy
    
    For pandas:
        pip install pandas

To run the project, navigate to the folder “app”, and then run either of the two following commands, depending on which computer the project is run on:

	For Mac:
		python3 -m flask --app __init__.py run

	For Windows or Linux:
		flask --app __init__.py run

When the project runs, a link to the webpage will appear in the terminal. Copy that link, and paste it into a browser to see the webpage. 

# How to interact with the webpage
To interact with our webpage, the user can click on the icons for each of the champions on the front page, where they then will be directed to another page where the champions win rates can be seen. On the front page as well, the user can search for a specific champion, using the search bar in the top left corner of the page. When the name of the champion is entered in the search bar and the user have pressed “enter”, the user will then be directed to the page where the champions win rates can be seen. Lastly, on the front page as well, the user can manually scroll down through the page to see all of the 167 champions.

# Where the data is from
The data for the project was obtained from riot games API, and consists of three games from top 9000 players on the europe server, where the duplicates have been removed. 

