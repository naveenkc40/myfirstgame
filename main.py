print("Welcome to my first game")
print("------------------------")

name = input("Enter your first name:")
age = int(input("Enter your age:"))

print("Hello",name,"You are",age,"years old")
health_points = 15


is_older = age >= 18

if (is_older == True):
    print("You are eligible to play!!!")
    wants_to_play = input("Do you want to play? ").lower()
    if(wants_to_play == "yes"):
         print("Let's play begin!!!")
         left_or_right =  input("First choice.... (Left/Right) ").lower()
         if left_or_right == "left":

              print("Bad choice:... you are in deep trouble.. you are drowning")
         
         elif left_or_right == "right":
              ans = input("Nice, Do you want gold or Money or Peace? ").lower()
              if ans == "gold":
                  print("You need to go and ask Swapna Suresh!! Where she is hiding all the gold")
                  diff_health_points = health_points + 50
                  print("Your Health Points: ", diff_health_points)

              elif ans == "money":
                    print("Check with our Cheif Minister about wealth he acquired by looting all money from people in kerala")
                    diff_health_points = health_points + 100
                    print("Your Health Points: ", diff_health_points)
              else:
                  print("Check with Padmaja CK for obituary enquiries")
                  diff_health_points = health_points - 50
                  print("Your Health Points: ", diff_health_points)
         else:
            diff_health_points = health_points - 10
            print("Wrong Choice: You are in deep trouble.. You have no desire.. and you lost 10 points..")
            print("Your Health Points: ", diff_health_points)
            

            

          
    else:
         print("Thank you!!!. You can come any time and play freely..")
    
else:
    eligible = 18
    diff_age = eligible - age
    print("You are not old enough to play. After",diff_age,"years, you can come and play this game....")
