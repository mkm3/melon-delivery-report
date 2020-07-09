""" """

def better_report(day_number, path):
    """ Given Day, Number of Deliveries & Produce Report """

    print()
    print("Day", day_number)

    the_file = open(path)

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("   Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

    the_file.close()



better_report(1, "um-deliveries-20140519.txt")
better_report(2, "um-deliveries-20140520.txt")
better_report(3, "um-deliveries-20140521.txt")