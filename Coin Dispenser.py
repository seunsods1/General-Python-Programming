quarter = 25
dime = 10
nickel = 5
penny = 1
item_cost = 50
count = 0
done = 0
finish = 0
return_change = 0
total_value = 0 # Money inputed into dispenser
coin_count = (0,0,0,0)
#########################################Initializing Total Coin count in dispenser#######################
total_quarter = 0
total_dime = 0
total_nickel = 0
total_penny = 0
#########################################Initializing Temp coin amounts to help eliminate invalid coins###########################
temp_quarter = 0
temp_dime = 0
temp_nickel = 0
temp_penny = 0
#######################################Change Value to Return###################################
quarter_back = 0
dime_back = 0
nickel_back = 0
penny_back = 0

temp_value = 0
coin_box_key = 0 #For access to coin box

while coin_box_key == 0:
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    item_cost = 50
    count = 0
    done = 0
    finish = 0
    return_change = 0
    total_value = 0 # Money inputed into dispenser
    coin_count = (0,0,0,0)
    
    temp_quarter = 0
    temp_dime = 0
    temp_nickel = 0
    temp_penny = 0
    #######################################Change Value to Return###################################
    quarter_back = 0
    dime_back = 0
    nickel_back = 0
    penny_back = 0
    
    temp_value = 0
    #############################################Input Coins##################################
    print "Super Neco Waves Vending Services"
    print "****************NEW PURCHASE*************"
    print 'This item costs ', item_cost
    print ('**Enter coin in form of 1,5,10,25,..')
    coin_value = input('enter coin values ')
    num_coins = len(coin_value)
    print coin_value, num_coins
    print "Is machine being services?\nType 1 if yes and Type 0 if no"
    break_cond = input("")
    coin_box_key = int(break_cond)
    if coin_box_key == 1:
        print 'Total coins in machine = ', coin_count
        print 'Total value of coins machine = ', total_value 
    
    elif coin_box_key == 0:
        ############################################Check if Any Invalid Coins####################
        while done == 0:
            count = 0
            while count < num_coins:
                current_value = coin_value[count]
                coin_amt = int(current_value)
                print 'count = ', count,'Coin Amount = ', coin_amt
                count += 1
                if coin_amt not in (quarter,dime,nickel,penny):
                   print 'An invalid coin was detected'
                   count = 0
                   coin_value = 0
                   num_coins = 0
                   coin_amt = 0
                   temp_quarter = 0
                   temp_dime = 0
                   temp_nickel = 0
                   temp_penny = 0
               
                   coin_value = input('enter coin values')
                   num_coins = len(coin_value)
                   
                elif coin_amt == 25: 
                     temp_quarter += 1
                     
                elif coin_amt == 10: 
                     temp_dime += 1
                     
                elif coin_amt == 5:
                     temp_nickel += 1
                     
                elif coin_amt == 1:
                     temp_penny += 1
            
            total_quarter += temp_quarter
            total_dime += temp_dime
            total_nickel += temp_nickel
            total_penny += temp_penny 
            coin_count = (total_quarter,total_dime,total_nickel,total_penny)
            total_value = total_quarter*25 + total_dime*10 + total_nickel*5 + total_penny*1 
            temp_value = temp_quarter*25 + temp_dime*10 + temp_nickel*5 + temp_penny*1
            print "The coin count is (q,d,n,p) ", coin_count
            print "The total number of coins in dispenser ", total_value
            
            ###########################Check if Input equals to the cost of the Item###############################
            if item_cost == temp_value:
                print 'Coin count= q,d,n,p ' ,coin_count
                print 'Total value=' ,total_value
                print "Take Item\nHave a great day"      
                print "**********End of Purchase******************"
                print ""
                print ""
                done = 1
            
            elif item_cost < temp_value:
                return_change = temp_value - item_cost
                print "The change is",(return_change),"cents"
                while finish == 0:
                    if return_change == 25:
                        quarter_back += 1
                        finish = 1
                    elif return_change > 25:
                        quarter_back += return_change/25
                        return_change = return_change%25
                        finish = 0
                    elif return_change == 10:
                        dime_back += 1
                        finish = 1
                    elif return_change > 10:
                        dime_back += return_change/10
                        return_change = return_change%10
                        finish = 0
                    elif return_change == 5:
                        nickel_back += 1
                        finish = 1
                    elif return_change > 5:
                        nickel_back += return_change/5
                        return_change = return_change%5
                        finish = 0
                    elif return_change == 1:
                        penny_back = 1
                        finish = 1
                    elif return_change > 1:
                        penny_back += return_change/1
                        finish = 1
                    else:
                        finish = 1
                        
                total_quarter -= quarter_back
                total_dime -= dime_back
                total_nickel -= nickel_back
                total_penny -= penny_back 
                coin_count = (total_quarter,total_dime,total_nickel,total_penny)
                total_value = total_quarter*25 + total_dime*10 + total_nickel*5 + total_penny*1 
                
                print "Take Item"
                print "The number of Quarters, Dimes, Nickel and Penny dispensed is",(quarter_back,dime_back,nickel_back,penny_back)
                print 'Total Coin count in vending machine after change = q,d,n,p ' ,coin_count
                print 'Total value of coin in vending machine after change =' ,total_value
                            
                print "Have a great day"
                print "**********End of Purchase******************"
                print ""
                print ""
                done = 1
            
            elif item_cost > temp_value:
                item_cost = item_cost - temp_value
                print "Not enough money please enter ", item_cost
                count = 0
                coin_value = 0
                num_coins = 0
                coin_amt = 0
                temp_quarter = 0
                temp_dime = 0
                temp_nickel = 0
                temp_penny = 0
                print 'Coin count= q,d,n,p ' ,coin_count
                print 'Total value=' ,total_value
                coin_value = input('enter coin values')
                num_coins = len(coin_value)
                
                done = 0
                print ''
                print ''
                

