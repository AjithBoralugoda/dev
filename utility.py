#!/usr/bin/env python
from time import gmtime, strftime


TICKET_PRICE = 25
BONUS_TICKET_RATE = 9
TRAIN_MAX_SEATS = 480
LAST_TRAIN_MAX_SEATS = 640

UpwardTrain = [ 'A','B','C','D' ]
UpwardTrainTime = [ '09.00', '11.00','13.00', '15.00' ]
UpwardTrainSeats = [ 480,480,480,480 ]
UpwardTrainPassengers = [ 0,0,0,0 ]
UpwardTrainIncome = [ 0.0,0.0,0.0,0.0 ]


DownwardTrain = [ 'E','F','G','H' ]
DownwardTrainTime = [ '10.00', '12.00','14.00', '16.00' ]
DownwardTrainSeats = [ 480,480,480,640 ]
DownwardTrainPassengers = [ 0,0,0,0 ]
DownwardTrainIncome = [ 0.0,0.0,0.0,0.0 ]


def CheckSeats ( Train ):
    if Train == 'A':
        if UpwardTrainSeats[0] != 0:
            return ( UpwardTrainSeats[0] ) 
        else:
            return 0
    elif Train == 'B':
        if UpwardTrainSeats[1] != 0:
            return ( UpwardTrainSeats[1] ) 
        else:
            return 0
    elif Train == 'C':
        return ('C')
        if UpwardTrainSeats[2] != 0:
            return ( UpwardTrainSeats[2] ) 
        else:
            return 0
    elif Train == 'D':
        if UpwardTrainSeats[3] != 0:
            return ( UpwardTrainSeats[3] ) 
        else:
            return 0
    if Train == 'E':
        if DownwardTrainSeats[0] != 0:
            return ( DownwardTrainSeats[0] ) 
        else:
            return 0
    elif Train == 'F':
        if DownwardTrainSeats[1] != 0:
            return ( DownwardTrainSeats[1] ) 
        else:
            return 0
    elif Train == 'G':
        if DownwardTrainSeats[2] != 0:
            return ( DownwardTrainSeats[2] ) 
        else:
            return 0
    elif Train == 'H':
        if DownwardTrainSeats[3] != 0:
            return ( DownwardTrainSeats[3] ) 
        else:
            return 0


def UpdateSeats ( Train , Seats):
    if Train == 'A':
        if UpwardTrainSeats[0] != 0:
            if Seats <=  UpwardTrainSeats[0] and Seats <= TRAIN_MAX_SEATS:
                UpwardTrainSeats[0] = UpwardTrainSeats[0] - Seats
                UpwardTrainPassengers[0] =  UpwardTrainPassengers[0] + Seats
            return (Seats) 
        else:
            return 0
    elif Train == 'B':
        if UpwardTrainSeats[1] != 0:
            if Seats <=  UpwardTrainSeats[1] and Seats <= TRAIN_MAX_SEATS:
                UpwardTrainSeats[1] = UpwardTrainSeats[1] - Seats
                UpwardTrainPassengers[1] = UpwardTrainPassengers[1] + Seats
            return (Seats) 
        else:
            return 0
    elif Train == 'C':
        if UpwardTrainSeats[2] != 0:
            if Seats <=  UpwardTrainSeats[2] and Seats <= TRAIN_MAX_SEATS:
                UpwardTrainSeats[2] = UpwardTrainSeats[2] - Seats
                UpwardTrainPassengers[2] = UpwardTrainPassengers[2] + Seats
            return (Seats) 
        else:
            return 0
    elif Train == 'D':
        if UpwardTrainSeats[3] != 0:
            if Seats <=  UpwardTrainSeats[3] and Seats <= TRAIN_MAX_SEATS:
                UpwardTrainSeats[3] = UpwardTrainSeats[3] - Seats
                UpwardTrainPassengers[3] = UpwardTrainPassengers[3] + Seats
            return (Seats) 
        else:
            return 0
    if Train == 'E':
        if DownwardTrainSeats[0] != 0:
            if Seats <=  DownwardTrainSeats[0] and Seats <= TRAIN_MAX_SEATS:
                DownwardTrainSeats[0] = DownwardTrainSeats[0] - Seats
                DownwardTrainPassengers[0] = DownwardTrainPassengers[0] + Seats
            return (Seats) 
        else:
            return 0
    elif Train == 'F':
        if DownwardTrainSeats[1] != 0:
            if Seats <=  DownwardTrainSeats[1] and Seats <= TRAIN_MAX_SEATS:
                DownwardTrainSeats[1] = DownwardTrainSeats[1] - Seats
                DownwardTrainPassengers[1] = DownwardTrainPassengers[1] + Seats
            return (Seats) 
        else:
            return 0
    elif Train == 'G':
        if DownwardTrainSeats[2] != 0:
            if Seats <=  DownwardTrainSeats[2] and Seats <= TRAIN_MAX_SEATS:
                DownwardTrainSeats[2] = DownwardTrainSeats[2] - Seats
                DownwardTrainPassengers[2] = DownwardTrainPassengers[2] + Seats
            return (Seats) 
        else:
            return 0
    elif Train == 'H':
        if DownwardTrainSeats[3] != 0:
            if Seats <=  DownwardTrainSeats[3] and Seats <= LAST_TRAIN_MAX_SEATS:
                DownwardTrainSeats[3] = DownwardTrainSeats[3] - Seats 
                DownwardTrainPassengers[3] = DownwardTrainPassengers[3] + Seats
            return (Seats) 
        else:
            return 0

def UpdateIncome ( Train, Seats ):

    actual_tickets_charged = Seats - Seats / BONUS_TICKET_RATE 
    Income = actual_tickets_charged * TICKET_PRICE

    if Train == 'A':
            UpwardTrainIncome[0] = UpwardTrainIncome[0] + Income
            return (Income) 
    elif Train == 'B':
            UpwardTrainIncome[1] = UpwardTrainIncome[1] + Income
            return (Income) 
    elif Train == 'C':
            UpwardTrainIncome[2] = UpwardTrainIncome[2] + Income
            return (Income) 
    elif Train == 'D':
            UpwardTrainIncome[3] = UpwardTrainIncome[3] + Income
            return (Income) 
    if Train == 'E':
            DownwardTrainIncome[0] = DownwardTrainIncome[0] + Income
            return (Income) 
    elif Train == 'F':
            DownwardTrainIncome[1] = DownwardTrainIncome[1] + Income
            return (Income) 
    elif Train == 'G':
            DownwardTrainIncome[2] = DownwardTrainIncome[2] + Income
            return (Income) 
    elif Train == 'H':
            DownwardTrainIncome[3] = DownwardTrainIncome[3] + Income
            return (Income) 

def SelectTrain (): 
    answer = raw_input("Enter Your Selection: >> ")
    while answer not in { 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e','E','f','F','g','G', 'h', 'H' ,'s', 'S'}:
        answer = raw_input("Enter Your Selection: >> ")
    return answer.upper()

def EnterTrainSeats ( Train ): 
    TrainSeats = raw_input("Enter Number of Tickets: >> ")
    while ( TrainSeats.isdigit() == False ):
        print "\nPlease Enter a number :"
        TrainSeats = raw_input("Enter Number of Tickets: >> ")
    return int (TrainSeats)

def DayEndReport():
    print "\n\n\n\n\n\n\n\n\n"
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print ("Day End Summary Report for the Date: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print ("------------- UPWARD Bound ----------------------           ------------- DOWNWARD Bound ----------------------")
    print ("Train  " + "    Time " + "    Passengers " + "     Income " + "          Train  " + "  Time " + "        Passengers " + " Income ")
    print ("-----  " + "---- " + "---------- " + "--------- " + "----------  " + "--------- " + "--------------- " + "----------------------------- ")
    for i in range(4):
        line1 = str (UpwardTrain[i]) + "          "  + str (UpwardTrainTime[i]) + "     " + str (UpwardTrainPassengers[i]) + "              " + str (UpwardTrainIncome[i])
        line2 = "           " + str (DownwardTrain[i]) + "       " + str (DownwardTrainTime[i]) + "        " + str (DownwardTrainPassengers[i]) + "           " + str (DownwardTrainIncome[i])
        print (line1 + line2)

    # ------- find the max passenger train etc
    all_passengers = UpwardTrainPassengers + DownwardTrainPassengers
    all_income = UpwardTrainIncome + DownwardTrainIncome 
    max_no_of_passengers = max(all_passengers)
    max_index = all_passengers.index(max_no_of_passengers) 
    #-------- FLAG Up and Down Train based on Index
    if max_index <= 3:
        train = 'U'
    else:
        train = 'D'

    if train == 'U':
        max_passenger_train = str (UpwardTrain[max_index])
        max_income = str (UpwardTrainIncome[max_index])
    else:
        if train == 'D':
            max_passenger_train = str (DownwardTrain[3 -(7 % max_index)])
            max_income = str (DownwardTrainIncome[3 -(7 % max_index)])
    print ("Maximum Number of Passengers : " + str (max_no_of_passengers) + "   travelled in Train: " + max_passenger_train +  "  with Maximum Income of : " + str(max_income)) 
    total_passengers = sum(all_passengers)
    total_income = sum(all_income)
    print ("Total  Number of Passengers Travelled in all trains: %d   Total Income: $%.2f" %(total_passengers, total_income)) 
    return 

def ShowScreen():
 while True:   
    #--- if available seats == 0 then print 'CLOSED' -----------------------
    if UpwardTrainSeats[0] == 0:
        UpwardStatus0 = 'CLOSED'
    else:
        UpwardStatus0 = str(UpwardTrainSeats[0])
    if UpwardTrainSeats[1] == 0:
        UpwardStatus1 = 'CLOSED' 
    else: 
        UpwardStatus1 = str(UpwardTrainSeats[1])
    if UpwardTrainSeats[2] == 0:
        UpwardStatus2 = 'CLOSED'
    else:
        UpwardStatus2 = str(UpwardTrainSeats[2])
    if UpwardTrainSeats[3] == 0:
        UpwardStatus3 = 'CLOSED'
    else:
        UpwardStatus3 = str(UpwardTrainSeats[3])

    if DownwardTrainSeats[0] == 0:
        DownwardStatus0 = 'CLOSED'
    else:
        DownwardStatus0 = str(DownwardTrainSeats[0])
    if DownwardTrainSeats[1] == 0:
        DownwardStatus1 = 'CLOSED'
    else:
        DownwardStatus1 = str(DownwardTrainSeats[1])
    if DownwardTrainSeats[2] == 0:
        DownwardStatus2 = 'CLOSED'
    else:
        DownwardStatus2 = str(DownwardTrainSeats[2])
    if DownwardTrainSeats[3] == 0:
        DownwardStatus3 = 'CLOSED'
    else:
        DownwardStatus3 = str(DownwardTrainSeats[3])

    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>   W E L C O M E  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print ("-----     Train UP-   AVAILABLE SEATS  ------- Train DOWN -  AVAILABLE   SEATS")
    print ("Train Departs at 9.00 -  Enter  A:" + UpwardStatus0 + "    Train Departs at 10.00 -  Enter  E:" + DownwardStatus0)
    print ("Train Departs at 11.00 - Enter  B:" + UpwardStatus1 + "    Train Departs at 12.00 -  Enter  F:" + DownwardStatus1)
    print ("Train Departs at 13.00 - Enter  C:" + UpwardStatus2 + "    Train Departs at 14.00 -  Enter  G:" + DownwardStatus2)
    print ("Train Departs at 15.00 - Enter  D:" + UpwardStatus3 + "    Train Departs at 16.00 -  Enter  H:" + DownwardStatus3)
    print (">>>>>>>>>>>>>>>>>>>>>> PRINT DAY SUMMARY REPORT Enter  S <<<<<<<<<<<<<<<<<<<<<")

    choice = SelectTrain()
    if choice != 'S':
        if choice == 'A':
            requested_seats = EnterTrainSeats('A')
            available_seats = CheckSeats('A') 
            if available_seats != 0 and available_seats >= requested_seats: 
                UpdateSeats('A', requested_seats)
                UpdateIncome('A', requested_seats)
            else:    
                if available_seats <= requested_seats and available_seats != 0:
                    print "Not Enough Seats .. please try another Train"
                else:
                    print "CLOSED" 

        elif choice == 'B':
            requested_seats = EnterTrainSeats('B')
            available_seats = CheckSeats('B') 
            if available_seats != 0 and available_seats >= requested_seats: 
                UpdateSeats('B', requested_seats)
                UpdateIncome('B', requested_seats)
            else:    
                if available_seats <= requested_seats and available_seats != 0:
                    print "Not Enough Seats .. please try another Train"
                else:
                    print "CLOSED" 

        elif choice == 'C':
            requested_seats = EnterTrainSeats('C')
            available_seats = CheckSeats('C') 
            if available_seats != 0 and available_seats >= requested_seats: 
                UpdateSeats('C', requested_seats)
                UpdateIncome('C', requested_seats)
            else:    
                if available_seats <= requested_seats and available_seats != 0:
                    print "Not Enough Seats .. please try another Train"
                else:
                    print "CLOSED" 

        elif choice == 'D':
            requested_seats = EnterTrainSeats('D')
            available_seats = CheckSeats('D')
            if available_seats != 0 and available_seats >= requested_seats: 
                UpdateSeats('D', requested_seats)
                UpdateIncome('D', requested_seats)
            else:    
                if available_seats <= requested_seats and available_seats != 0:
                    print "Not Enough Seats .. please try another Train"
                else:
                    print "CLOSED" 

        elif choice == 'E':
            requested_seats = EnterTrainSeats('E')
            available_seats = CheckSeats('E') 
            if available_seats != 0 and available_seats >= requested_seats: 
                UpdateSeats('E', requested_seats)
                UpdateIncome('E', requested_seats)
            else:    
                if available_seats <= requested_seats and available_seats != 0:
                    print "Not Enough Seats .. please try another Train"
                else:
                    print "CLOSED" 

        elif choice == 'F':
            requested_seats = EnterTrainSeats('F')
            available_seats = CheckSeats('F')
            if available_seats != 0 and available_seats >= requested_seats: 
                UpdateSeats('F', requested_seats)
                UpdateIncome('F', requested_seats)
            else:    
                if available_seats <= requested_seats and available_seats != 0:
                    print "Not Enough Seats .. please try another Train"
                else:
                    print "CLOSED" 

        elif choice == 'G':
            requested_seats = EnterTrainSeats('G')
            available_seats = CheckSeats('G')
            if available_seats != 0 and available_seats >= requested_seats: 
                UpdateSeats('G', requested_seats)
                UpdateIncome('G', requested_seats)
            else:    
                if available_seats <= requested_seats and available_seats != 0:
                    print "Not Enough Seats .. please try another Train"
                else:
                    print "CLOSED" 

        elif choice == 'H':
            requested_seats = EnterTrainSeats('H')
            available_seats = CheckSeats('H')
            if available_seats != 0 and available_seats >= requested_seats: 
                UpdateSeats('H', requested_seats)
                UpdateIncome('H', requested_seats)
            else:    
                if available_seats <= requested_seats and available_seats != 0:
                    print "Not Enough Seats .. please try another Train"
                else:
                    print "CLOSED" 
    else:
        DayEndReport()
        break

