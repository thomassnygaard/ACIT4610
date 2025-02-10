ACIT4610 - TSP City Coordinates Parser
Overview
This project processes a .tsp file, extracting the city coordinates (longitude and latitude), and prints the longitude of the first city along with all city coordinates. The script is designed to handle typical .tsp file formats and will output each city's ID, latitude, and longitude.

🛠 Requirements
Ensure you have Python 3.x or later installed on your system:

bash
Kopier
Rediger
python --version
If you don't have Python, install it from python.org.

📂 Installing Dependencies
If the project requires any external libraries, they will be listed in requirements.txt. You can install them by running:

bash
Kopier
Rediger
pip install -r requirements.txt
▶️ Run the Program
To run the script and process the .tsp file, use:

bash
Kopier
Rediger
python burma.py
📄 Sample Input/Output
Sample Input (cities.tsp):

objectivec
Kopier
Rediger
CITY 1 34.0522 -118.2437
CITY 2 40.7128 -74.0060
...
Expected Output:

yaml
Kopier
Rediger
Longitude of first city: -118.2437
City 1: Latitude: 34.0522, Longitude: -118.2437
City 2: Latitude: 40.7128, Longitude: -74.0060
...
🔑 SSH Authentication (If Needed)
If you encounter authentication issues when pulling or pushing to the repository:

Generate an SSH Key (if you haven't already):

bash
Kopier
Rediger
ssh-keygen -t ed25519 -C "your-email@example.com"
Add the SSH Key to GitHub:

bash
Kopier
Rediger
cat ~/.ssh/id_ed25519.pub
Copy the output and add it to GitHub under Settings → SSH and GPG keys.

Test the Connection:

bash
Kopier
Rediger
ssh -T git@github.com
Set Remote to SSH (if using HTTPS):

bash
Kopier
Rediger
git remote set-url origin git@github.com:thomassnygaard/ACIT4610.git
🚀 Push Changes (If Contributing)
To push your changes:

bash
Kopier
Rediger
git add .
git commit -m "Your commit message"
git push origin main
❓ Troubleshooting
If you see a 403 Permission Denied error, ensure you're logged in to the correct GitHub account.
If you have trouble running the script, double-check that Python is correctly installed.
For any other issues, feel free to open an issue on GitHub!
