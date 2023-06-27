# NextLab-Django-Assignment-Evaluation
## Problem Set 1
#### Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list).
`{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}`
#### Expected o/p: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '648', '649', '650', '651', '652', '653', '3']

## Problem Set 2 - A functioning web app with API
### Please create a website - which should have two components:

#### Expose all the endpoints using Rest API, with proper permissions, authentication and documentation. Please refer to the image link - https://i.imgur.com/T0ZCO9A.png
#### Admin Facing - Where admin user can add an android app as well as the number of points - earned by user for downloading the app. (Please do not use the default Django Admin)
#### User Facing - where the user can see the apps added by the admin and the points. The user should be able to see the following fields. 
#### Signup and Login (Feel free to use any package for the same). 
#### Their Name and Profile
#### Points Earned.
#### Tasks completed. 
#### Option to upload a screenshot (which must include drag and drop) for that particular task. (Like if a user downloads a particular app), he can send a screenshot of the open app to confirm that he has indeed downloaded the app. 


## Problem Set 3
### Please answer the below questions:

#### A. Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?


#### B. In what circumstances would you use Flask instead of Django and vice versa? 
| Flask                                      | Django                                     |
| ------------------------------------------ | ------------------------------------------ | 
| Micro-framework                            | Full Stack Framework                       | 
| Lightweight But, Extensible.               | Best for large & complex applications.     | 