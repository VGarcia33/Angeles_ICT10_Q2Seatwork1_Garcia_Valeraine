from pyscript import document, display

club_members= ["Thomas Greene","Newt Isaac","Minho Park","Teresa Agnes", "Brenda Grace"]
 
def check_members(event):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    full_name = first_name + " " + last_name 

    said_member = full_name in club_members

    message= document.getElementById("message")


    if said_member:
        message.innerHTML = f"Congratulations!!! {full_name}, you are now part of the ICT Club!!"

    else:
        message.innerHTML = f"Sorry,  {full_name}, you are not a member of the ICT Club."







  
    
        