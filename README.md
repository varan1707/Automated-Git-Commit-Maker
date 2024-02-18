# Automated-Git-Commit-Tool

- The tool has been created using Python and Google's Gemini Generative AI model. 
- It essentially detects the changes that have been made between a previous commit and the next commit and lists the changes in the commit message.
- Helps you by saving your time by describing all the changes you made so you can focus on Coding and Implementation.

### How to use: 

- Essentially, all that's needed to be done to use this tool is to add the app.py and the .gitignore file to the local folder of the project you are currently working on.
- After that, once you change something in your code, you can run the git command: 'git status' to check the files that have been changed. Add the modified files using 'git add <file-name>' and  running this command will list the list of files that have been changed as the generate_commit_message function is called.
- You can edit these if you would like to make changes to the commit message or you can simply push enter and run the 'git push' command to push the commit with the automatically generated   
 commit message to GitHub.

### Iteration 2 Plan 

- Currently, all the changes made a provided in the Commit Message, however, we would like to have the more detailed version appear when PR (Pull Requests) are made to transfer code from a functional branch to the main branch or a similar repository PR.

