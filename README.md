## 17.04.2021

## Meme Generator 

### Overview: 

The purpose of this application is to show the skills learned in the Udacity program 'Intermediate Python':
- Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
- DRY (don’t repeat yourself) principles of class and method design.
- Working with modules and packages in Python.
- Coding best practices for style and documentation
- Code, docstrings, and comments that adhere to PEP 8 Standards


### Application Features:

- Interaction with a variety of complex filetypes (emulates data engineering role).
- Loading of quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
- Loading, manipulation, and saving of images.
- Accept dynamic user input through a command-line tool, and a web service (emulates full-stack developer role).


### Instructions for Running the Application:

1. Run main.py from command line, which gives the meme path as output.
2. For flask mode, run app.py from command line (Flask will run on port 3000).
3. Open a web browser and paste the url generated while running the app.py
4. A random meme is initially generated, but for custom meme click create and provide the necessary inputs.
5. After entering inputs, click 'create meme' to show generated meme.

### Description of Sub-Modules:

#### Quote Engine Module
This module extracts quotes from the specified file (eg: pdf, csv, txt, docx) 
and returns the list of quotes specified in it.

Dependencies:
- python-docx
- pandas
- xpdf tool

1. From the main file meme, call the Ingestor class parse function.
2. The parse function call should contain the path to the file as input.
3. As a result, it will return the list of quotes as output.

#### Meme Engine Module
This module fetches an image and adds the quote on that image and stores the new image while returning its path as output

Dependencies:
- PIL

1. From the main file meme, call the MemeEngine class with the output path as the parameter.
2. The meme function will take 'imagepath', 'body', and 'author' as parameters.
3. The function will return the path of the newly created meme.



