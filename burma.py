coordinates = []

# Angi stien til filen, hvis filen er i samme mappe kan du bruke navnet direkte
file_path = 'burma14.tsp'

with open(file_path, 'r') as file:
    lines = file.readlines()

def read_data_from_file(filename):
    """
    Reads a TSP file and extracts city coordinates (ID, latitude, longitude).
    
    Args:
    filename (str): The path to the TSP file.
    
    Returns:
    List of tuples: Each tuple contains (city_id, latitude, longitude).
    """
    coordinates = []
    
    try:
        # Open the file and read all lines
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Flag to start reading coordinates
        reading_coordinates = False

        # Process each line and extract city data
        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace
            if not line or line.startswith('NAME:') or line.startswith('TYPE:') or line.startswith('COMMENT'):
                continue  # Skip non-coordinate lines
            
            if line.strip() == "NODE_COORD_SECTION":
                reading_coordinates = True
                continue  # Skip the 'NODE_COORD_SECTION' line
            
            if reading_coordinates:
                if line.strip() == "EOF":
                    break  # Stop reading when we reach EOF
                # Process coordinates
                parts = line.split()
                if len(parts) < 3:
                    continue  # Skip lines that don't contain the expected number of parts
                try:
                    city_id = int(parts[0])  # City ID
                    latitude = float(parts[1])  # Latitude
                    longitude = float(parts[2])  # Longitude
                    coordinates.append((city_id, latitude, longitude))
                except ValueError:
                    continue  # Skip lines with invalid data (non-numeric values)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return coordinates


def get_target_longitude(coordinates):
    """
    Retrieves the longitude of the first city in the list.
    
    Args:
    coordinates (List of tuples): The list of city coordinates.
    
    Returns:
    float: The longitude of the first city.
    """
    if coordinates:
        return coordinates[0][2]  # Longitude of the first city
    else:
        print("No coordinates found.")
        return None


def main():
    # Specify the path to the TSP file
    file_path = 'burma14.tsp'

    # Read the data from the file
    coordinates = read_data_from_file(file_path)

    # Get the target longitude from the first city's coordinates
    target_longitude = get_target_longitude(coordinates)

    # Print the target longitude and coordinates of all cities
    if target_longitude is not None:
        print(f"Target Longitude (from City {coordinates[0][0]}): {target_longitude}")
    
    for coord in coordinates:
        print(f"City ID: {coord[0]}, Latitude: {coord[1]}, Longitude: {coord[2]}")


# Run the main function
if __name__ == "__main__":
    main()
