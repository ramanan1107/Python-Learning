
import re

text = """
Welcome to Ocean Academy. We provide training in Python, Java,
Full Stack Development, Data Analytics, and Software Testing.

For Python course details, contact python.team@gmail.com.
For Java training, email java.support@oceanacademy.in.
Our placement team can be reached at placements2026@yahoo.com.

Students can send their resumes to student.jobs@gmail.com or
career.support@outlook.com. For technical issues, contact
tech.help123@gmail.com.

Our trainers include trainer.one@gmail.com, trainer.two@yahoo.com,
and senior.trainer@oceanacademy.in.

For admission enquiries, contact admissions@oceanacademy.in.
For general enquiries, write to info@gmail.com.
For workshop registration, email workshop2026@outlook.com.

You can also contact our partners at company.hr@abc.com,
recruitment.team@xyz.in, and support123@company.org.

Please do not send personal documents to invalid addresses such as
python@, @gmail.com, or hello@gmail.

Thank you for choosing Ocean Academy!
"""

# Extract email addresses
emails = re.findall(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    text
)

# Remove duplicate emails
emails = list(set(emails))

# Display the emails separately
print("Email Addresses Found:")

for email in sorted(emails):
    print(email)

print("Total Emails:", len(emails))
