def screen()
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

