# Premier League Teams
## Author: Kieran Armstrong
## Objective
My goal in this project is to create an interface through which users can add, remove, update and view information about players on Premier League teams. 

## Planning, Tracking and Design
For the purpose of tracking my project, I will be using an application called Trello. Trello allows me to track tasks and progress in a simple and visualised format and in one centralised location. It also contains calender and project timeline features which help with time management and ensuring time constraints are maintained.
(![trello](https://user-images.githubusercontent.com/99684374/161283554-e7cefb1a-aef4-4864-ba5d-63454010d335.png)

 
 I have used LucidChart to create my entity relationship diagram. This application allowed me to easily create diagrams to help visualise my database structure.
 
 ![ERD](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/ERD.PNG) 
 
 ## Risk Assessment
 I have created and maintained a risk assessment, adding to it as new risks were realised. As this is a relatively simple app with few dependencies, there are not many risks present
 (![RA](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/RA.png)
 
 ## CI Pipeline 
 The image below is a basic flowchart for the CI pipeline in place for this project, along with the software used at each stage.
 (![pipeline](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/ciPipeline.PNG)
 
 ## Front End 
 I have created a simple user interface that allows users to navigate to different pages.
 Users can create, read, update and delete both players and teams by navigating to the relevant page and using the data entry fields. Changes are enforced using buttons
(![home](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/home.PNG)

This page allows user to add a team
(![addTeam](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/addTeams.PNG)

This page allows user to view teams
(![viewTeam](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/viewTeams.PNG)

This page allows user to add players
(![addPlayer](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/addPlayer.PNG)
 
 This page allows user to view players
 (![viewPlayers](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/viewPlayers.PNG)
 
 ## Issues and challenges during development
 I encountered several issues throughout development. Most of these issues involved connecting to the database and ensuring data was stored correctly. These issues were overcome eventually and now all is functioning as expected.
 I think I could have expanded upon the board I used on Trello with more detail. This would give me better visualisation of how the development process would pan out.
 
 ## Testing
 When tests were run on the app, I achieved a coverage of 96% 
 (![cov](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/coverage.PNG)
 
 The tests returned 4 failed from 14 tests run
 (![test](https://github.com/Kieran-Armstrong/QAproject1/blob/main/images/test.png)
 
These are minor faults, and all of the main functions of the app work as expected.



## Future Improvements
Through future development, I would like to make the following improvements:
>Make the web interface nicer to look at through visual improvements

>Add multiple leagues, allowing the database to expand further

>Implement a table view that allows a user to select a team, which will then display all the players of that team in a neat table
 
 ## Authors
 Kieran Armstrong
