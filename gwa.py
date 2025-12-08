from pyscript import display, document

def general_weighted_average(e):
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)
    subject = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
    units_subject = (5, 3, 2, 1)

   #to add the sum of weighted grades and total units 
    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units

    summary = f"""{subject[0]}: {science:.0f}
{subject[1]}: {math:.0f}
{subject[2]}: {english:.0f}
{subject[3]}: {filipino:.0f}
{subject[4]}: {ict:.0f}
{subject[5]}: {pe:.0f}"""

    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')


#Clear all input fields and output containers."""
def clear_fields(e=None):
    document.getElementById('first_name').value = ""
    document.getElementById('last_name').value = ""
    document.getElementById('science').value = ""
    document.getElementById('math').value = ""
    document.getElementById('english').value = ""
    document.getElementById('filipino').value = ""
    document.getElementById('ict').value = ""
    document.getElementById('pe').value = ""
    
    document.getElementById('student_info').innerHTML = ""
    document.getElementById('summary').innerHTML = ""
    document.getElementById('output').innerHTML = ""