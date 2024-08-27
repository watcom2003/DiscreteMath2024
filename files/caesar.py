Message = "Meet you in the park"
MessCapital = Message.upper()
NoLetter = len(Message)
MessCypher = list(Message)

for i in range(0,NoLetter):
  newMess =  ord(MessCapital[i]) + 3
  if (newMess > ord('Z')):
    MessCypher[i] = chr(newMess - ord('Z') + 64)
  else:
    MessCypher[i] = chr(newMess)

print(str(MessCypher))
