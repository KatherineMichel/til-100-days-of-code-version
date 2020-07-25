'''
Changes I Made

Major changes I made:
* Rather than making updates through an editor locally, updates will be made in the browser
* Instead of using a `README.md.template`, all of the content is generated directly into the README.md from update.py
* Moved the content creation part of the program out of functions and into `main()`, leaving `read_file()` and `parse_til()` functions
* Created `HEADER` and `FOOTER` variables assigned to multiline, triple-double-quote strings
* Changed the formatting to f-strings
* Added newlines to break the markdown table into two sections and create a footer
* Implemented [Twython](https://twython.readthedocs.io/), including adding secret tokens accessed via the GitHub Action
* Added a `status` variable to the `post` dictionary and passed it into Twython to auto-tweet a status update
* Implemented a GitHub Action to run the script when a commit is made
* Formatted update.py file using [Black](https://black.readthedocs.io/)

Minor changes I made:
* `codecs` and `json` were removed, because they were unnecessary for my approach
* Changed some variable names to make the meaning more clear
* Changed `cwd` to `"."`
* Altered the excluded directories
* Excluded dotfiles from within the `categories` variable
* Changed the markdown header text and emojis; capitalized the category names
* Created a `recent_content` string
'''

'''
Program Notes

Import the Python standard libraries needed to run the code
Import the third-party libraries needed to run the code
Pass the environment variables into Twython to be used to authenticate into Twitter and tweet
Create a `HEADER` global constant variable in a triple-double-quote string containing the README.md header
Create a `FOOTER` global constant variable in a triple-double-quote string containing the README.md footer
Create a variable named `root` and assign it to the current directory
Create a list of excluded category names
Create a list of categories using directories in the root, but exclude those that are in the `excludes` list or begin with "."
Sort the categories
Create a `content` variable and assign it to an empty string; all content will eventually be appended to this
Create a `recent_content` variable and assign it to an empty string; `recent_content` will be appended to this
Create a `cat_content` variable and assign it to an empty string; `cat_content` will be appended to this
Create a `recent_tils` variable and assign it to an empty list; `tils` will be added to this and sorted to find the most recent
Set the `til` counter to 0
Append the header to the `content` string
Append the category markdown header to the `cat_content` string
Iterate through each category in the `categories` list
Create a `cat_tils` variable and assign it to an empty list; `tils` will be added to this and sorted by oldest first
Iterate through the files in each category, joining the root and category together as the path
Assigning the variable `raw` to each file, call the `read_files()` function on the file, joining the root, category, and file together as the path
Split the file up into parts
Iterate through each part in parts
Assigning the variable `til` to each part, call the `parse_til()` function on the part, stripping whitespace, and passing in category
Assign the file variable name to the `til` file name
Append each `til` to the `cat_tils` list
Append each `til` to the `recent_tils` list
Sort `tils` in `cat_tils` by date, oldest first
For each category, append the category markdown header to the `cat_content` string
Iterate through each `til` in `cat_tils`
For each `til`, add 1 to the counter
For each `til`, append the `til` markdown header to the `cat_content` string, including the `count` and `til` variables
Append a new line to the end of the category section to end the section
Sort `tils` in `cat_tils` by date, most recent first
Append the most recent tils markdown header to the `recent_content` string
Iterate through the first five `tils`
For each of the first five `tils`, append the `til` markdown header to the `recent_content` string, including `til` variables
Append a new line to the end of the most recent section to end the section
Append the `recent_content` to the `content` string
Append the `cat_content` to the `content` string
Append the footer to the `content` string
Open the README.md file and write the `content` into the README.md
Assign the `status` variable to the `status` variable of the first `til` in the `recent_tils` list
Call the `tweet()` function, passing in the status
read_files() function... passing in the file `file_path`, open up the file and read it


Assign the `tweet` variable to the `status` variable
Use Twython library to tweet the `status` update
'''
