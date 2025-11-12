file_name= 'programming poll.txt'
print("Enter 'quit' to stop the poll")
while True:
    reason= input("why do you like programming?")
    if reason.lower() =='quit':
        break
    with open(file_name,'a') as file:
        file.write(reason + '\n')
print("Thanks for sharing your reason!")