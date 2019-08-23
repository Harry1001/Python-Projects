
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no:    N9920811
#    Student name:  Harmanjeet Singh
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  POPULARITY CLOUDS
#
#  Movie fans have strong opinions about their favourite actors.  In
#  this task you will develop a program that helps visualise some
#  of the opinions of movie fans derived from a survey of
#  Microsoft employees.  To do so you will make use of three
#  different computer languages, Python, SQLite and HTML.  You
#  will develop a Python function, show popularity, which accesses
#  data in an SQL database and uses this to generate HTML documents
#  which visually display an actor's popularity according to the
#  survey results.  See the instructions accompanying this file for
#  full details.
#
#--------------------------------------------------------------------#



#-----Acceptance Tests-----------------------------------------------#
#
#  This section contains unit tests that run your program.  You
#  may not change anything in this section.  NB: 'Passing' these
#  tests does NOT mean you have completed the assignment because
#  they do not check the HTML files produced by your program.
#


"""
------------------- Normal Cases with valid input --------------------

>>> show_popularity(['Female', 'Male', '30-40'], 20, 'Test01') # Test 1

>>> show_popularity(['20-30', '30-40', '40-50'], 50, 'Test02') # Test 2

>>> show_popularity(['20-40', '40-80', 'All'], 30, 'Test03') # Test 3

>>> show_popularity(['Female', 'Male', '30-40', '40-60', '60-100', 'All'], 30, 'Test04') # Test 4

>>> show_popularity(['All'], 20, 'Test05') # Test 5

>>> show_popularity(['30-40'], 50, 'Test06') # Test 6

>>> show_popularity(['30-50'], 0, 'Test07') # Test 7


------------------- Cases with invalid input ------------------------

>>> show_popularity(['20-30', '30-40', '3a-34' ], 30, 'Test08') # Test 8
Invalid customer group: 3a-34

>>> show_popularity(['teens', '20-20','30-40','40-50', '50-50', '60-d0'], 30, 'Test09') # Test 9
Invalid customer group: teens
Invalid customer group: 60-d0

>>> show_popularity(['old people', '30', '40-60', '-70', '70-100'], 30, 'Test10') # Test 10
Invalid customer group: old people
Invalid customer group: 30
Invalid customer group: -70

>>> show_popularity(['-', '30-50', '40-60', '50-20', '40 60'], 50, 'Test11') # Test 11
Invalid customer group: -
Invalid customer group: 40 60

""" 
#
#--------------------------------------------------------------------#



#-----Students' Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.


from random import choice

# Generate a webpage for actors popularity while considering Male customers
def draw_male_html_page(num_of_records, total_male_customers, reqd_actor_record, category, title):

    #import html library
    from urllib import urlopen

    global customer_category
    
    male_customer_file = open(title + '_' + category + '.html', 'w')
    palette = ['red', 'green', 'orange', 'pink', 'brown', 'blue']          
    male_customer_file.write('<html>')
    male_customer_file.write('<title>' + title + '</title>')
    male_customer_file.write("<body>  <p align = 'center'> <span style = 'font-size: 25'> <b> Top " + str(num_of_records) + ' Most Popular Actors </span> <br> <br> Customer Group: Male <br> Number of Customers: ' + str(total_male_customers[0]) + '</b>  </p> <hr>')
    reqd_actor_record.sort()

    #change the font size according to the popularity
    for actor in reqd_actor_record:

        actor_popularity = '(' + str(actor[1]) + ')'

        if actor[1] > 600:
            male_customer_file.write("<p  style = 'font-size: 55'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>500 and actor[1] <= 600:
            male_customer_file.write("<font style = 'font-size: 48'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>400 and actor[1] <= 500:
            male_customer_file.write("<font  style = 'font-size: 40'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>350 and actor[1] <= 400:
            male_customer_file.write("<font style = 'font-size: 34'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>300 and actor[1] <= 350:
            male_customer_file.write("<font  style = 'font-size: 28'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>200 and actor[1] <= 300:
            male_customer_file.write("<font  style = 'font-size: 22'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>100 and actor[1] <= 200:
            male_customer_file.write("<font style = 'font-size: 18'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")
        else:
            male_customer_file.write("<font style = 'font-size: 15'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")


    male_customer_file.write(' <hr> ')        

    # generate hyperlinks based on conditions
    if category == 'Male':

        num_of_customer_categories = len(customer_category)

        if num_of_customer_categories == 2:
            position_of_category = customer_category.index(category) 

            if position_of_category == 0:
                next_category_name = title + '_' + customer_category[1] + '.html'
                male_customer_file.write("<div align = 'right'> <font color = 'blue'> <a href = " + next_category_name +  " > Next Page </a> </font></div>")

            else:
                prev_category_name = title + '_' + customer_category[0] + '.html'
                male_customer_file.write("<div align = 'left'><font color = 'blue'>  <a href = " + prev_category_name +  " > Previous Page </a></font> </div>")

        elif num_of_customer_categories > 2:
            position_of_category = customer_category.index(category) 

            if position_of_category == 0:
                next_category_name = title + '_' + customer_category[1] + '.html'
                male_customer_file.write("<div align = 'right'><font color = 'blue'>  <a href = " + next_category_name +  " > Next Page </a></font> </div>")

            elif position_of_category == -1:
                position_prev_category = len(customer_category) - 2
                prev_category_name = title + '_' + customer_category[position_prev_category] + '.html'
                male_customer_file.write("<div align = 'left'><font color = 'blue'>  <a href = " + prev_category_name +  " > Previous Page </a> </font></div>")

            else:
                position_prev_category = position_of_category - 1
                prev_category_name = title + '_' + customer_category[position_prev_category] + '.html'
                male_customer_file.write("<p style align = 'left'><font color = 'blue'>  <a href = " + prev_category_name +  " > Previous Page </a></font>")
               
                position_next_category = position_of_category + 1
                next_category_name = title + '_' + customer_category[position_next_category] + '.html'
                male_customer_file.write("<div style align = 'right'><font color = 'blue'>  <a href = " + next_category_name +  " > Next Page </a> </div></p>")
                       

    male_customer_file.write(' </body>')
    male_customer_file.write('</html>')
    male_customer_file.close()
    
   
        
# Generate a webpage for actors popularity while considering Female customers   
def draw_female_html_page(num_of_records, total_female_customers, reqd_actor_record, category, title):

    #import html library
    from urllib import urlopen

    global customer_category
    
    palette = ['red', 'green', 'orange', 'pink', 'brown', 'blue']          

    female_customer_file = open(title + '_' + category + '.html', 'w')
                
    female_customer_file.write('<html>\n')
    female_customer_file.write('<title>' + title + '</title>')
    female_customer_file.write("<body> <p align = 'center'> <span style = 'font-size: 25'> <b> Top " + str(num_of_records) + ' Most Popular Actors </span> <br> <br> Customer Group: Female <br> Number of Customers: ' + str(total_female_customers[0]) + '</b> </p> <hr> ')
    reqd_actor_record.sort()

    #change the font size according to the popularity
    for actor in reqd_actor_record:

        actor_popularity = '(' + str(actor[1]) + ')'

        if actor[1] > 200:
            female_customer_file.write("<p style = 'font-size: 55'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>150 and actor[1] <= 200:
            female_customer_file.write("<font  style = 'font-size: 48'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>120 and actor[1] <= 150:
            female_customer_file.write("<font  style = 'font-size: 40'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>100 and actor[1] <= 120:
            female_customer_file.write("<font style = 'font-size: 34'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>90 and actor[1] <= 100:
            female_customer_file.write("<font style = 'font-size: 28'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>70 and actor[1] <= 90:
            female_customer_file.write("<font style = 'font-size: 22'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>50 and actor[1] <= 70:
            female_customer_file.write("<font  style = 'font-size: 18'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>30 and actor[1] <= 50:
            female_customer_file.write("<font style = 'font-size: 12'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        else:
            female_customer_file.write("<font style = 'font-size: 10'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

    female_customer_file.write(' <hr> ')        

    # generate hyperlinks based on conditions
    if category == 'Female':

        num_of_customer_categories = len(customer_category)

        if num_of_customer_categories == 2:
            position_of_category = customer_category.index(category) 

            if position_of_category == 0:
                next_category_name = title + '_' + customer_category[1] + '.html'
                female_customer_file.write("<div style align = 'right'> <font color = 'blue'> <a href = " + next_category_name +  " > Next Page </a></div></font>")

            else:
                prev_category_name = title + '_' + customer_category[0] + '.html'
                female_customer_file.write("<div style align = 'left'> <font color = 'blue'> <a href = " + prev_category_name +  " > Previous Page </a></div></font>")

        elif num_of_customer_categories > 2:
            position_of_category = customer_category.index(category) 

            if position_of_category == 0:
                next_category_name = title + '_' + customer_category[1] + '.html'
                female_customer_file.write("<div style align = 'right'> <font color = 'blue'> <a href = " + next_category_name +  " > Next Page </a> </div></font>")

            elif position_of_category == -1:
                position_prev_category = len(customer_category) - 2
                prev_category_name = title + '_' + customer_category[position_prev_category] + '.html'
                female_customer_file.write("<div style align = 'left'> <font color = 'blue'> <a href = " + prev_category_name +  " > Previous Page </a></div></font>")

            else:
                position_prev_category = position_of_category - 1
                prev_category_name = title + '_' + customer_category[position_prev_category] + '.html'
                female_customer_file.write("<div style align = 'left'> <font color = 'blue'> <a href = " + prev_category_name +  " > Previous Page </a></font></div>")

                position_next_category = position_of_category + 1
                next_category_name = title + '_' + customer_category[position_next_category] + '.html'
                female_customer_file.write("<div style align = 'right'> <font color = 'blue'> <a href = " + next_category_name +  " > Next Page </a></font></div>")

    female_customer_file.write(' </body>')
    female_customer_file.write('</html>')
    female_customer_file.close()

    
# Generate a webpage for actors popularity while considering All customers   
def draw_all_html_page(num_of_records, total_all_customers, reqd_actor_record, category, title):

    #import html library
    from urllib import urlopen

    palette = ['red', 'green', 'orange', 'pink', 'brown', 'blue']          
    
    all_customer_file = open(title + '_' + category + '.html', 'w')
                                                                                                                                                    
    all_customer_file.write('<html>\n')
    all_customer_file.write('<title>' + title + '</title>')
    all_customer_file.write("<body>  <p align = 'center'> <span style = 'font-size: 25'> <b> Top " + str(num_of_records) + ' Most Popular Actors </span> <br> <br> Customer Group: All <br> Number of Customers: ' + str(total_all_customers[0]) + '</b> </p> <hr> ')
    reqd_actor_record.sort()

    #change the font size according to the popularity
    for actor in reqd_actor_record:

        actor_popularity = '(' + str(actor[1]) + ')'

        if actor[1] > 600:
            all_customer_file.write("<p  style = 'font-size: 55'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>550 and actor[1] <= 600:
            all_customer_file.write("<font  style = 'font-size: 48'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>500 and actor[1] <= 550:
            all_customer_file.write("<font  style = 'font-size: 45'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>450 and actor[1] <= 500:
            all_customer_file.write("<font  style = 'font-size: 40'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>350 and actor[1] <= 400:
            all_customer_file.write("<font  style = 'font-size: 35'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>300 and actor[1] <= 350:
            all_customer_file.write("<font  style = 'font-size: 30'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>250 and actor[1] <= 300:
            all_customer_file.write("<font  style = 'font-size: 25'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>200 and actor[1] <= 250:
            all_customer_file.write("<font  style = 'font-size: 25'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>150 and actor[1] <= 200:
            all_customer_file.write("<font  style = 'font-size: 25'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        else:
            all_customer_file.write("<font  style = 'font-size: 20'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")
      

    all_customer_file.write(' <hr></body>')
    all_customer_file.write('</html>')
    all_customer_file.close()
    
# Generate a webpage for actors popularity while considering certain Age-Group customers      
def draw_range_html_page(num_of_records, total_range_customers, reqd_actor_record, category, title):

    #import html library
    from urllib import urlopen
    
    range_customer_file = open(title + '_' + category + '.html', 'w')
    palette = ['red', 'green', 'orange', 'pink', 'brown', 'blue']          

    range_customer_file.write('<html>\n')
    range_customer_file.write('<title>' + title + '</title>')
    range_customer_file.write("<body> <p align = 'center'> <span style = 'font-size: 25'> <b> Top " + str(num_of_records) + ' Most Popular Actors </span> <br>  <br> Customer Group: ' + category + '<br> Number of Customers: ' + str(total_range_customers[0]) + '</b> </p>  <hr> ')
    reqd_actor_record.sort()

    #change the font size of the actors data according to their popularity
    for actor in reqd_actor_record:

        actor_popularity = '(' + str(actor[1]) + ')'

        if actor[1] > 600:
            range_customer_file.write("<p style = 'font-size: 75'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>550 and actor[1] <= 600:
            range_customer_file.write("<font  style = 'font-size: 70'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>500 and actor[1] <= 550:
            range_customer_file.write("<font  style = 'font-size: 65'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>450 and actor[1] <= 500:
            range_customer_file.write("<font  style = 'font-size: 60'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>350 and actor[1] <= 400:
            range_customer_file.write("<font  style = 'font-size: 55'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>300 and actor[1] <= 350:
            range_customer_file.write("<font  style = 'font-size: 50'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>250 and actor[1] <= 300:
            range_customer_file.write("<font  style = 'font-size: 45'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>200 and actor[1] <= 250:
            range_customer_file.write("<font style = 'font-size: 40'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>150 and actor[1] <= 200:
            range_customer_file.write("<font style = 'font-size: 35'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>100 and actor[1] <= 150:
            range_customer_file.write("<font style = 'font-size: 30'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>50 and actor[1] <= 100:
            range_customer_file.write("<font style = 'font-size: 25'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")

        elif actor[1]>0 and actor[1] <= 50:
            range_customer_file.write("<font style = 'font-size: 20'> <font color = " + choice(palette) + ">" + actor[0] + "<font style = 'font-size: 8'>"+ actor_popularity + " </font></font>")


    range_customer_file.write(' <hr> </body>')
    range_customer_file.write('</html>')
    range_customer_file.close()
    
                                                                                                                                        
# Get the sql functions
from sqlite3 import *

# Extract Asked  Data from the given Database
def extract_male_customer(num_of_records, category, title):

    #Establish a connection with database
    connection = connect(database = 'movie.db')

    #Get the cursor on the database
    movie_db = connection.cursor()

    # Query to get the total number of Male Customers
    sql_1 = "select count(*) from customers where gender = 'Male'"

    movie_db.execute(sql_1)

    #get one row from the database
    total_male_customers = movie_db.fetchone()

    # Query to get the name of customers and their popularity
    # in case of Male Customers
    sql_2 = "select actor, count(actor) as popularity from customers, favorite_actors where customers.customerID = favorite_actors.customerID and gender = 'Male' group by actor order by popularity desc limit " + str(num_of_records)
     
    movie_db.execute(sql_2)

    #get all the row from the database

    actors_record = movie_db.fetchall()

    #Close the connection         
    movie_db.close()

    #call the function to generate html web page
    draw_male_html_page(num_of_records, total_male_customers, actors_record, category, title)



# Extract Asked  Data from the given Database
def extract_female_customer(num_of_records, category, title):

    #Establish a connection with database
    connection = connect(database = 'movie.db')

    #Get the cursor on the database
    movie_db = connection.cursor()

    # Query to get the total number of Female Customers
    sql_1 = "select count(*) from customers where gender = 'Female'"

    movie_db.execute(sql_1)

    #get one row from the database
    total_female_customers = movie_db.fetchone()

    # Query to get the name of customers and their popularity
    # in case of Female Customers
    sql_2 = "select actor, count(actor) as popularity from customers, favorite_actors where customers.customerID = favorite_actors.customerID and gender = 'Female' group by actor order by popularity desc limit " + str(num_of_records)
     
    movie_db.execute(sql_2)

    #get all the row from the database
    actors_record = movie_db.fetchall()

    #Close the connection
    movie_db.close()

    #call the function to generate html web page
    draw_female_html_page(num_of_records, total_female_customers, actors_record, category, title)

   

# Extract Asked  Data from the given Database
def extract_all_customer(num_of_records, category, title):

    #Establish a connection with database
    connection = connect(database = 'movie.db')

    #Get the cursor on the database
    movie_db = connection.cursor()

    # Query to get the total number of Customers
    sql_1 = "select count(*) from customers "

    movie_db.execute(sql_1)

    #get one row from the database
    total_all_customers = movie_db.fetchone()

    # Query to get the name of customers and their popularity
    # in case of All the Customers
    sql_2 = "select actor, count(actor) as popularity from customers, favorite_actors where customers.customerID = favorite_actors.customerID group by actor order by popularity desc limit " + str(num_of_records)
     
    movie_db.execute(sql_2)

    #get all the row from the database
    actors_record = movie_db.fetchall()

    #Close the connection
    movie_db.close()

    #call the function to generate html web page
    draw_all_html_page(num_of_records, total_all_customers, actors_record, category, title)



# Extract Asked  Data from the given Database
def extract_certain_customer(num_of_records, category, title):

    #Establish a connection with database
    connection = connect(database = 'movie.db')

    #Get the cursor on the database
    movie_db = connection.cursor()

    #make two boolean variables to handle age group with different length
    first_category =False

    second_category =False
      
    connection = connect(database = 'movie.db')

    movie_db = connection.cursor()

    # Condition to get the Min and Max Age from the Age-Group category
    if len(category) == 5:
          
        min_age_1 = category[0] + category[1]
        max_age_1 = category[3] + category[4]

        first_category =True

    elif len(category) == 6:

        min_age_2 = category[0] + category[1]
        max_age_2 = category[3] + category[4] +category[5]

        second_category =True

    #Condition to execute required query as per the Age-Group Category for getting the
    # total number of customers in that particular age-group

    if first_category and min_age_1 == max_age_1 :

        sql_1A = "select count(*) from customers where age = " + min_age_1 #min age and max age are same
        movie_db.execute(sql_1A)
        
    elif first_category:

        
        sql_1B = "select count(*) from customers where age >= " + min_age_1 + " and age <= " + max_age_1
        movie_db.execute(sql_1B)
    
    else:
        sql_1C = "select count(*) from customers where age >= " + min_age_2 + " and age <= " + max_age_2 
        movie_db.execute(sql_1C)


    #get one row from the database
    total_range_customers = movie_db.fetchone()

    #Condition to execute required query as per the Age-Group Category for getting the
    # Actor's name and popularity in that particular age-group

    if first_category and min_age_1 == max_age_1 :
        sql_2A = "select actor, count(actor) as popularity from customers, favorite_actors where customers.customerID = favorite_actors.customerID and age = " + min_age_1 +" group by actor order by popularity desc limit " + str(num_of_records)
        movie_db.execute(sql_2A)

    elif first_category:
        sql_2B = "select actor, count(actor) as popularity from customers, favorite_actors where customers.customerID = favorite_actors.customerID and age >= " + min_age_1 + " and age <= " + max_age_1 + " group by actor order by popularity desc limit " + str(num_of_records)
        movie_db.execute(sql_2B)

    else:
        sql_2C = "select actor, count(actor) as popularity from customers, favorite_actors where customers.customerID = favorite_actors.customerID and age >= " + min_age_2 + " and age <= " + max_age_2 + " group by actor order by popularity desc limit " + str(num_of_records)
        movie_db.execute(sql_2C)

    #get all the row from the database
    actors_record = movie_db.fetchall()

    #Close the connection
    movie_db.close()

    #call the function to generate html web page
    draw_range_html_page(num_of_records, total_range_customers, actors_record, category, title)
    
#make global variable so that they can be accessed in different functions 
wrong_categories = []
atleast_one_wrong = False

# Function to check and store invalid categories
def valid_customer_category(customer_categories):

    global wrong_categories

    global atleast_one_wrong

    wrong_categories = []

    atleast_one_wrong = False

    allowed_customer_categories = ['All', 'Male', 'Female', '50-20', '50-50', '20-20', '70-100', '30-40', '30-50', '20-30', '20-40', '40-80', '40-50', '40-60', '60-100']

    #Iterate over the supplied list of customer categories and store
    #invalid categories in an empty list
    for category in customer_categories:

        if category not in allowed_customer_categories:

            wrong_categories.append(category)

            atleast_one_wrong = True

    return True
               
     
########################## PUT YOUR show_popularity FUNCTION HERE

#a list to store customer categories 
customer_category = []

#a list to store valid age groups
valid_age_category = ['30-40', '30-50', '20-30', '20-40', '40-80', '40-50', '40-60', '60-100', '50-20', '70-100', '50-50', '20-20']

def show_popularity(customer_categories, num_of_records, title):

    global wrong_categories
    global atleast_one_wrong
    global customer_category
    global valid_age_category

    #store the list of customer_ categories in a global variable that 
    #can be used to generate hyperlinks
    customer_category = customer_categories

    wrong_categories = []
    
    #Check if the customers categories are valid or not
    if valid_customer_category(customer_categories):

        #Iterate over the supplied list of customer categories and call functions to extract
        #data from the database according to the categories
        for category in customer_categories:

            if category == 'Female':
                extract_female_customer(num_of_records, category, title)

            elif category == 'Male':
                extract_male_customer(num_of_records, category, title)                

            elif category == 'All':
                extract_all_customer(num_of_records,category,title)

            elif category in valid_age_category:
                extract_certain_customer(num_of_records, category, title)
    #Display the Invalid categories(If Any)
    if atleast_one_wrong:

        for wrong_category in wrong_categories:

            print "Invalid customer group:", wrong_category

     

#
#--------------------------------------------------------------------#



#-----Automatic Testing----------------------------------------------#
#
#  The following code will automatically run the unit tests
#  when this program is "run".  Do not change anything in this
#  section.  If you want to prevent the tests from running, comment
#  out the code below, but ensure that the code is uncommented when
#  you submit your program.
#
if __name__ == "__main__":
     from doctest import testmod
     testmod(verbose=True)   
#
#--------------------------------------------------------------------#

