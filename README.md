# CS458_Netfilix_Sign_In
SOFTWARE VERIFICATION AND VALIDATION 
2021-2022 SPRING 
PROJECT # 1 
INTRODUCTION TO TEST AUTOMATION (WEB)

For implementing this project we are using HTML and CSS for frontend and javascript for backend. Moreover for storing user to be able to login we are using Firebase which let us to store users' email and password. 

Since, one of the requirements of this project is login with Facebook account, we need a HTTPS link in order to access the Facebook link. Hence, we are using ngrok which converts out localhost into a HTTPS link. After that we add the HTPPS link to the domain of Firebase. Therefore, if you faced with the "Facebook has detected that Netflix_CS458 isn't using a secure connection to transfer information." you need use a HTTPS link and tell us to add that link to the Firebase domain.

For testing application can use the information below:

Email:
    radman@gmail.com
Password:
    123456

or

phone:
    5318199021  
password:
    123456

The two html files are present in the folder that contains this README.md file. To create a live server that will host these html files, we used a Visual Studio Code extension called Live Server. You can just right click on our html file and start a live server using this extension. You can host the html files by other means too, but Live Server extension is recommended. 

After hosting the html files, you can run the automated tests. The python file containing the tests can be found in the TestScript folder. You can run the seleniumtry.py file there to run the tests.

The tests were tested using python 3.9.10. The selenium package needs to be installed via pip. The chromedriver and geckodriver needs to be installed too. The lines 10 and 11 of the seleniumtry.py contains the codes that points to the location of these drivers on our machine. These lines need to be updated based on the location of those files on your system.