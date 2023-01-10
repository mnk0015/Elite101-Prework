#This project was in inspiration from various chatbot designs from websites such as Playstation, Feastables Chocolate, and Optimum Wifi. 

import time

def anything_else():
  while True:
    other = input('Would you like anything else? Reply with "y" or "n". \n')
    if other == "y":
      chatbot()
    elif other == "n":
      exit()
    else: 
      print('Type only "y" or "n"')

def typing():
  print("typing...")
  time.sleep(3)

def appeal_ban():
  while True:
    try:
      email = input("SB: In order to Appeal your account, we will need your email associated with your account. Type your email. \n")
      break
    except ValueError:
      print("Invalid input. Please enter a valid email.")
  typing()
  print(f'SB: A verification code has been sent to {email}. We will continue the process after your verification. \n')
  appeal = input('Explain why you should be unbanned. \n')
  typing()

  transcript = f'Here is your recorded response below. Explain why you should be unbanned: {appeal}'
  print(transcript) 
  time.sleep(2)
  print('[Completed verification and appealed in secured website.] \n')
  time.sleep(3)
  print('We will look at the appeal and get back to you in 3-5 business days.')

  

print('------STAR GAMES CHATBOT PROTOTYPE------ \n')

name = input('SB: Please type your name. \n')
typing()
print(f'SB: Hi {name}, I am StarBot, your virtual assistant chatbot. What can I help with?')

def chatbot():
  response = int(input("Please respond with the corresponding number. \n1: Account Help \n2: Purchase Issue \n3: Contact an Agent \n"))
  response1 = 0  # Initialize response1 with a default value 
  response2 = 0
  item = ""  # Initialize item with a default value
  if response == 1:
    typing()
    print("SB: Sure, what topic would you like help with?")
    time.sleep(1)
    response1 = int(input('1: Appeal Ban \n2: Forgot Username \n3: Forgot Password \n '))  
  elif response == 2:
    typing()
    print("SB: Sure, what topic would you like help with?")
    time.sleep(1)
    response2 = int(input('1: Return Eligibilty \n2: Item Issue \n'))
  elif response == 3:
    typing()
    print("SB: Sure, We will connect you with an agent")
    time.sleep(2)
    print("connecting...")
    time.sleep(3)
    print("[Chatbot connects to customer service. Customer Service works with client. Call ends after issue is resolved.]")
    time.sleep(3)
    anything_else()
    
# Responses to choosing Account Help
  if response1 == 1:
    appeal_ban()
    anything_else()
    
  elif response1 == 2: 
    typing()
    email = input("SB: In order to change your Username , we will need your email associated with your account. Type your email. \n")
    typing()
    print(f'SB: A verification code has been sent to {email}. We will continue the process after your verification. \n')
    time.sleep(3)
    print('[Completed verification and the username changed in secured website.] \n')
    new_username= input('Please type in your new username. \n')
    confirm_username = input('Please confirm your new Username. \n')
    if new_username == confirm_username:
      print('[Completed verification and changed username in secured website.] \n')
      time.sleep(3)
      print('Your username has been successfully changed.')
      anything_else()

  elif response1 == 3: 
    typing()
    email = input("SB: In order to change your password , we will need your email associated with your account. Type your email. \n")
    typing()
    print(f'SB: A verification code has been sent to {email}. We will continue the process after your verification. \n')
    time.sleep(3)
    new_password = input("Please type in your new password. \n")
    confirm_password = input("Please confirm your new password. \n")
    if new_password == confirm_password:
      print('[Completed verification and reset password in secured website.] \n')
      time.sleep(3)
      print('Your password has been successfully reset.')
      anything_else()

# Responses to Choosing Purchase Issue
  if response2 == 1:
    item = ''
    reason = ''
    transcript1 = ''
    typing()
    print("The Return policy can be found on our website.\n")
    typing()
    item = str(input("What item are you returning? \n"))
    typing()
    reason = str(input(f"why are you returning {item}? \n"))
    transcript1 = f'You have successfully returned {item}. Below is our saved transcript from our conversation.\n TRANSCRIPT: \nWhat item are you returining: "{item}". \nWhy are you returning {item}: "{reason}"'
    print(transcript1)
    typing()
    anything_else()
    
  elif response2 == 2:
    item_issue = ''
    item_reason = ''
    transcript2 = ''
    item_issue = input('What item are you having issues with? \n')
    typing()
    item_reason = input(f"What is the issue with {item_issue}? \n")
    typing()
    print(f'You may come to our location at Star and 134 Street to claim your warranty for your "{item_issue}".') 
    typing()
    time.sleep(2)
    transcript2 = f'Below is our saved transcript from our conversation.\n TRANSCRIPT: \nWhat item are you returning?: "{item_issue}". \nWhy are you returning "{item_issue}?": "{item_reason}"'
    print(transcript2)
    typing()
    anything_else()

    
chatbot() 