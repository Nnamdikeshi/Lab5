import sqlite3

db_url = 'mileage.db'   # Assumes the table miles have already been created.

# Our mileage exception
class MileageError(Exception):
    pass

def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles
    If the vehicle is None or new_miles is not a positive number, raise MileageError
    '''

    if not vehicle:
        raise MileageError('Provide a vehicle name')
        # Miles need to be a number and it has to be greater than 0
    if not isinstance(new_miles, (int, float)) or new_miles < 0:
        raise MileageError('Provide a positive number for new miles')
    # Connect to DB and update with vehicle and new miles
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
    if rows_mod.rowcount == 0:
        cursor.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    conn.commit()
    conn.close()
    
def get_mileage(vehicle):
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    result_set = cursor.execute('SELECT total_miles FROM MILES WHERE vehicle = ?', (vehicle,)).fetchall()
    conn.close()
    # result should be 0 or 1
    if len(result_set) is 1:
        # The first item should be total_miles
        return str(result_set[0][0])
    #The car was not found: return 'None'
    return None
    
    # Converts input into UPPERCASE
def all_chars_upper_case(string):
    return string.upper()
    
def main():
    # Main loop for choices
    while True:
        vehicle = input("\nWelcome to mileage.py .\n\n" "To Add a new vehicles mileage, Enter the vehicles name. \n" "To Search for a vehicle, Press 's' then enter.\n" "To quit, press 'q' then enter:\n" )
        
        # If q then break
        if vehicle == "q" or vehicle == "Q":
            break
        vehicle = all_chars_upper_case(vehicle)

        if vehicle == "s" or vehicle == "S":
            vehicle = all_chars_upper_case(input("Enter name of vehicle to search for.\n" "Or.... Press 'q' then enter to exit.\n"))
            if vehicle == "q" or vehicle == "Q":
                break
            mileage = get_mileage(vehicle)
            if not mileage:
                print("Sorry... That Vehicle was not found.")
            else:
                print("Mileage for the vehicle is: \n" + mileage)
        else:
            miles = float(input('Enter new miles for %s: ' % vehicle))  # TODO input validation
            add_miles(vehicle, miles)

if __name__ == '__main__':
    main()