from pyscript import document, display

def checkmember(e):
    
    club_members = ["georgina banal", "adriana averilla", "isaias berdin", "cameron bufford", "carlos david"]
    
    first_name = document.getElementById("firstname").value.strip().lower()
    last_name = document.getElementById("lastname").value.strip().lower()
    full_name = f"{first_name} {last_name}"
    
    confirm_member = full_name in club_members
    
    message = ('Unfortunately, your name is not on the list.' , 'Congratulations! You are now part of the Theatre club. "Movies will make you famous... but theatre will make you good." — Terrence Mann')
    
    document.getElementById("output1").innerHTML = message[confirm_member]