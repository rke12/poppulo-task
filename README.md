# poppulo-task
Submission for Senior Test Engineer take home task at Poppulo for Rachel Egan.

---

## Introduction
The task is comprised of two parts. 

- Part 1 is a report on Exploratory testing of the given API. This is documented in the file 'part1.md'. 
- Part 2 is the automation excercise. Lemoncheesecake was the framework used for the automation task. 

    The code for the automation task can be found in the 'my_suites.py' file in the 'suites' folder. Here you will find four tests that test Employee API by sending requests to create, read, update and delete an employee. 

    Lemoncheesecake will be needed to run the tests so if you don't have it installed already, run the below command:

    ```pip install lemoncheesecake-requests```


    To run the tests, download this repo and simply run the below command in the terminal while in the project root:

    ```lcc run``` 

    The terminal will then display the results of the tests that were ran. Please bear in mind that this API is very unstable and so some tests may fail. If this is the case then try running the command again. It might take a few tries for all tests to pass.

    To view a more detailed HTML report, simply copy and paste the HTML report link that is at the bottom of the terminal output. Here you can click through the tests that were ran for more detailed output than shown in the terminal.

    There is a custom User Agent in use in the headers to avoid getting a 406 every time a request was sent.