patients = []
recent_stack = []

def add_patient(patient):
    patients.append(patient)
    recent_stack.append(patient)

def get_patients():
    return patients

def get_recent():
    return recent_stack[-5:]