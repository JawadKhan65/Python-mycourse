# error handling is useful and necessary bcz when writing a code 
# there is a exception of error

try:
    into = int(input(" Enter number table you want: "))
    for i in range(1, 11):
         print(f"{into} X {i} = {into * i}")
except Exception as e:
     print("some error occured invalid input")         
     print(e)         
    # the other one is finally which is always to be executed  
finally:
     print("boss i am executed everytime always")    
# raise keyword is used to raise an custom error 

im =  int(input(" Enter number table you want: "))
if(im > 5 or im < 9):
     raise ValueError("value should be between 5 and 9") # raising custom error
