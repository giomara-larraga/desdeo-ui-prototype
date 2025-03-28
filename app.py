from server import app  # Import the app instance
from index import app_layout  # Import layout AFTER app is initialized

app.layout = app_layout  # Set layout

if __name__ == "__main__":
    app.run(debug=True)  # Corrected function
