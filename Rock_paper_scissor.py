# stone-paper-scissor
import random
list= ["rock", "paper", "scissor"]
pscore=0
cscore=0
i=1
while i<=10:
	c= random.choice(list)
	print("round", i)
	n= input("enter you choice as rock, paper, scissor :\n ")
	if n!="rock" and n!="paper" and n!="scissor":
		print("invalid choice")
		continue
	elif n=="rock" and c=="rock":
		print("Tie , Computer choice is", c)
	elif n=="rock" and c=="paper":
		cscore+=1
		print("you loose, computer choice is", c)
	elif n=="rock" and c=="scissor":
		pscore+=1
		print("you win, computer choice is", c)
	elif n=="paper" and c=="rock":
		pscore+=1
		print("you win, computer choice is", c)
	elif n=="paper" and c=="paper":
		print("tie, computer choice is", c)
	elif n=="paper" and c=="scissor":
		cscore+=1
		print("you loose, computer choice is", c)
	elif n=="scissor" and c=="rock":
		cscore+=1
		print("you loose, computer choice is", c)
	elif n=="scissor" and c=="paper":
		pscore+=1
		print("you win, computer choice is", c)
	elif n=="scissor" and c=="scissor":
		print("tie, computer choice is", c)
	print("total computer score:", cscore)
	print("your total score:", pscore)
	i+=1
if cscore==pscore:
	print("Tie")
elif cscore>pscore:
	print("you loose")
else:
	print("you win")
