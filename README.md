# CS458_Netfilix_Sign_In
SOFTWARE VERIFICATION AND VALIDATION 
2021-2022 SPRING 
PROJECT # 1 
INTRODUCTION TO TEST AUTOMATION (WEB)

The two html files are present in the folder that contains this README.md file. To create a live server that will host these html files, we used a Visual Studio Code extension called Live Server. You can just right click on our html file and start a live server using this extension. You can host the html files by other means too, but Live Server extension is recommended. 

After hosting the html files, you can run the automated tests. The python file containing the tests can be found in the TestScript folder. You can run the seleniumtry.py file there to run the tests.

The tests were tested using python 3.9.10. The selenium package needs to be installed via pip. The chromedriver and geckodriver needs to be installed too. The lines 10 and 11 of the seleniumtry.py contains the codes that points to the location of these drivers on our machine. These lines need to be updated based on the location of those files on your system.