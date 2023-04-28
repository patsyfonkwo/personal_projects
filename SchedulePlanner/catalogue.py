from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()

def get_requirements(major:str="computer science and engineering") -> list:
    """Returns list of all classes from the major requirements"""
    driver.get("https://catalogue.uci.edu/undergraduatedegrees/")
    letters = 'abcdefghijklmnpqrsu'

    lower_major = ''.join(major.split()).lower()
    alph_ord = letters.find(major[0].lower()) + 1
    major_element = []
    i = 1
    while True:
        major_sel = driver.find_element(by='xpath', value=f'//*[@id="tgl{alph_ord}"]/ul/li[{i}]/a')
        major_name = major_sel.get_property('text')
        if ''.join(major_name.split(',')[0].split()).lower() == lower_major:
            major_element.append(major_sel)
            break
        i += 1
    try:
        major_element = major_element[0]
        print(f"{major_element.get_property('text')}:")
        major_link = major_element.get_property('href')+"/#requirementstext"
        print("Link to catalogue:", major_link)
        driver.get(major_link)
        classes = [x.text for x in driver.find_elements(by="class name", value="bubblelink.code") if x.text]
        for i,x in enumerate(classes):
            try:
                int(x[0])
                classes[i] = f"{' '.join(classes[i - 1].split()[:-1])} {x}"
            except ValueError:
                pass
        return classes
    except IndexError:
        print("Major Not Found")
        return []

example_list = ['ART HIS 30', 'AFAM 70A', 'ART HIS 40B', 'ART HIS 40C', 'ART HIS 42A', 'ART HIS 42B']

def get_class_info(text : str) -> tuple:
    """Gets text file of class listing; if no class, returns empty
        string; if class returns tuple:
        (class code, string information of all listed classes available)
    """

def get_available_classes(classes:list) -> list:
    """Returns a list of tuple pairs of classes with their text info if
    they are available in the next quarter"""
    available_classes = []
    driver.get('https://www.reg.uci.edu/perl/WebSoc')
    department_names = driver.find_element(by="xpath", value="/html/body/form/table/tbody/tr[4]/td[3]/select")
    select = Select(department_names)  # department name dropdown
    for course in classes:
        # print(course)
        try:
            for dept in select.options[1:]:
                # print(select.options)
                if ' '.join(course.split()[:-1]) == dept.text[:dept.text.find('.')].strip():
                    '''What happens when the course selected is in the departments list'''
                    # print(dept.text)
                    select.select_by_visible_text(dept.text)
                    text_box = driver.find_element(by="xpath", value="/html/body/form/table/tbody/tr[5]/td[3]/input")
                    text_box.clear()
                    text_box.send_keys(course.split()[-1])
                    enter = driver.find_element(by="xpath", value="/html/body/form/p[1]/input[2]")
                    enter.click()
                    text = driver.find_element(by="xpath", value="/html/body").text
                    available_classes.append(text)
                    driver.back()
        except StaleElementReferenceException:
            '''Catching the exception that happens everytime the page needs to refresh'''
            department_names = driver.find_element(by="xpath", value="/html/body/form/table/tbody/tr[4]/td[3]/select")
            select = Select(department_names)  # department name dropdown
            continue
    return available_classes
    # class_names = [x.text[:x.text.find('.')].strip() for x in select.options][1:]
    # print(class_names)  # all departments available to select
    # departments_list = department_names.text

def close_driver():
    driver.close()

if __name__ == '__main__':
    # major = input("Enter Major: ")
    # if major:
    #     classes = get_requirements(major)
    # else:
    #     classes = get_requirements()
    #
    # print(classes)

    classes = []
    available_classes = get_available_classes(example_list)
    for cl in available_classes:
        classes.append(get_class_info(cl))
    [print(x) for x in available_classes]
    close_driver()
