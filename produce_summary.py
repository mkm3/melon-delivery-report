""" """

def better_report(day_number, path):
    """ Given Day, Number of Deliveries & Produce Report """

    print()
    print("Day", day_number)
    # displays the day (day_number) of the delivery

    the_file = open(path)
    # assigning variable to our open function, passing through produce report (path)

    for line in the_file:
    # iterating through each line of the produce report

        line = line.rstrip()
        #removes the whitespace to the right of the string

        words = line.split('|')
        #item is created by split string when "|" is located in line

        melon = words[0]
        count = words[1]
        amount = words[2]
        #variables for our print statement below

        print("   Delivered {} {}s for total of ${}".format(
            count, melon, amount))

    the_file.close()



better_report(1, "um-deliveries-20140519.txt")
better_report(2, "um-deliveries-20140520.txt")
better_report(3, "um-deliveries-20140521.txt")