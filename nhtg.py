from selenium import webdriver
import codecs

j = 0

driver = webdriver.Chrome()
driver.get("http://www.education.gov.uk/comptimetable/search.aspx")
driver.find_element_by_name("ctl00$mainContent$accept").click()
years = driver.find_element_by_name("UCBasicSearch$ddSession").find_elements_by_tag_name("option")
for i in range(len(years)):
    years = driver.find_element_by_name("UCBasicSearch$ddSession").find_elements_by_tag_name("option")
    years[i].click()
    driver.find_element_by_name("UCBasicSearch$showAllSub").click()
    driver.find_element_by_name("UCBasicSearch2$UCSearchByLetter$btnAll").click()
    subjects = driver.find_elements_by_xpath("//input[starts-with(@name, 'UCBasicSearch2$UCPostBackSubjectList$subjectsRepeater$ctl') and contains(@name, '$SubjectList$ctl') and contains(@name, '$subjectName')]")
    for i in range(len(subjects)):
        subjects = driver.find_elements_by_xpath("//input[starts-with(@name, 'UCBasicSearch2$UCPostBackSubjectList$subjectsRepeater$ctl') and contains(@name, '$SubjectList$ctl') and contains(@name, '$subjectName')]")
        subjects[i].click()
        num_nexts = 0
        
        while True:
            with codecs.open("data/%d.html" % j, "w", "utf-8") as f: f.write(driver.page_source)
            j += 1

            if not len(driver.find_elements_by_name("UCResultsTable$topNavigation$btnNext")): break
            driver.find_element_by_name("UCResultsTable$topNavigation$btnNext").click()
            num_nexts += 1

        for n in range(num_nexts+1): driver.back()
    for n in range(2): driver.back()
