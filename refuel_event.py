# this function will take a list of readings

# note that the readings should be sorted before putting them in this function
# with the oldest being the lowest index and the latest being the highest index.
# e.g.[reading1,reading2,reading3]
class REFUEL():
    def __init__(self, reading1, reading2):
        self.reading1 = reading1
        self.reading2 = reading2
        self.gallons_refueled = self.reading2 - self.reading1
    def __repr__(self):
        return str(self.gallons_refueled)

def refuel_event(readings=None):
    TRENDING_UP = False
    EVENTS = []

    for index, reading in enumerate(readings):
        # prevents the index from running out of range
        if index < len(readings) - 1:

            if readings[index+1] > (reading + 5) and TRENDING_UP == False:
                TRENDING_DOWN = False
                TRENDING_UP = True

                for index_rf, reading_rf in enumerate(readings[index:]):
                    previous_reading_index = index + (index_rf-1)
                    if reading_rf < (readings[previous_reading_index]) and TRENDING_DOWN == False:
                        print(reading_rf)
                        print(readings[previous_reading_index])
                        print("%"*20)
                        refuel = REFUEL(reading, readings[previous_reading_index])
                        EVENTS.append(refuel)
                        TRENDING_UP = False
                        TRENDING_DOWN = True
                    else:
                        continue

            else:
                continue

    return  EVENTS

test_readings = [100, 95, 80, 70, 71, 80, 85, 170, 160, 150, 140, 130, 139, 149, 159, 140, 120, ]

print(refuel_event(readings=test_readings))
