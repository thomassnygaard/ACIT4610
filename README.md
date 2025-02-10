# ACIT4610 - TSP City Coordinates Parser

This project reads a `.tsp` file containing city coordinates, extracts the data, and prints the longitude of the first city along with all city coordinates.

## 👥 Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone git@github.com:thomassnygaard/ACIT4610.git
cd ACIT4610
```

## 🛠 Requirements

Ensure you have Python installed on your system. Check by running:

```bash
python --version
```

If you don't have Python, install it from [python.org](https://www.python.org/downloads/).

## ▶️ Run the Program

Run the script using:

```bash
python main.py
```

## 🔑 Setting Up SSH Authentication (If Needed)

If you encounter authentication issues while pulling/pushing:

1. **Generate an SSH Key** (if you haven't already):
   ```bash
   ssh-keygen -t ed25519 -C "your-email@example.com"
   ```
   Press **Enter** for all prompts.

2. **Add the SSH Key to GitHub**:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
   Copy the output and add it to GitHub under **Settings → SSH and GPG keys**.

3. **Test the Connection**:
   ```bash
   ssh -T git@github.com
   ```

4. **Set Remote to SSH (if it's using HTTPS)**:
   ```bash
   git remote set-url origin git@github.com:thomassnygaard/ACIT4610.git
   ```

## 🚀 Push Changes (If Contributing)

To push any modifications, run:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

## ❓ Troubleshooting

- If you get a **403 Permission Denied** error, ensure you're logged in to the correct GitHub account.
- If you can't run the script, check if Python is correctly installed.
- For other issues, feel free to open an issue on GitHub!

---
Made with ❤️ by [thomassnygaard](https://github.com/thomassnygaard)

