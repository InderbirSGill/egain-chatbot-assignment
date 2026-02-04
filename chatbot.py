''' 
    eGain Package Tracker: Customer Service Chatbot
    
    Utilizing Python CLI to design a simple chatbot that assists 
    a customer in tracking down their package.

'''
def package_bot(): # Main chatbot interface 

    # Greeting the customer to the chatbot to assist them.
    print("Hello! I am eGain Package Bot! I will track your package! ")
    print("\nPlease enter the 10-digit tracking number or type 'q' to leave.")

    # User inputs
    while True:
        
        user_input = input("-> ").strip() # tracking number input 

        # EMPTY INPUT
        if user_input == "":
            print("Please enter the 10-digit tracking number or type 'q' to exit.")
            continue

        # EXIT condition
        if user_input.lower() == "q": # accounting for capatilized replies
            print("Thank you!! Goodbye :)")
            break

        # VALIDATING INPUT
        if not valid_tracking_num(user_input):
            print("Unfortunately, your input is not valid.")
            print("\nPlease enter the 10-digit tracking number or type 'q' to exit.")
            continue

        # Obtaining the status of the customer's package 
        status = get_package_status(user_input)
        package_route(status)

        # Checking to see if the customer has another package to track.
        print("\nIs there any other package you would like to track? 'y' to continue or press any key to quit.")
        another = input("-> ").strip()

        if another.lower() == "y":
            print("Please enter the 10-digit tracking number or type 'q' to exit.")
            continue
        else:
            print("Thank you!! Goodbye :)")
            break

'''       
    Validating that the tracking number that the user input meets the criteria.
'''
def valid_tracking_num(tracking_number): 
    
    return (
        tracking_number.isdigit() and len(tracking_number) == 10
        ) or (
            len(tracking_number) == 11 
            and tracking_number[:10].isdigit()
            and tracking_number[-1].lower() in ('d', 'l')
        )

''' 
    Function that simulates the status of the package.
    If at the end of a 10 digit tracking number, a d or l follow,
    then that indicates whether the packaged is delayed (d) or lost (l).
'''
def get_package_status(tracking_number): 

    tracking_number = tracking_number.lower()

    if tracking_number.endswith("d"):
        return "delayed"
    elif tracking_number.endswith("l"):
        return "lost"
    else:
        return "on_route" 

'''
    Depending on the package number input, this function will relay the package status to the customer.
'''
def package_route(status):

    if status == "delayed":
        print("It seems that your package is delayed, but should arrive soon!")
        print("We greatly apologize for the inconvience.")
    elif status == "lost":
        print("Bad news, but it seems that your package has been lost in transit.")
        print("We greatly apologize. Please redirect to egain customer service to speak to an agent.")
    else:
        print("Great news!! Your package is en route and will arrive as scheduled.")

# starting the egain package bot
package_bot()
