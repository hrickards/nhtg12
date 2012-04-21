import os
import glob
import codecs
import lxml.html
import re
import csv

writer = csv.writer(open("exams.csv", "w"))
exams_set = list()

for i, infile in enumerate(glob.glob(os.path.join("data/", "*.html"))):
    print i
    with codecs.open(infile, "r", "utf-8") as f: source = f.read()

    html = lxml.html.fromstring(source)

    if not len(html.xpath("//table[@id='UCResultsTable_resultsTbl']")):
        continue

    exams = html.get_element_by_id("UCResultsTable_resultsTbl").xpath("//tr[td/@class = 'results noprint']")
    for exam in exams:
	# details = [re.sub("<br>|\n", " ", re.sub("</?td( class=\"b\")?>|</?(div|input).*>|\t", "", lxml.html.tostring(detail))) for detail in exam.xpath("td[not(input)]")]
        details = ["<a onClick='event_add($(this))'>%s</a>" % re.sub("<br>|\n", " ", re.sub("</?td( class=\"b\")?>|</?(div|input).*>|\t", "", lxml.html.tostring(detail))) for detail in exam.xpath("td[not(input)]")]
        if details not in exams_set:
            writer.writerow(details)
            exams_set.append(details)
