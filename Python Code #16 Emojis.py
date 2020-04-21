# emoji dictionary

message = input(">")

words = message.split(' ') # creates a lsit of inputs from the input command

emojis = {
        
      ":)" : "😊"  ,
      ";)" : "😉"
 
        
        }

output = " "
for word in words:
   output += emojis.get(word, word)
   
print(output) 