# TrelloSeleniumPython

## DESCRIPTION
This is a assignment to automate trello app using selenium python using pytest framework by POM model.
I have automated the application by creating lists,cards and implementing moving of cards.
I have implemented getting data from excel,generating reports and hidden password method.

## STEPS
Login into Trello.
Create a new Board. (Project)
Create 4 Lists (Not Started, In Progress, QA, Done )
Create 4 Cards. : Card 1, Card 2, Card 3, Card 4. under the list Not Started.
Move Card 2 to In Progress.
Move Card 3 to QA.
Move Card 2 under QA.
Open Card 1 and Assign it to the current logged in user and then leave a comment on Card 1 saying “I am done”

## Packages used
1)Pytest-Python framework
2)Openpyxl- to work with excel operations
3)easygui- to implement hidden password authentication
4)python-docx- to copy gnerated screenshots into word file

## TO RUN THE PROJECT

py.test --browser_name chrome --html=report.html

