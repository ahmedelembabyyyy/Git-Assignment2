import threading
import time

receptionect = threading.Semaphore(5)

def enter_examinationroom(n):
    print(f"patient {n} is waiting for his turn")
    receptionect.acquire()  
    print(f"patient {n} is in the examinationroom")
    time.sleep(2)
    print(f"patient {n} is out of  the examinationroom")
    receptionect.release()  

patients = []

for i in range(10):
    Patient = threading.Thread(target=enter_examinationroom, args=(i,))
    patients.append(Patient)
    Patient.start()
