#The Main bug object
import datetime as dt

class Bug :
    def __init__(self, ID, description, projectID, projectName, priority):
        self.id = ID
        self.description = description
        self.projId = projectID
        self.projName = projectName
        self.priority = priority
        self.solverId = None #as an init value only
        self.date_detected = dt.datetime.now()
        self.stats = "open"
    
        

    