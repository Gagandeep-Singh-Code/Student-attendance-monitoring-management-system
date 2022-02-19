# Student attendance monitoring management system

There is a limited amount of time in which the teaching faculty in a classroom not only has to make sure that the concepts are comprehensible but rather than having the content at the focal point they have to focus on various aspects such as taking attendance, being attentive for every student and trying to deliver the content with sincerity. This puts off the balance leading to deterioration in learning, and wastage of valuable time and effort. Our project aims to make the lives of teachers easier by automatically marking students' attendance using Face recognition. It'll reduce the time wasted in taking attendance and also prevent proxy attendance. This project will also upload the attendance directly to a spreadsheet. It will not cause any disturbance during teaching and also save time. Although, it has some limitations on the distance from the students from which it can work, the use of high quality cameras and multiple cameras can reduce it. The project is quite realistic and efficient. This project uses the Microsoft Azure Face API as base resource along with Azure SQL Databases for storage and Azure SQL servers to manage databases. The project was deployed using Azure App Services. The source code is written in python using Visual Studio Code. 

Project URL: https://student-attendance-monitoring-management-system.azurewebsites.net

Demo Video URL:

(1) This project was deployed using Azure App Services. Deployed Python (Flask) web app to Azure App Service. The below image shows creation of Azure App Service under Student-attendance-monitoring-management-system.

![WebApp](https://user-images.githubusercontent.com/73172200/154810423-e57c32fa-d746-4127-b22b-95084cf8cd65.PNG)

URL: https://student-attendance-monitoring-management-system.azurewebsites.net
After Clicking on the URL you are redirected to the application.
![WebPage](https://user-images.githubusercontent.com/73172200/154810575-a165e7b4-a572-4942-bfac-87061d13c447.PNG)

The web app is not currently in working state because the database services have been stopped but the demo can be watched at this URL. Demo URL:


(2) The project's foundation depends on the Azure FaceAPI service. The below image shows creation of Azure FaceAPI resource.

![FaceAPI](https://user-images.githubusercontent.com/73172200/154810712-13783a5f-8910-420c-9dc3-07e834f5bc7e.PNG)

-Using the KEY and ENDPOINT of the FaceAPI resource, we are able to upload images, create person groups and a person ID for an invidual person belonging to a particular person group. The library used by the program is "azure-cognitiveservices-vision-face". From this library even further FaceClient library is imported for the functions related to Azure Face services. The image shows code snippet for creating a object of the FaceClient library.

![FaceAPICode1](https://user-images.githubusercontent.com/73172200/154810924-1363cb9a-bef5-46ea-a0e9-9e4617425c78.PNG)

-By navigating to https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395248 we can get details related to the person groups created using the FaceAPI. The below image displays the webpage.

![FaceAPIWebsite](https://user-images.githubusercontent.com/73172200/154811122-a92b9fc7-a7dc-4a04-9b50-2636cb407d1e.PNG)

-Different persons ID's can be found by entering the person group ID and the subscription key. The below image depicts this.

![FaceAPI2](https://user-images.githubusercontent.com/73172200/154811184-2c6fa037-6210-4db4-8773-b4fdfd198195.PNG)

-By clicking on the Add Student Record button on the web application a user can add new students' data.

![WebPage1](https://user-images.githubusercontent.com/73172200/154811394-cb1844c5-00d7-4b36-ad5c-4cbc472dc3c6.png)

-Here you add the data.

![WebPage4](https://user-images.githubusercontent.com/73172200/154811740-8a15da15-442a-4c9b-b35a-ef761007f3c6.PNG)

-After the data has been added then the changes for the new user say "user10" is reflected on FaceAPI website.

![FaceAPI3](https://user-images.githubusercontent.com/73172200/154811792-dcfb2fc7-ed72-4e19-8b95-e5b1c5c72dc0.PNG)

(3) Another Azure service used is Azure SQL Databases to store the students' data and the person ID associated with each person.Azure SQL servers resource is used to access the Azure SQL Databases resource. With the help of all the credentials of Azure SQL servers we are able to upload and store the acquired data in Azure SQL Databases. The below image shows creation of Azure SQL Databases resource.

![DB1](https://user-images.githubusercontent.com/73172200/154811862-ba28f4c1-985a-4581-b023-712e83c8b696.PNG)

-Initially when the record for "user10" has not been added there is no row for this particular user as shown below.

![DB2](https://user-images.githubusercontent.com/73172200/154811908-6fd67823-85ec-4cdd-bafd-a7cac8ddd98d.PNG)

-When the Add Student Record on the web application is pressed and the students details have been added and as you click on the submit button the camera is triggered and it automatically captures 20 frames of the person while moving its face in different directions. Let's say we add "Jimmy Kimmel" as name and "A10" as roll number and since a person group named "classroom" was already created there is no need to create new but you can wish to create new by typing yes. The below image depicts this.

![WebPage6](https://user-images.githubusercontent.com/73172200/154812443-e5fd4ea3-514e-48d4-909c-6cae32ab29ad.PNG)

-When the data is added on Add Student Record page of the web application then the changes are reflected on the database with the corresponding person ID received from the FaceAPI as shown below.

![DB3](https://user-images.githubusercontent.com/73172200/154811987-d9da5727-7682-4310-9e06-05ca96cc9d96.PNG)

(4) By clicking on the Take Attendance button on the web application a user can automatically take the attendance as the image is automatically captured and detection of faces is carried out. These faces are then uploaded to identify to which person they belong using the persoID. The below image shows Take Attendance button.

![WebPage3](https://user-images.githubusercontent.com/73172200/154812195-c92f16ab-b1b0-407c-abd6-96badba4f2e8.png)

The below image shows the web page where you will be directed after clicking on Take Attendance button.

![WebPage5](https://user-images.githubusercontent.com/73172200/154812231-5b5da3d3-a2c9-4727-b59e-f134330757ee.PNG)

When identifying a person in the image for attendance, the corresponding person IDs are acquired from the database and API call is made to identify each person and automatically create a spreadsheet highlighting the attendance recorded. The download hyperlink in the above image can be used to download the report created by the application. The below image shows the attendance image.

![attend 1 1](https://user-images.githubusercontent.com/73172200/154812452-38e8e865-0894-469d-8ee4-c39479601228.jpg)

The below image shows the final report generated.

![FinalReport](https://user-images.githubusercontent.com/73172200/154812470-f723e2aa-9497-4922-bbe8-75b3197b56da.PNG)

The below image shows the resource group "Project" and all the resource created under it.

![Project-ResourceGroup](https://user-images.githubusercontent.com/73172200/154812788-9d019832-0a04-4d61-8a5a-b97068643706.PNG)
