movie = (input("Movie name: "))
rate = int(input("Rating of Movies: "))
#Create a popularity score of type float , let it be 72.65
popularity = float(input("popularity: "))
#Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if rate >=4 and popularity > 80 :
    print("Highly recommended")
#else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif rate >=3 and popularity > 70 :
    print("I recommended it . It is good")
#else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif rate <=2 and popularity >50 :
    print ("You should check it out!")
#else the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
else :
    print("Don't watch it. It is a waste of time")
    