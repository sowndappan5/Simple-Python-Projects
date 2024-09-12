# Import necessary modules
import http.server  # For implementing HTTP web servers
import socket  # Provides access to the BSD socket interface
import socketserver  # A framework for network servers
import webbrowser  # To display web-based documents to users
import pyqrcode  # To generate QR codes
import os  # To access operating system control

# Define the port for the HTTP server
PORT = 8010

# Change the working directory to the user's OneDrive folder
desktop_path = os.path.join(os.environ['USERPROFILE'], 'OneDrive')
os.chdir(desktop_path)

# Create a handler for HTTP requests
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    pass  # You can extend this class to add custom behavior if needed

# Get the hostname of the system
hostname = socket.gethostname()

# Find the IP address of the PC
def get_ip_address():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))  # Connect to a public DNS server
        return s.getsockname()[0]

# Generate a QR code for the server link
def generate_qr_code(link):
    qr_code = pyqrcode.create(link)  # Create a QR code from the link
    qr_code.svg("myqr.svg", scale=8)  # Save the QR code as an SVG file
    webbrowser.open('myqr.svg')  # Open the QR code image in the web browser

# Main function to set up and start the HTTP server
def start_http_server():
    ip_address = get_ip_address()
    server_link = f"http://{ip_address}:{PORT}"
    
    # Generate and display the QR code
    generate_qr_code(server_link)
    
    # Start the HTTP server
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print("Serving at port", PORT)
        print("Access the server using this link:", server_link)
        print("Or scan the QR code to access the server.")
        httpd.serve_forever()

# Run the main function
if __name__ == "__main__":
    start_http_server()