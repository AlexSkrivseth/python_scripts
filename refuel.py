# this function will take a list of readings

# note that the readings should be sorted before putting them in this function
# with the oldest being the lowest index and the latest being the highest index.
# e.g.[reading1,reading2,reading3]

def refuel_event(readings=None):
    TRENDING_UP = False
    EVENTS = []

    for index, reading in enumerate(readings):
        # prevents the index from running out of range
        if index < len(readings) - 1:

            # checks to see of the reading in front is higher
            if readings[index+1] > reading and TRENDING_UP == False:

                start_reading = reading
                TRENDING_UP = True
            #
            if readings[index-1] > reading and TRENDING_UP == True:
                print(reading)

                if readings[index+1] < reading:

                    end_reading = readings[index-1]
                    TRENDING_UP = False
                    EVENTS.append(end_reading - start_reading)
                if index == len(readings)-2:
                    end_reading = readings[index+1]
                    EVENTS.append(end_reading - start_reading)

    return  EVENTS

test_readings = [100, 300, 95, 80, 70, 71, 80, 85, 170, 160, 150, 140, 130, 139, 149, 159, 140, 120, 122, 129, 130, 140, 150, 145,140,135,195]

target = [200, 100, 29, 30, 60]
print("Target -  results {}".format(target))
print("Real   -  results {}".format(refuel_event(readings=test_readings)))
