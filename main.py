from pyscript import document

# List of ALL candidates (shown on the page so users know who to type)
candidates = [
    "Cassey Mallari",
    "Brixen Rabacca",
    "Zyren Naguit",
    "Lucas Tanglao",
    "Raji Santos",
    "Matthew Saldania",
    "Sydney de Leon",
    "Andrei Viray",
    "Leeroy Torres",
    "Elisha Genove",
]

# List of the candidates who were SELECTED to join the club
# (these are only revealed when the user checks a name)
club_members = [
    "Cassey Mallari",
    "Brixen Rabacca",
    "Lucas Tanglao",
    "Raji Santos",
    "Matthew Saldania",
    "Andrei Viray",  
]

# Index 0 = name NOT on the list (False), index 1 = name IS on the list (True).
# Using the True/False result as a list index lets us pick the right
# message and style without an if/else statement or a loop.
messages = [
    "Sorry {name}, your name is not on the list.",
    "Congratulations {name}! You are now part of the ICT club.",
]

alert_styles = [
    "alert alert-danger",
    "alert alert-success",
]

# Show every candidate on the page as a chip (join, so no loop needed)
candidate_list = document.getElementById("candidate-list")
candidate_list.innerHTML = "<li>" + "</li><li>".join(candidates) + "</li>"
document.getElementById("candidate-count").textContent = f"{len(candidates)} candidates"


def check_candidate(event):
    # Get the first name and last name typed by the user
    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()

    # Combine them into one full name (Title Case so "josua ortiz" still matches)
    full_name = f"{first_name} {last_name}".title()

    # Check if the full name is in the club members list and store the result
    is_member = full_name in club_members

    # Show the message in the result area
    result = document.getElementById("result")
    result.className = alert_styles[is_member]
    result.textContent = messages[is_member].format(name=full_name)