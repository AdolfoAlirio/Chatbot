#Adolfo Alvarenga

import sys

greeting={'hello','hi','hey','yo','hello Unique','hi Unique','Hello Unique','Hi Unique', 'hello unique','hi unique'}
thanx = {'thanks','thank you','Thank You','Thanks'}
quit={'bye','goodbye','good bye','ciao','quit','exit'}
awesome={'awesome','Awesome','Great','cool','great','Cool'}


def Unique():
    name = input("Please enter your name: ")

    print("Hello, " + name+ ", I'm Unique")
    while True:
        user = input(name+ ":")
        user.strip()

        if user in greeting:
            print("Unique: How can I help you?")
        if "trouble" in user:
            print("Unique: OK, what kind of trouble are you having")
        if "access" in user:
            print("Unique: Let me check that for you")
        if "bought" in user:
            print("Unique: Ah yes, it's been paid for, let me enable it for you")
            print("Unique: I'm sorry for the inconvenient")
            print("Unique: Anything else I can help you with?")
        if "Yes" in user:
            print("Unique: What can I help you with?")
        if "device" in user or "devices" in user:
            print("Unique: Please visit www.devicerequirements.com for a list of device requirements")
        if user in thanx:
            print("Unique: My pleasure "+ name)
        if "help" in user:
            print("Unique: What can I help you with?")
        if "support" in user:
            print("Unique: Let me check the ticket number and see whats going on")
        if "resolve" in user:
            print("Unique: I will email you with all the information on this ticket number")
        if "No" in user:
            print("Unique: Thank you for contacting us, good bye!")
            exit(0)
        if user == "My latest video isn't online":
            print("Unique: Sometimes it takes 24 hours for a video to show in your library")
        if "uploaded" and "terday" in user:
            print("Unique: Check back tomorrow and if the problem is still there we can open a ticket")
        if "ok" in user:
            print("Unique: Good Bye!")
        if "page" in user:
            print("Unique: We are working on your subscription give us 24 hours for it to be ready")
        if "lastest" and "video" and "was" in user:
            print("Unique: Yes, we are updating our system")
        if "first on my page" in user:
            print("Unique: I will set it up to show first on your page")
        if "open a support ticket" in user:
            print("Unique: Ok, lets open up a support ticket for you")
        if "cut off" in user:
            print("Unique: There might be a bad internet connection")
        if "max" in user:
            print("Unique: We appoligize for the inconvenience, but we are working on it")
        if "trim" in user:
            print("Unique: Thanks for your suggestion, we will consider it and maybe added for our next release")
        if user in quit:
            print("Unique: Good bye!")
            exit(0)
        if "payment" in user:
            print("Unique: Ok let me take you to our secure payment system")
        if "pay for" in user:
            print("Unique: Here are the instructions on how to pay www.payinstructions.com")
        if "stop my" and "to a feed" in user:
            print("Unique: Your feed subscription has been cancel\nAnything else I can hel you with?")
        if "still getting charged" and "nownews" and "cancelled" in user:
            print("Unique: I'm sorry about that, I will refund you the money back to your account on file")
        if "How much" in user:
            print("Unique: If you'll like to rent a video, each video cost 2.98. For a subscription you are looking at 9.98")
        if "$5.00" in user:
            print("Unique: Ok, lets set it up")
        if "$10.00" in user:
            print("Unique: Sounds like a good idea, lets do it!")
        if "$15.00" in user:
            print("Unique: OK, I can help you set it up")
        if "not getting paid" in user:
            print("Unique: Lets take a look at your account and see what the problem is")
        if "views have I gotten" in user:
            print("Unique: You have gotten 257 views since last week")
        if "money that hasn't been paid out" in user:
            print("Unique: yes there is some money in your account that has not been paid out\nWould you like to transfer it")
        if "Yes please" in user:
            print("Unique: Ok, I will transfer it")
        if "for kids" in user:
            print("Unique: Yes, we have a huge selection on videos for kids, check the kids section in your page or click on the kids tab")
        if "music videos" in user:
            print("Unique: A library of music videos is available under the music videos tab")
        if "cosplay" in user:
            print("Unique: All cosplay videos are available under the entertaiment tab")
        if "codingallday" in user:
            print("Unique: The lastest video of user codingallday is 'how to make a chatbot'")
        if "anything" in user:
            print("Unique: I was not able to check your account, please call our customer service at 1888-882-8888 and one of our representatitves will be able to help you")
        if "problem" in user:
            print("Unique: What kind of problem are you having?")
        if "day going?" in user:
            print('Unique: Its going good, how about yours?')
        if "is going good" in user:
            print("Unique: Great! how can I help you?")
        if user in awesome:
            print("Unique: Yes, you can find them in the kids section of your page")
        if "stream multiple" in user:
            print("Unique: You can stream in 2 devices at once with your subscription")
        if "phone works" in user:
            print("Unique: Have you check a list of compatible devices at www.devicecompatibility.com")


if __name__ == '__main__':
    Unique()


