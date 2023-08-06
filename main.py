import glob
import io
import smtplib
import datetime as dt
import random
import pandas


def get_random_letter():
    letters = []
    files = [file for file in glob.glob("letter_templates/*")]

    for file_name in files:
        with io.open(file_name, 'rb') as file:
            letters.append(file.readlines())

            random_letter = random.choice(letters)

    # Convert each byte string to a regular string
    string_list = [item.decode('utf-8') for item in random_letter]

    # Join the string_list elements to create the final string
    return ''.join(string_list)


def send_email(wish_letter, email):
    my_email = "xxxxx"
    password = "xxxxx"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{wish_letter}")


birthdays = pandas.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    today = dt.datetime.now().month, dt.datetime.now().day
    birthday_day = (row["month"], row["day"])
    if birthday_day == today:
        # send email
        letter = get_random_letter().replace("[NAME]", row["name"])
        send_email(letter, row["email"])

# ------------------------------------------------------------------------------------ #

