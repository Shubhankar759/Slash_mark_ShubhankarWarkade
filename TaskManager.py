import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import random

Task = pd.DataFrame(columns =['Description','Priority'])

try:
    Task = pd.read_csv(r"C:\Users\shubh\Slash_Mark_Internship_Projects\Task.csv")
except FileNotFoundError:
    print("ERROR:File Not Found in System")

def save_task():
   Task.to_csv( r"C:\Users\shubh\Slash_Mark_Internship_Projects\Task.csv",index=False)
   
    
def add_task(description, priority):
    global Task  # Declare tasks as a global variable
    new_task = pd.DataFrame({'Description': [description], 'Priority': [priority]})
    Task = pd.concat([Task, new_task], ignore_index=True)
    save_task()
    
def remove_task(description):
    global Task
    print("Removing Task ",description)
   
    Task = Task[Task['Description'] != description]
    save_task()

def list():
    if Task.empty:
        print("No task present")
    else:
        print(Task)

while True:
 print("\nWelcome to Task Manager")
 print("Enter 1 to Add Task")
 print("Enter 2 to Remove Task")
 print("Enter 3 to List Task")
 print("Enter 4 to Recommand Task")
 print("Enter 5 to EXIT")
 chocie= input("Select One: ")
 
 if chocie=="1":
     description = input("Enter Description to the task: ")
     priority = input("Enter Priority (High/Medium/Low):").capitalize()
     add_task(description,priority)
     print("Task added")
     
 elif chocie=="2":
     description = input("Enter Description of Task to be removed: ")
     remove_task(description)
     print("Task Removed")
      
 elif chocie=="3":
     list() 
 elif chocie=="4":
     print("Hello")
     
 elif chocie=="5":
     print("Exiting Task Manager")
     break 
 
 else: print("Invalid Option Enter Valid Option")
 
 
 
 
