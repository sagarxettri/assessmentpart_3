
REQUISITION_COUNTER = 1000

class RequisitionSystem:

    all_requisitions = [] 

    def __init__(self):
        global REQUISITION_COUNTER
        REQUISITION_COUNTER += 1
        self.requisition_id = REQUISITION_COUNTER
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.total = 0
        self.status = "Pending"
        self.approval_reference_number = "Not available"
        RequisitionSystem.all_requisitions.append(self)

    def staff_info(self):
        self.date = input("Enter the Date Of Requisition: ")
        self.staff_id = input("Enter Unique Staff ID: ")
        self.staff_name = input("Enter Staff Name: ")

    def requisitions_details(self):
        total = 0
        while True:
            price = input("Enter item price and when you are done type 'done': $ ")
            if price.lower() == "done":
                break
            try:
                total += float(price)
            except:
                print("Invalid format. Please type a number.")
        self.total = total

    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
        else:
            self.status = "Pending"

    def respond_requisition(self):
        if self.status == "Pending":
            decision = input("Manager: Approve this requisition? yes or no: ")
            if decision.lower() == "yes":
                self.status = "Approved"
                self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
            elif decision.lower() == "no":
                self.status = "Not approved"
            else:
                print("Wrong format.")
        else:
            print("This requisition is already " + self.status)

    def display_requisition(self):
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Date: {self.date}")
        print(f"Staff: {self.staff_name} ({self.staff_id})")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Ref: {self.approval_reference_number}")

    def requisition_statistics(self):
        total_submitted = len(RequisitionSystem.all_requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for req in RequisitionSystem.all_requisitions:
            if req.status == "Approved":
                approved += 1
            elif req.status == "Pending":
                pending += 1
            elif req.status == "Not approved":
                not_approved += 1

        print("\n Requisition Statistics")
        print(f"Total requisition submitted: {total_submitted}")
        print(f"Requisition Approved: {approved}")
        print(f"Requisition Pending: {pending}")
        print(f"Requisition Not Approved: {not_approved}")
        

if __name__ == "__main__":
    num_reqs = int(input("How many requisitions do you want to enter? "))


    for i in range(num_reqs):
        req = RequisitionSystem()
        print(f"\nRequisition {i+1}")
        req.staff_info()
        req.requisitions_details()
        req.requisition_approval()
        req.respond_requisition()
        req.display_requisition()
        req.requisition_statistics()
