p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "subscribe this"
p4 = "Click this"

message = input("Enter your Comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam be aware from that")

else:
    print("This comment is not a Spam")    