# HOMEWORK WEEK 5-6
##### (handout for students)
## TASK 1 (Agile Techniques)
#### Question 1
Complete definitions for Scrum related key terminology provided below.

SCRUM CEREMONIES
- Product backlog refinement
I'm actually not entirely convinced that this can be called a ceremony, siding it on the same level with sprint planning or retrospective or with the daily scrum. It doesn't have a concrete time to be held, unlike the ceremonies do, it is not called a ceremony nowhere in the Scrum Guide, nor it was listed together with all the Scrum Events, nor it was ever called this way on my PSM preparaction class. It's more of a regular, reocurring process that should be done in the background/simultaneously, a "living artifact", so the Product Backlog should be continuoulsy refined in order to serve its purpose the best.
Product backlog refinement is the act of reviewing the items in the product backlog in order to evaluate their priority, readability/understandability (for devs), size (should it be chunked into smaller pieces or reformatted in any way) and usefulness. It is done by the Product Owner (as the owner of the Product Backlog artifact) and member sof the Scrum Team - presence of everyone is not necessary, but the Product Owner should do it with consulting the Dev Team representative/s.The aim is to conceptualise the tasks in the Product Backlog in understandable, small and detailed, more actionable items.

- Sprint planning
Sprint planning is just as the name suggests, an event that takes place prior to every single Sprint, and its' sole purpose is to come up with an actionable plan for the next Sprint. At least the Product Owner and the Developers Team should be present and active during this event. Over the course of this event the team will decide what is their goal for this sprint (the main functionality they want to implement with the incrementation resulting from this Sprint). To come up with a detailed action plan with concrete deadlines the team reviews the Product Backlog (the items which are not yet implemented) and the Product Goal and try to answer guiding questions like "why are we doing this Sprint? (to achieve / implement what?)", "what precisely we will aim to implement with this incrementation?" (which Product Backlog items to choose to tackle with this Sprint), and "how exactly are we planning on implementing that?" (chunking the tasks into a detailed to-do kind of task items list). For a 2 weeks Sprint, the planninv event should take no longer than 4 hours.

- Daily scrum
This is a daily event that ideally happens in the morning, before the team commences work, and takes up to 15 minutes - again, ideally, but if it takes longer it becomes distractive and burdening. It can be done in the form of a stand-up meeting to facilitate the swiftness and briefness. This meeting is for the people who actively work on the Sprint Backlog items, thus the presence of the Scrum Master and the Product Owner is non-obligatory. It's often advised for the Scrum Masters though so that they can keep their hand on the pulse, see how the progress goes and if there are any obstacles they could assist solving. The meeting takes form of each developer answering 3 questions - what did they do yesterday, what will they do today, and if there are any obstacles limiting their work. The aim of the Daily Scrum is to keep the whole team on the same page in regards to work progress & status towards achieving the Spring Goal, give the opportunity to call for help whenever required, and to ensure adherence to the Spring Goal. 

- Sprint review
A Sprint Review is a meeting which takes place upon the completion of the Sprint. The participants are the whole Scrum Team (that includes the Scrum Master and the Product Owner) and the client. The aim of this meeting is to present the fruits of the Sprint to the client, solicit their feedback, check if this is what they've wanted, if any tweaks are necessary, how the progress toward the Product Goal vision is going. If there are any new ideas or requirement refinements from the client side, they ought to be discussed and then the Product Backlog may need to be furnished with additional tasks or updated/changed in some way. The client's feedback is helpful in shaping the future iincrements & Sprints. This meeting should not take over 4 hours (assuming the most common length of the Sprint, which is 2 weeks. Scrum Guide suggests for each 1 week of sprint duration this meeting as well as the Sprint Planning meeting should take up to 2 hours - so 2 weeks long Sprint => 4 hours, 1 month long Sprint => up to 8 hours Planning & Review meetings).

- Sprint retrospective
This meeting takes place after the Sprint Review and before the commencement of the next Sprint. Its aim is to review the previous Sprint from the Scrum Team's side (yes, with the Scrum Master and the Product Owner) - what went well, what didn't go well, which problems are yet unsolved, how could they be solved, what to optimise and how. This meeting is the one where it's best to speak of tweaks and optimisation to project-global rules of work such as the Definition of Done, how the team conducts Sprint Planning or the Daily Scrum, if the team misses any crucial skills in order to deliver the work ahead, or simply just choosign the communication methods for this projecte - such issues should not be changed on the run, mid-Sprint, because they would affect the daily work too much making it hard to tweak. It is also a timebox event, should not take longer than 3 hours for a 1 month long Sprint.

SCRUM ROLES
- ScrumMaster
A Scrum Master is a leader-servant role. They are serving the Scrum Team by coaching them in Scrum ways, helping them indestand the methodology and reasons for Scrum methods in order to best implement them in practice. The Scrum Master's goal is to increase the team's effectiveness. They should do this by ensuring high value of the output content, clear Definition of Done, clearly outlined backlog items and goals, ensuring the meetings are timely and productive (everyone stays on topic), remove productivity limiting impediments and ensure adhering to the Scrum practices, coach about Scrum whenever necessary/needed.

- Product Owner
Product Owner is the owner of the Product Backlog artifact, and is solely responsible for its contents and ordering. Of course, this artifact is a result of their consultations with both the client and the developers, so between the vision & requirements and the technical possibilities of output, however its shape must be decided by the Product Owner only. They are to make sure that the Product Goal & Backlog items are clearly understandable in the same way by the whole team - if not, they should refine them in order to achieve such a clear understanding. The aim of this role is to maximise the value of the Scrum Team's output in terms of the shipped product - this is why tha bility to prioritise the Backlog items is crucial, and this hinges heavily on the Product Owner's ability to both communicate with & understand the client's needs and expectations well, and to communicate those to the Developer's Team as well, in order to prioritise the most important, crucial functionalities first and foremost, for maximum client satisfaction with the product.

- Development Team
The developers are the Scrum Team members who are actively responsible for delivering a workable (usable) increment (= the result of the Sprint is an increment of the application or a code). Because of this, they are also responsible for ensuring the clarity and adherence to the Definition of Done, choosing the Product Backlog items for implementation during the Sprint, setting the Sprint Goal and adapting the daily work in order to meet the Sprint Goal they have set upon themseves during Sprint Planning.

(All Scrum related answers are based on my own knowledge, class notes and the cheatsheet I've prepared long time ago while preparing for the exam, and << all that << is of course based on the Scrum Guide, as the Scrum Guide is actually the only really reliable source of knowledge about anything Scrum related - https://www.scrum.org/resources/scrum-guide)

#### Question 2
You are leading a development team that was given a task to create a new yoga booking system.
High level description of the system is as follows:
- It has a very simple interface to accept user input (bookings) and display classes information.
- All bookings, appointments, schedules etc should be stored in a SQL database.
- There is a ‘backend’ system that should be written in Python to handle the logic and manage the data flow.

Your team has two weeks to build a simple prototype that will be shown to the client to seek their feedback and discuss further enhancements.
 
TASK
- Break this task into smaller stories (chunks of work) for the team to work on.
- Assume that one person works on one task.
- Mark tasks that can be worked on in parallel and perhaps those that need to be worked on in particular order.

#### Task 1 Answer 2

1. Database Creation + Procedures
    - create a normalised database for:
        - yoga classes - yoga type, and trainer
        - yoga classrooms - building, room capacity, *hour availability
        - yoga people - name, surname, teacher/student
        - contact data - telephone number, email address
        - *address data - address, postal code, city
        - trainer time availability schedule
        - available yoga classes (mix of yoga type, trainer availability and classroom availability - also with class capacity = room capacity -3 - +user view)
        - class booking / available class remaining capacity (as people book, this should be recorded, rooms have their unsurpassable capacity)
    - create procedures and events for:
        - adding, deleting, editing a trainer
        - adding, deleting, editing a user
        - adding, deleting, editing an admin
        - adding, deleting, editing a classroom
        - adding, deleting, editing a class
        - booking the class
        - showing available classes (in a view)
        - adding, deleting, editing trainer schedule data
2. Write the backend logic connecting this:
    - write the main module displaying the available classes
    - connect the main module to the DB so that it displays available classes
3. Login - Sample Admin + User
    - sample crude user registration (user name + password only, additional fields TBA)
    - sample crude admin panel (functionality to create/add, edit and delete yoga classes and users)
4. Write even crude and simple frontend so that the prototype is presentable
    - write the main landing page with available classes table
    - write userlogin form/page
    - write user registration form/page
    - write pages for login errors
    - write user logged in landing page with available classes table - now with booking availability after login
    - write profile page with editable user data
    - write user booked classes page
5. Connect user action pages with DB, using views where applicable

I may be overly optimistic, but I see nothing that truly collides here preventing work. Even frontend can be first, as it does not matter if we connect backend to frontend or frontend to backend. Names can be easily changed if they don't match, we can use fake mock data just for the sake of trying out the styling in frontend etc. - it is a small enough project to allow for small changes when connecting layers easily - I think. I used to be self taught so there was a long time where I didn't know where such projects should be started best, and I still made a lot of them. For websites in the end I'd always start from the layout design, although in several cases this proved wrong and unflexible. Here I'd personally start from the database design though, and then move onto the connection and interclicability design before donning it all in frontend layer making the app clickable with a mouse in the browser instead of with the console. Frontend in this case is unimportant because this is just a mock prototype, we don't even need a graphics artist, styling with color in CSS will be plenty enough to showcase the prototype's functionalities.

Please see the below diagrams which showcase how I'd attempt to approach implementation of the steps leading to a working prototype of this application.
![Main process flow in the Yoga Class Booking App](/yoga-class-booking-flow.png "Main process flow in the Yoga Class Booking App")
![Yoga Class Booking App Workflow](/yoga-class-booking-workflow.png "Yoga Class Booking App Workflow")
(diagrams made using miro)

## TASK 2 (SQL)
#### Question 1
Design a cinema booking system. Think how you would approach the problem and what are potential ways of solving it?
You do not need to write actual code, but describe the high-level approach:
##### - Draw a list of key requirements.
1. Database Creation
    - create a normalised database for:
        - movies - id, title, year, available/showing or not
        - movie rooms - id, name, capacity, type of screen, hours available
        - users - id, name, surname, email, phone number, payment details, payment status, history of bookings, active bookings
        - movie availability possible schedule (mix of movies, movie rooms)
        - movie schedule  movies, seats & screening times available for booking
    - create procedures and events for:
        - adding, deleting, editing a user, admin, movie room, movie
        - booking the movie & cancelling the booking
        - showing current movie schedule (in a view)
        - adding, deleting, editing movie schedule data
2. Write the backend logic connecting this:
    - write the main module displaying the available movies (movie schedule)
    - connect the main module to the DB so that it displays available movies from the DB
3. Login - Sample Admin + User
    - sample crude user registration (user name + password only, additional fields TBA)
    - sample crude admin panel (functionality to create/add movies, screening times, movie rooms, edit these and user info)
4. Write frontend
    - write the main landing page with available classes table
    - write user login form/page
    - write user registration form/page
    - write pages for login errors
    - write user logged in landing page with current movie schedule - now with booking availability after login
    - write profile page with editable user data incl. payment data, booking history, active bookings
    - write user booked movies page with possibility of cancellation
5. Connect user action pages with DB, using views where applicable
    - set the logic / full procedure for booking, cancellation, adding, editing and removing payment methods
    - set the full procedure & logic for admin populating the movie DB with movies, movie rooms & movie schedule
    - ascertain pulling the current movie schedule works well
    - ascertain booking & cancelling works well

##### - What are your main considerations?
1. user registration, data input & edition, deletion & removal ;
2. movie schedule import view from DB ;
3. making movies bookable from the movie schedule ;
4. booking logic both from user side and DB side ;
5. confirming payment prior to confirming booking and decreasing the number of available seats for the movie ;
6. admin populating the movie DB ;
7. admin creating the current schedule ;

##### - What would be your common or biggest problems?
1. implementing the payment processing
2. connecting the result of processed payment to movie booking logic
3. forgotten password / username => user data reset
4. blocking movie seats when user starts the booking process even before payment is processed to avoid potential booking of the same seats in different booking sessions

##### - What components or tools would you potentially use?
1. payment processing module, there definitely are some, i just never used any
2. probably there is some handy JS tool for table visualisation on the interface
3. definitely a DB connector!
4. not that i've done this, but i'm sure there are modules which can be proceduralised to auto send confirmation emails like "you booked a movie" or "your payment got through"
5. possibly a tool for password checking, i don't know for sure if there are any, if not i'd do password validation with loops ifs and regex, but something to ensure the user passwords are not "1234" and similat 2IQ level security threats
6. i'd definitely employ a few frontend addons/tools to make the website look nice, there should be something for a calendar, for the weekly cinema schedule data visualisation, effects on the buttons to make them stand out a bit and "move" to underscore that they are active elements, such things.

##### - You are welcome to draw a diagram (a very simple one) for the process flow to explain how it is going to work. 
![Cinema Movie Seat Booking](/movie-booking.png "Cinema Movie Seat Booking")