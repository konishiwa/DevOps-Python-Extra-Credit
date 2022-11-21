# Python Extra Credit

Create a main.py file with the following contents:

- Create a Python function that calculates the hypotenuse of a triangle using Pythagorean Theorem.
    - For more information on what Pythagorean Theorem is, please refer to the following: [https://www.calculator.net/pythagorean-theorem-calculator.html](https://www.calculator.net/pythagorean-theorem-calculator.html)
    - Test the created function by calling the function and comparing the solution to the correct answer using the website calculator linked above.
    - All inputs and outputs should be a **float** data type.
- From the foobar.txt file posted on slack create a function that:
    - Opens the file in read mode
    - Creates a new line with the “,”
    - Prints out the new file output
    - Closes the file
- Import the following library fibo and **only import the following function**: fib
    - Hint: The syntax on how to write this from python statement is in your Python assessment.
    - Create a function using the fibo library and the fib function.
- Create a function using the sys library that takes in two arguments from the user and prints both arguments out.
- Create a function with a while loop with the following:
    - Takes in an **int** user input
    - If the int is greater than -1, decrement the user input by 5.
    - Print the new user input in the while loop.
    - Once the user input is less than -1, the while loop should exit.
- Explain what Python Mitigation is. Why is this a possible security vulnerability? What is an example of a Python Mitigation?

For each function created, make sure to add comments on the purpose of the function.

Submitting your Extra Credit:

- Create a formatted README.md file in this directory with the Python Mitigation write-up and information on the repository.
    - For information on how to format md files please refer to: [https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- Create a new Repository in Github and push the contents of the directory (main.py and README.md)
    - For more information please refer to: [https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github)

Paste the link to your repository in the Extra Credit:

Acceptance Criteria for Dockerfile:

Make sure to comment each line of your Dockerfile to explain what the purpose of the line/layer is, and what actions is it executing?

**Repository Contents**:

- Create directory on your computer with the following files:
    - **jpeg**: A picture of your favorite animal in the .jpeg format.
    - **html**: An html file from the S3 static website lecture.
        - The html code is also in slack.
    - Dockerfile: The file to create your docker image.

**DockerFile Instructions**:

- Create a Dockerfile that uses the base image:
    - Base Image: nginx
    - Tag: alpine
- Run the following commands in the Dockerfile:
    - apk update
    - apk upgrade
- Copy the contents on your current directory (this directory should have all the repository contents in the section above) to the container directory:
    - /usr/share/nginx/html

**Build and Run the Docker Image**:

- Build the new docker image with the newly created Dockerfile
    - Name the docker image my-website with a tag v1
- List all the docker image using the docker command to confirm you have successfully built the container
    - **Take a screenshot of this.**
- Run the following command in your terminal to run the container:
    - docker run -d -p 80:80 my-website:v1
- Run the command:
    - curl localhost:80
    - You should see your index.html contents
    - **Take a screenshot of this.**
- Go to your browser and confirm that you can see the index.html contents
    - If you are seeing the index.html from the curl localhost:80 command and not seeing it in the browser, you may need to open up an incognito tab.
    - **Take a screenshot of this.**

Extra Credit Submission:

- Create a formatted README.md file in this directory with the three required screenshots and information on the repository.
    - For information on how to format md files please refer to: [https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- Create a new Repository in Github and push the contents of the directory (Dockerfile, index.html, animal.jpeg and README.md)
    - For more information please refer to: [https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github)
- Paste the link to your repository in the Extra Credit:
