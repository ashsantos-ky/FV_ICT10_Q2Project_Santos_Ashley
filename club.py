from pyscript import display, document

#club information to be displayed when submit is clicked
club = [
    {
        'name': 'Science Club',
        'description': 'A club for interesting science activities',
        'meeting_time': 'Tuesdays (3:00pm - 4:00pm), Fridays (2:00pm - 3:00pm)',
        'room_number': '404',
        'advisor': 'Ms. Jameelyn Maramag',
        'members': 18,
        'category': 'Academic'
    },
    {
        'name': 'Math Club',
        'description': 'To challenge and improve math skills',
        'meeting_time': 'Monday 2:30-4:30 Pm',
        'room_number': '404',
        'advisor': 'Mr. Gabuya',
        'members': 16,
        'category': 'Academic'
    },
    {
        'name': 'Dance Club',
        'description': 'To perform and entertain through dance',
        'meeting_time': 'Tuesday 3:00 PM',
        'room_number': 'Theatro',
        'advisor': 'Mr. Cases',
        'members': 18,
        'category': 'Non-Academic'
    },
    {
        'name': 'Band Club',
        'description': 'Play instruments and perform music',
        'meeting_time': 'Monday,Tuesday, and Wednesday 3-4:30 PM',
        'room_number': 'Marching Band Room',
        'advisor': 'Mr. Alumno',
        'members': 42,
        'category': 'Non-Academic'
    },
    {
        'name': 'Volleyball Club',
        'description': 'To compete against other schools and tournament',
        'meeting_time': 'Wednesday 3:00 PM',
        'room_number': 'Quadrangle',
        'advisor': 'Mr. Ruiz',
        'members': 24,
        'category': 'Non-Academic'
    },
    {
        'name': 'Basketball Club',
        'description': 'To compete against other schools and tournaments',
        'meeting_time': 'Monday 3:00-5 PM',
        'room_number': 'Quadrangle',
        'advisor': 'Mr. Ruiz',
        'members': 16,
        'category': 'Non-Academic'
    }
]

def show_club_info(selected_index):
    club_index = int(selected_index)
    selected_club = club[club_index]

#the message that will be displayed when club is submitted 
    message = f"""
    <div class='result'>Club Information:</div>
    <div class='club-info'>
        <strong>Name:</strong> {selected_club['name']}<br>
        <strong>Description:</strong> {selected_club['description']}<br>
        <strong>Meeting Time:</strong> {selected_club['meeting_time']}<br>
        <strong>Room Number:</strong> {selected_club['room_number']}<br>
        <strong>Advisor:</strong> {selected_club['advisor']}<br>
        <strong>Number of Members:</strong> {selected_club['members']}<br>
        <strong>Category:</strong> {selected_club['category']}<br>
    </div>
    <div class='result-title notes-title'>club form</div>
    """
    
    output = document.getElementById("output")
    output.innerHTML = message
def on_button_click(event):
    selected_value = dropdown.value
    show_club_info(selected_value)

#to make the button functional
button = document.getElementById("button")
dropdown = document.getElementById("club-select")
button.onclick = on_button_click