import catalogue
import scheduleParser

if __name__ == '__main__':
    print("Welcome to UCI SCHEDULE PLANNER")
    while True:
        try:
            major = input("Enter your major name (no typos allowed): ")
            requirements = catalogue.get_requirements(major)
            # print(requirements)
            print("Sit tight while we fetch your available major requirement classes :)\n")
            available_classes = catalogue.get_available_classes(requirements)

            break
        except:
            print("Your request failed. You typed:", major)
            print("Please try again.\n")
    print("These are your major requirements available for the next quarter: \n")

    # print(scheduleParser.schedule_parser(available_classes[0][0]))
    for course in available_classes:
        print(scheduleParser.schedule_parser(course)[1])

    catalogue.close_driver()
