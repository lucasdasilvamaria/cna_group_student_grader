# CNA Box Turma Automation Script

This Python script automates logging into [CNA Box](https://www.cnabox.com.br), handling popups, navigating to the **Turma** page, and clicking the **Filtrar** button.
It is designed for teachers who want to quickly access and filter their Turma without manually interacting with the site.

---

## Features

* Reads login and password from a text file (`credentials.txt`).
* Handles two-step login using keyboard automation.
* Closes popups/modals automatically.
* Scrolls and clicks the **Filtrar** button on the Turma page.
* Uses PyAutoGUI for mouse and keyboard actions.
* Keeps the browser open until user confirms.

---

## Setup

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv .venv
```

3. **Activate the virtual environment:**

* **Windows:**

```bash
.venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source .venv/bin/activate
```

4. **Install dependencies:**

```bash
pip install selenium pyautogui
```

5. **Create `credentials.txt` in the project folder**:

```
# Write your login here:
your.email@cna.com.br
# Write your password here:
YourPassword123
```

> ⚠️ Make sure to **not commit** `credentials.txt` to GitHub. Add it to `.gitignore`:

```
credentials.txt
.venv/
```

---

## How to Run

```bash
python main.py
```

* The script will open Chrome and navigate to the CNA Box login page.
* It will automatically:

  1. Enter your login and password.
  2. Complete the secondary authentication step.
  3. Navigate to the **Turma** page.
  4. Click the **Fechar** popup button at coordinates `(920, 658)` twice, pressing **End** in between.
  5. Scroll down twice and click the **Filtrar** button at coordinates `(79, 440)`.
* The browser will stay open until you press Enter.

---

## How It Works

1. **Read credentials:**
   The script reads the login (line 2) and password (line 4) from `credentials.txt`.

2. **Launch Chrome:**
   Opens Chrome using Selenium and maximizes the window.

3. **Two-step login:**
   Uses PyAutoGUI to navigate fields with **Tab** and submit login credentials.

4. **Navigate to Turma page:**
   Goes straight to `https://www.cnabox.com.br/#/Turma`.

5. **Handle popup/modal:**
   Clicks the **Fechar** button at coordinates `(920, 658)`, presses **End**, then clicks again.

6. **Scroll and click Filtrar:**
   Scrolls down twice and clicks the **Filtrar** button at coordinates `(79, 440)`.

7. **Wait for user:**
   Browser remains open until Enter is pressed for observation or further interaction.

---

## Notes

* Coordinates are specific to screen resolution and window placement. Adjust `(920, 658)` and `(79, 440)` if needed.
* Sleep times (`time.sleep`) are used to ensure pages and animations load. You may increase them if your internet is slow.
* For safety, **never commit `credentials.txt`** to a repository.

---

## Dependencies

* [Python 3.x](https://www.python.org/)
* [Selenium](https://pypi.org/project/selenium/)
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
* Chrome browser installed locally

---

## License

This project is free to use for personal and educational purposes.
Do not share credentials publicly.
