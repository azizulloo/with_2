class Royhat:
    def __init__(self):
        self.elements = []
        self.backup = []
    
    def append(self, element):
        self.elements.append(element)
    
def ap_joy(a_royhat):
    backup = a_royhat.elements.copy()
    return a_royhat, backup

def restore_state(custom_list, backup):
    custom_list.elements = backup

ap_royhat = Royhat()
try:
    with ap_joy(ap_royhat) as (cl, backup):
        cl.append(1)
        cl.append(2)
        cl.append(3)
        raise ValueError("Xatolik yuz berdi")
except ValueError as e:
    restore_state(ap_royhat, backup)
    print("Xatolik yuz berdi. Elementlar asl holatiga qaytarilmoqda.")
else:
    print("Hech qanday xatolik yuz bermadi. Natija saqlanmoqda.")

print(ap_royhat.elements) 
