🌍 Coordinate Converter

# Coordinate-Converter-v1.00.0
Coordinate Converter v1.0.0 is a user-friendly tool for converting geographic coordinates between Decimal Degrees (DD), Degrees and Minutes (DM), and Degrees, Minutes, and Seconds (DMS). Ideal for mapping, 
navigation, and research, it ensures quick, accurate conversions with an intuitive interface for seamless use.

**Coordinate Converter is a standalone app that requires no installation to use.** 


Background

Coordinate Converter is a small project that come about after finding a need to quickly and easily convertt GPS coordinates  between the different formats. I frequently work with maps and mapping applications as a hobby, often referencing historic maps that use different coordinate formats. I’ve found myself needing to convert between Decimal Degrees (DD), Degrees & Minutes (DM), and Degrees, Minutes, Seconds (DMS) regularly, which led me to create this tool for quick and accurate conversions.

One feature that I have implemented in this app is a simiple input/output format. Many coordinate converters require separate input fields for latitude and longitude, but that's not always practical when copying coordinates from various sources. With this in mind, I designed this app with a single input field, allowing users to paste an entire coordinate string, press convert, and get the result instantly. The app still supports converting individual values as well as multiple coordinate sets at once.
________________________________________
🔹 Overview
The Coordinate Converter allows you to easily convert coordinates between:
✅ Decimal Degrees (DD) → 35.87972
✅ Degrees & Minutes (DM) → 35°52.783′ N
✅ Degrees, Minutes, Seconds (DMS) → 35°52′47″ N
________________________________________
📌 How to Use the Coordinate Converter
1️. Enter a Coordinate (or a Pair)
•	Open the app and type your coordinates into the input box.
•	You can enter any format:
o	35.87972 → Decimal Degrees
o	35°52.783′ N → Degrees & Minutes
o	35°52′47″ N → Degrees, Minutes, Seconds
💡 Want to convert two coordinates at once?
Just separate them with a comma:
35°52.85′ N, 84°30.517′ W
2️. Use the Symbol Buttons (Optional)
•	If you don’t have the °, ′, or ″ symbols on your keyboard, just click the symbol buttons below the input box.
•	They will insert the symbols at your cursor’s position automatically.
3️. Choose Your Output Format
•	Below the input, you’ll see a dropdown menu.
•	Select the format you want the conversion to be displayed in:
o	DD → 35.87972
o	DM → 35°52.783′ N
o	DMS → 35°52′47″ N
4️. Click "Convert"
•	Press the "Convert" button to generate the converted coordinates in your chosen format.
•	If you entered a pair of coordinates, both will be converted at once.
5️. Copy the Results
•	Below the result, there’s a "Copy" button—click it to copy the converted coordinates to your clipboard.
•	You can paste them anywhere you need!
________________________________________
💡 Why Use This?
•	Provides instant coordinate conversions
•	Supports copying results with a single click
•	No installation required – just run the .exe
•	Easy-to-use GUI with symbol buttons
________________________________________
📥 Download & Installation
📌 Download the App
💻 Running the Program
•	Windows: Download and double-click Coordinate_Converter.exe
•	Mac/Linux: Currently, only available for Windows.
🛠️ Using Python?
If you prefer running the script directly:
git clone https://github.com/your-github-repo-name.git
cd coordinate_converter
python coordinate_converter.py
(Requires Python 3.10+ and Tkinter.)
________________________________________
🎨 User Interface (UI Preview)
Here’s what the app looks like:

(Replace with actual UI screenshot.)
🔹 Features at a Glance:
•	Enter coordinates in any format
•	Use symbol buttons for °, ′, and ″
•	Select output format from the dropdown
•	Copy results with a single click
________________________________________
🚀 Examples & Supported Formats
--------------------------------------------------------------------
Input Format			| Example Input	| Converted Output
--------------------------------------------------------------------
Decimal Degrees (DD)		| 35.87972	| 35°52′47″ N
Degrees & Minutes (DM)		| 35°52.783′ N	| 35.87972
Degrees, Minutes, Seconds (DMS)	| 35°52′47″ N	| 35.87972
____________________________________________________________________

💡 FAQ & Troubleshooting
🔹 Why is my antivirus flagging the .exe as a threat?
This is a false positive because the .exe was packaged using PyInstaller. Add it to your antivirus exceptions list to prevent issues.
🔹 Can I run this without installing Python?
Yes! The .exe is fully standalone. No installation required.
🔹 Does this work on Mac or Linux?
Currently, this version is Windows-only. A cross-platform version is planned.
🔹 I found a bug! How can I report it?
Open an issue on GitHub or contact the developer.
________________________________________
👨‍💻 Contribute
Want to improve this project? Fork the repository and submit a pull request!
sh
Copy code
git clone https://github.com/your-github-repo-name.git
cd coordinate_converter
python coordinate_converter.py
________________________________________
📜 License
📜 This project is licensed under the MIT License, meaning you’re free to use, modify, and distribute it.
🚀 Made with ❤️ by [Your Name]
🔗 Website/GitHub: [Your Repo Link Here]

