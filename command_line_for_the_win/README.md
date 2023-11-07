- *-------------------------------------------------------*
-
-					
-	***	Command line for the win	***
-
-					
- *-------------------------------------------------------*


#### File Transfer Using SFTP

#### Open a terminal or command prompt on your local machine.

#### Establish an SFTP connection to the sandbox environment by using the following command: sftp username@hostname. Replace "username" with your actual username and "hostname" with the appropriate hostname or IP address for the sandbox environment.

#### Enter your password when prompted to authenticate and establish the SFTP connection.

### Navigate to the directory on the sandbox environment where you want to upload the screenshots using the cd command. 

##### For example cd /path/to/sandbox/directory.

### Navigate to the directory where you have the screenshots on your local machine 

##### For example: lcd /path/to/sandbox/directory. 

### Use the put command to upload the screenshots from your local machine to the sandbox environment, You can Also Provide the full path to each screenshot file you want to upload.

##### put screenshot1.png

##### put screenshot2.png

##### put screenshot3.png

#### To confirm the successful transfer of the screenshots, check the contents of the sandbox directory using the ls command: ls. This will display a list of files in the current directory on the sandbox environment, including the uploaded screenshots.

#### When you have finished transferring and verifying the screenshots, you can exit the SFTP session using the quit or exit command: quit.

#### By following these steps, you should be able to upload the screenshots from your local machine to the sandbox environment using SFTP and confirm that the transfer was successful.
