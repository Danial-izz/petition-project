# Word Frequency Extraction - Python

<br> Hi Everyone, Please find this as an instruction on running the script that will take an input file in the form of Image A and output it into a csv file in the form of Image B. A brief overview on the approach will also be introduced. <br>

<br>Image A<br>
<img width="735" alt="Screenshot 2023-06-12 at 07 57 31" src="https://github.com/Danial-izz/petition-project/assets/79645492/1653c201-128b-46b8-a05c-4cf1b104f35b">


<br>Image B <br>
<img width="881" alt="Screenshot 2023-06-12 at 07 58 59" src="https://github.com/Danial-izz/petition-project/assets/79645492/2d5f97ab-7f07-47c2-8564-c34e34a52477">

## Brief Overview
<br> This exercise was conducted purely on python using pandas and nltk library to perform data manipulation and also text preprocessing. The exercise was to extract the top 20 word frequency that has more than 5 letters of word from a JSON formatted file and exported it into a csv file. This exercise would simulate an ETL pipeline of transforming an input file into the required output file. This exercise also leverage some of software dev best practices by introducing modularity and containerization. By sectioning the code into modules, it allows the ease of reusability and also when performing testing and debugging. Docker is introduced to get rid of the scenario where "if it works on my laptop, it should work on yours too!". There is only one test case being introduced in this exercise which is when performing the preprocessing step. A simple unit test was introduced using pytest as the library. 
<br>

## Instructions.
<br>With Docker:<br>
<br>To run it with docker, please just build an image by running these line of code one-by-one. Replace the image-name & container-name based on your liking
<br>I have not specified any path for the output thus it could be found on the app directory of the docker container. 
```
docker build -t image-name . 
docker run --name container-name image-name
```
<br>Without Docker:
To run it without docker, please perform the code below on the root directory of the project:
```
python main.py
```
<br>Running Test:
To run the test, please perform the code below on the root directory of the project:
```
pytest
```
<br>

## Improvement
Upon writing this document, further improvement can be done to simulate an end-to-end pipeline. One of them would be by introducing another test to see if the code only count words that are more than 5 letters. visually, this can be seen that the code can do the job but in production settings, a test like this should be introdcued to make sure the code will always perform as it is intended to. The usage of pyspark is also another set of improvement as it can handle large-scale data processing. However, pandas was used for its ease of usage as a one time task. 
