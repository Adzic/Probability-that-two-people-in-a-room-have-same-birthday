import streamlit as st
import random

def simulate(num_people):
    birthdays = []
    st.text("Here's what our room looks like:")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for i in range(0, num_people):
        month_choice = random.choice(months)
        if month_choice == "February":
            day = random.randint(1, 29)
        elif month_choice in ["April", "June", "September", "November"]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
        birthday = month_choice + " " + str(day)
        birthdays.append(birthday)
        st.text("Person {0}'s birthday: {1}".format(i + 1, birthday))

    calculate_probability(num_people, st)
    match = False

    for i in range(len(birthdays)):
        if find_duplicates(birthdays, birthdays[i], i, st):
            match = True
            break
    if not match:
        st.text("In our simulation, no two people have the same birthday")

def calculate_probability(num_people, st):
    if num_people < 2:
        st.text("Not enough people in the room!")
        return
    else:
        numerator = 365
        countdown = 364
        for i in range(2, num_people + 1):
            numerator = numerator * countdown
            countdown -= 1
        denominator = 365 ** num_people
        probability = 1 - numerator / float(denominator)
        rounded = round(probability * 100, 2)
        st.text("The probability that two people in a room of {0} people have the same birthday is nearly {1}%".format(num_people, rounded))

def find_duplicates(birthdays_list, birthday, index, st):
    people = []
    for i in range(len(birthdays_list)):
        if birthdays_list[i] == birthday and i != index:
            people.append(i + 1)
    if people:
        people.append(index + 1)
        st.text("In our simulation, the following people have the same birthdays:")
        for person in people:
            st.text("Person {0}".format(person))
        return True
    else:
        return False

# Streamlit UI
st.title("Birthday Simulation App")
num_people_in_room = st.number_input("Enter the number of people in the room", min_value=2, value=10, step=1)
simulate_button = st.button("Simulate")
if simulate_button:
    simulate(num_people_in_room)
