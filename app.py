from contextlib import nullcontext
import os
import subprocess
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv('GOOGLE-API_KEY')

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def generate_commit_message():
    git_changes =  subprocess.run(["git", "diff", "--cached"], capture_output = True, text = True)
    return model.generate_content('''You are an expert at creating a GitHub commit message for a set of changes. 
    Here is a diff of changes we need to a commit message for: ''' + str(git_changes))

#Some data has been taken from documentation that is offered by Google. Here is the link for the same as well "https://ai.google.dev/tutorials/rest_quickstart"

if __name__ == '__main__':
    print("Your commit message is " +  generate_commit_message().text) 
    
