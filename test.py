""" x = 3
y = float(3)
print(x,y) """
""" values = [1,2.23,5,7,2,30,15]
print(values[0])
print(values[5])
 answer1 = input("")  """
""" 
answer1 = input("What's your name?")
print(f"Hello {answer1}")
answer3 = input("What day is it for you?")
print("Nice!")
answer4 = input("What's your favorite subject?")
print("ew.)")
answer5 = input("What's your favorite ice cream flavor?")
print("yumm")
answer6 = input("Who's your best friend/favorite person?")
print("cool")
answer7 = input("When do you leave school?")
print("yippee!")
print(f"{answer1} was on their way to school on a normal {answer3} when suddenly a biker on a bike passes by at what felt like 200 miles per hour. You spin and nearly fall, balancing on your feet and all of a sudden a flock of seagulls fly over you, and drops of bird dookie start raining over you. You skillfully dodge the dookie-rain because you're just that cool. Later in the day, you go to your favorite class, {answer4} and have a blast. You leave school at {answer7} and see an ice cream truck. You think to yourself 'hmmmm i really want some ice cream right now.' You make your way in line and when it's your turn, you pay for your favorite ice cream {answer5}. Then all of a sudden, a wild and coocoo {answer6} comes sneak attacking you, making you drop your delicious {answer5} flavored ice cream. Now you have no ice cream. :C)") """
""" 
def odd_or_even(x):
    if x % 2 == 0:
        print("even")
    else: 
       print("odd")
odd_or_even(19)

bill = int(input("How much was your bill?"))
values = ["great", "good", "okay", "bad"]
values = input("How was your experience here? Please answer with one of the following: great, good, okay, bad")
def total():
    if values == "great":
        print(bill * 1.25)
    if values == "good":
        print(bill * 1.20)
    if values == "okay":
        print(bill * 1.15)
    if values == "bad":
        print(bill * 1.00)
total()
 """
""" factors = int(input("Type any number(has to be a whole number"))
def number(x):
    list = []
    for i in range(1, x + 1):
        if x % i == 0:
            list.append(i)
    return(list)
print(number(factors)) """

gcf = int(input("type in one number"))
gcf2 = int(input("type in another number greater than the previous number"))
def common(x , y):
    list = []
    for i in range(1,x):
            if x % i == 0 and y % i == 0:
             list.append(i)
    return(list)
print(common(gcf , gcf2))
