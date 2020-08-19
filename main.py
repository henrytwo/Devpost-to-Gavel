'''
Converts the export from Devpost to a Gavel friendly format.

By Henry Tu
'''

import csv
import html

with open('devpost.csv', 'r') as devpost:
    devpostCSV = csv.reader(devpost)

    with open('gavel.csv', 'w') as gavel:
        gavelCSV = csv.writer(gavel)

        for row in devpostCSV:
            submission_title = html.escape(row[0])
            submission_url = html.escape(row[1])
            submission_tagline = html.escape(row[2])

            # This is definitely the first row
            if submission_url == 'Submission Url':
                continue

            print(submission_title, submission_url, submission_tagline)

            gavelCSV.writerow([submission_title, '<a href="%s" target="_blank">%s</a>' % (submission_url, submission_url), submission_tagline])