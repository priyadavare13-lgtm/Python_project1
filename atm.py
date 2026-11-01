balance=1000
og=balance
c_p="1234"
attempt=0
history=[]
while attempt<3:
  c=input("enter the pin:")
  if c!=c_p:
    attempt+=1
    left_attempt=3-attempt
    if attempt>2:
      print("card blocked")
    else:
      print("wrong pin, attempt_remained",left_attempt)
  else:
    break
while c==c_p:
  print("""####Menu###
  1)Balance
  2)Deposite
  3)Withdraw
  4)Exit""")
  choice=input("choices:")
  if choice=="1":
    print("check balance:",balance)
  elif choice=="2":
    deposit=int(input("amont to be deposited:"))
    if deposit>0:
      balance+=deposit
      history.append("Original balance: "+str(og)+" Deposit:"+ str(deposit)+ " new_balance : "+str(balance))
      print("new balance amount:",balance)
    else:
      print("Invalid amount")
  elif choice=="3":
    withdraw=int(input("enter amount to be taken: "))
    if withdraw>balance:
      print("amount cant be taken:")
    else:
      balance-=withdraw
      history.append(" Withdraw : "+str(withdraw)+","+" New balance : "+str(balance))
      print("new balance amount :",balance)
  elif choice=="4":
    for item in history:
      print(item)
    print("Exit:Thankyou")
    break
  else:
    print("not correct choice")