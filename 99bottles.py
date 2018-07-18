# Simply print out the song "99 Bottles of Beer" in the terminal with a space between each verse
for i in reversed(range(1,100)):
    if i == 2:
        print("{} bottles of beer on the wall, {} bottles of beer!".format(i,i))
        print("Take one down, pass it around, {} more bottle of beer on the wall! \n".format(i-1))
        print("{} bottle of beer on the wall, {} bottle of beer!".format(i-1,i-1))
    elif i > 1:
        print("{} bottles of beer on the wall, {} bottles of beer!".format(i,i))
        print("Take one down, pass it around, {} bottles of beer on the wall! \n".format(i-1))
    else:
        print("Take one down, pass it around, no more bottles of beer on the wall!")