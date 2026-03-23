import os
import time

def export_email_file(sender, recipient, subj, body_text, person_name):
    folder_name = 'local_outbox'
    os.makedirs(folder_name, exist_ok=True)
    

    timestamp = str(int(time.time()))
    formatted_name = person_name.replace(' ', '-') 
    destination = os.path.join(folder_name, f"{formatted_name}-{timestamp}.txt")
    
    email_lines = [
        f"From: {sender}\n",
        f"To: {recipient}\n",
        f"Subject: {subj}\n\n",
        f"Hi, {person_name}\n",
        f"{body_text}\n",
        "Thanks\n"
    ]
    
    with open(destination, 'w') as out_file:
        out_file.writelines(email_lines)
        
    print(f"File successfully created at: {destination}")