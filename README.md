# Student attendance monitoring management system

There is a limited amount of time in which the teaching faculty in a classroom not only has to make sure that the concepts are comprehensible but rather than having the content at the focal point they have to focus on various aspects such as taking attendance, being attentive for every student and trying to deliver the content with sincerity. This puts off the balance leading to deterioration in learning, and wastage of valuable time and effort. Our project aims to make the lives of teachers easier by automatically marking students' attendance using Face recognition. It'll reduce the time wasted in taking attendance and also prevent proxy attendance. This project will also upload the attendance directly to a spreadsheet. It will not cause any disturbance during teaching and also save time. Although, it has some limitations on the distance from the students from which it can work, the use of high quality cameras and multiple cameras can reduce it. The project is quite realistic and efficient. This project uses the Microsoft Azure Face API as base resource along with Azure SQL Databases for storage and Azure SQL servers to manage databases. The project was deployed using Azure App Services. The source code is written in python using Visual Studio Code. 

Project URL:
Demo Video URL:

(1)This project was deployed using Azure App Services. Deployed Python (Flask) web app to Azure App Service.

![WebApp](https://user-images.githubusercontent.com/73172200/154810423-e57c32fa-d746-4127-b22b-95084cf8cd65.PNG)










Using the KEY and ENDPOINT of the FaceAPI resource, we are able to upload images, create person groups and a person ID for an invidual person belonging to a particular person group. With the help of all the credentials of Azure SQL servers we are able to upload and store the acquired data in Azure SQL Databases.
When identifying a person in the image for attendance, the corresponding person IDs are acquired from the database and API call is made to identify each person and automatically create a spreadsheet highlighting the attendance recorded.
