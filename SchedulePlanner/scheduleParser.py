# IMPORTANT MESSAGE: This script has been edited to only be ran from the main script
# TO RUN TESTS FROM THIS SCRIPT enumerate(text) and concatenate to returned strings w/o a '\n' char

def schedule_parser(text: str):
    """Takes the text from schedule of classes (in a line by line, text file format) and return the title of
        the class that was searched and the results of the search. Each call is for one file or one searched
        file; KEEP IN MIND THAT IN THIS SCRIPT TEXT IS A FILE (IO TEXT WRAPPER) AND IN THE MAIN FILE IT'S ONE
        BIG STRING"""

    """I would also like to mention that there is a lot of info displayed in the final result, so you can get 
       rid of some of it by conctenating to "string" until "_________________________________________________________________"
       and the continuing after the next "_________________________________________________________________"
       like a valve that opens and closes using a flag variable"""
    # print(type(text))
    string = ''
    search = ''
    title = ''
    divide = "═"*122

    flag = 0
    for i, line in enumerate(text.split('\n')):
        if "**** No courses matched your search criteria for this term." in line:
            return title + '\n' + divide, search + "\nNO COURSES AVAILABLE\n" + divide
        if i in (0, 1, 9):
            title += (line + '\n')
            continue
        if i in (8, 10, 11):
            continue
        if i in (3, 4, 5, 6):
            search += (line + '\n')

        INFO_LINE2 = "_________________________________________________________________" in line
        if INFO_LINE2:
            flag += 1

        POUND_LINE = "###" in line
        INFO_LINE = (flag % 2 == 1)

        if (not INFO_LINE) and (not POUND_LINE) and (not INFO_LINE2):
            # this is just here to declutter (this can be up to the user if they
            # want to see the info provided in this section)
            string += (line + '\n')


    return title + divide, string + divide



if __name__ == '__main__':
    no_match = open("/Users/user/Desktop/WebPages/NoMatchWebSoc.txt")
    match = open("/Users/user/Desktop/WebPages/WebSoc.txt")
    no_match_result = schedule_parser(no_match)
    print(eval(no_match_result[0]))
    print(eval(no_match_result[1]))
    print(eval(schedule_parser(match)[1]))

    #Maybe try using eval()
