# CV Generator

## Description
A Python application that generates a professional CV in PDF format using user-provided details such as contact information, skills, work experience, and education. The application uses `Tkinter` for the graphical interface, `FPDF` for PDF creation, and `pyqrcode` for generating a QR code linking to the user’s portfolio or website.

## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PDF-CV-Generator.git
2. Navigate to the project directory: 
```bash
cd PDF-CV-Generator
```
3. Install the required dependencies:
```bash
pip install fpdf tkinter pyqrcode pypng
```
 
## Usage
1. Run the application
2. In the GUI:
    - Fill in your personal information such as name, email, phone number, and address.
    - Enter your skills, work experience, education, and a brief description of yourself in the corresponding fields.
    - Provide a link to your portfolio or website for the QR code.
    - Click Generate CV to create a PDF document of your CV with the entered information and QR code.
3. The generated PDF will include your contact information, skills, work experience, education, and a QR code linking to your portfolio.

## How it works
- Tkinter GUI: The user inputs their details in a simple graphical interface.
- PDF Generation: The application uses FPDF to create a structured CV, complete with custom fonts and layout.
- QR Code: A QR code linking to the user’s portfolio is generated using pyqrcode and included in the header of the PDF.
- Output: The generated CV is saved as a PDF in the specified directory, containing sections for contact information, skills, work experience, education, and a short bio.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

