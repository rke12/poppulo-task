# Exploratory Testing report

## Introduction
This is a brief exploratory testing report for the REST API Employee service found at the below link:

http://dummy.restapiexample.com/

This document outlines an evaluation of the API tested, what was tested and how it was tested, and a retrospective of the design and implementation of the API which includes how the team could have handled this project to result with a better and more usable service as well as how it should be tested as a team going forward.

---
## Evaluation of the quality of the API


This is not a well designed or implemented API, in my opinion. It is inconsistent in successfully returning users, the data returned is inconsistent too. For example, when trying to return a specific Employee entry based on the ID given, you would be inconsistently thrown a 429 Error of 'too many requests'. This shows that the API itself is not stable and could not really be relied on to consistently pull specific data from.

As well as that, when you use a GET request to pull a specific employee, depending on the ID used, the data returned displays as NULL. However if you use the same ID number to update that record you are returned the correct data that was just sent in the PUT request. There are many reasons why this could be, it might be that data is not mapped correctly or there are some other measure(s) in place. 

There doesn't seem to be any character limits, or any checks on the backend that check the type of character being inserted per field. For example, entering symbols in the 'name' field or letters in the 'salary' and 'age' field still resulted in a succesful request when trying to add or update a record, which in my opinion would be unexpected.

From my findings there is not much in the way of handling bad requests. Part of this is it seems that the API will accept any text for the fields it's accepting which will allow for a lot of bad data to enter the system. As mentioned above, it does not always display the data that is returned. One of the only times I could purposely get a bad request returned was when entering 0 as an ID, in which case a 400 error was returned. Even with unrealistic ID values a successful request (200) was returned. 

---
## What was tested and how


The API was manually tested using Postman to send GET, PUT, POST, and DEL requests to the given API. 

My approach for each of the request types was to first send a positive request, with the data that the API would successfully consume. After that I would change the data that was in the request, varying between letters, symbols and numbers and note the response returned (positive 200 response for the extreme majority despite my expectations of errors). I would then change parameters in the URI to see what would happen with unexpected parameters. In most instances of changing the URI a 405 method not allowed error was returned.

Requests have been saved as a collection on Postman and can be sent on if needed.

---
## Retrospective on design and implementation phase


From my point of view, after an exploratory testing session on the API, it's quite clear that there was a large breakdown in communication during the early phase of designing and implementation of the API, with very limited testing done, if any.

A whole team approach from the early stages of the SDLC needs to be taken here. There are small inconsistencies (i.e. 'employee' vs 'employees' in the URI, no mapping when field names are different 'name' vs 'employee_name') resulting in data being returned as null which greatly impacts the usability of the API. As well as that there's little in the way of reducing user error when sending requests, e.g. no character limits on fields, no checks for appropriate text type per field, which down the line would generate a lot of problems for the userbase as well as bad data in the system.

If I was to approach this project again I would ensure that there is full team participation from the beginning of the project. This includes any documents (e.g. an ADR) to be reviewed by the team prior to any Refinment or Estimation sessions. With the PO and EM I would ensure that tickets were broken down into small enough tasks with clear Acceptance Criteria to elimate the risk of overcomplicating a particular task, as well as priortising the tasks into the most relevate order of completion. Full team participation for Refinement and Estimation sessions to ensure everybody is as clear as possible with the tasks to be carried out. Where possible there should be Unit Tests included in each PR to ensure sufficient test coverage. I would also ensure that there are regular testing sessions (weekly or bi-weekly) where the team will come together to test the API while it's being developed. This will give the team the opportunity to see what stage of developemt the API is at, where potential gaps are, and find any bugs and log them accordingly. Developers (incl. test engineers), should be encouraged to pair program on tasks if they get stuck on particular implementations.

Going forward with testing this particular API I think the team would greatly benefit from a Testing Guideline document and/or a Exploratory Testing Charter that they can use in future testing sessions. Perhaps even documenting the core flows needed for the API to ensure that the end result is easy to find. In my opinion, I find group Exploratory Testing/Mob sessions would be most beneficial to the team for future testing as it could allow for a more robust manual test coverage by allowing the team to leverage on teammates ideas to think of new scenarios to try. 

Given the state that the current implemetation of the API is in, it could be beneficial to the team to have an embedded QA Engineer to ensure smoother testing throughout the SDLC by doing manual checks more often, and participating in Code Reviews to ensure sufficient automation coverage with each PR, and mentoring the team with testing the API as a whole if needed.