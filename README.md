# country_indicator

Script to indicate 
your country based on your external ip address
Indication in system tray

For PRETTY_NAME="Ubuntu 22.04.2 LTS"


The gi module is used to access the GObject Introspection API, which allows Python code to interact with libraries that have been compiled for use with other programming languages. In this code snippet, the gi module is used to access the GTK and AppIndicator3 libraries, which are used to create a system tray icon that displays the user's country code.

The requests module is also imported to make an HTTP request to the ipinfo.io/country API endpoint to retrieve the user's country code.


---
How to Run a Python Script as an App in Ubuntu

There are a few different ways to run a Python script as an app in Ubuntu, depending on your specific needs. Here are a few options:

    Create a desktop entry: You can create a .desktop file in the /usr/share/applications/ directory to create a launcher for your Python script. The contents of the file should look something like this:

[Desktop Entry]
Type=Application
Name=My Python Script
Exec=/usr/bin/python3 /path/to/my/script.py
Icon=/path/to/my/icon.png
Terminal=false

Replace My Python Script with the name of your app, /usr/bin/python3 with the path to your Python interpreter, /path/to/my/script.py with the path to your Python script, /path/to/my/icon.png with the path to your app's icon (if you have one), and false with true if your script requires a terminal window. Save the file and your app should now appear in your applications menu.

Use PyInstaller: PyInstaller is a tool that can package a Python script and its dependencies into a standalone executable file. To use PyInstaller, you'll need to install it first:

pip install pyinstaller

Once PyInstaller is installed, you can package your Python script into an executable file like this:

    pyinstaller --onefile /path/to/my/script.py

    This will create a standalone executable file in the dist/ directory. You can then run this file like any other app.

    Use a Python IDE: If you're using a Python IDE such as PyCharm, you can create a run configuration for your Python script and then run it from within the IDE. This can be a convenient way to test and debug your app during development.


These are just a few of the ways you can run a Python script as an app in Ubuntu. The best option for you will depend on your specific needs and preferences.
