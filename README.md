# ACIT4610 - TSP City Coordinates Parser

## Overview
This project processes a `.tsp` file, extracting the city coordinates (longitude and latitude), and prints the longitude of the first city along with all city coordinates. The script is designed to handle typical `.tsp` file formats and will output each city's ID, latitude, and longitude.

## 🛠 Requirements
Ensure you have Python 3.x or later installed on your system:

```bash
python --version
```
## 📂 Installing Dependencies
This project does not require any external libraries. But I created an virtual environment and installed some unneeded dependencies, helping me knowing what to do when there is dependencies in the project in the future:
```bash

pip install -r requirements.txt
```

## ▶️ Run the Program To run the script and process the .tsp file, use:

```bash

python burma.py
```
## 📄 Sample Input/Output

### Sample Input (cities.tsp):

```bash

   1  16.47       96.10
   2  16.47       94.44
   3  20.09       92.54
   4  22.39       93.37
   5  25.23       97.24

```
### Expected Output:

```bash

City ID: 1, Latitude: 16.47, Longitude: 96.1
City ID: 2, Latitude: 16.47, Longitude: 94.44
City ID: 3, Latitude: 20.09, Longitude: 92.54
City ID: 4, Latitude: 22.39, Longitude: 93.37
City ID: 5, Latitude: 25.23, Longitude: 97.24
```
## 🔑 SSH Authentication (If Needed) If you encounter authentication issues when pulling or pushing to the repository:

1. Generate an SSH Key (if you haven't already):
```bash

ssh-keygen -t ed25519 -C "your-email@example.com"
```
2. Add the SSH Key to GitHub:
```bash

cat ~/.ssh/id_ed25519.pub
```
Copy the output and add it to GitHub under Settings → SSH and GPG keys.

3. Test the Connection:
```bash

ssh -T git@github.com
```
4. Set Remote to SSH (if using HTTPS):
```bash
git remote set-url origin git@github.com:thomassnygaard/ACIT4610.git
```
## 🚀 Push Changes (If Contributing) To push your changes:

```bash

git add .
git commit -m "Your commit message"
git push origin main
```
## ❓ Troubleshooting If you see a 403 Permission Denied error, ensure you're logged in to the correct GitHub account.
If you have trouble running the script, double-check that Python is correctly installed.
For any other issues, feel free to open an issue on GitHub!

## License This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements This project was developed as part of the ACIT4610 resit exam for 2025.
Special thanks to the Python community for the tools and libraries used in this project.
