# Beton Calculator

Beton Calculator is a desktop application built with Python and Tkinter that helps you calculate the material requirements (cement, sand, gravel, and water) for different concrete mix ratios based on the dimensions and quantities of columns, beams, and plates.

## Features

- Select different concrete mix ratios (K100, K150, K225, K250, K275, K300).
- Input dimensions and quantities for columns, beams, and plates.
- Calculate the total material requirements (cement, sand, gravel, and water).
- Modern and user-friendly interface using `ttkbootstrap` for better appearance.

## Requirements

- Python 3.9 or higher
- `tkinter` library
- `ttkbootstrap` library

## Installation

1. Clone the repository:

   ```sh
   https://github.com/insa21/beton_desktop/
   cd beton-calculator
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```sh
   python app.py
   ```

2. The application window will open. Select the desired concrete mix ratio and input the dimensions and quantities for columns, beams, and plates.

3. Click the "Hitung Kebutuhan Material" button to calculate the material requirements.

4. The results will be displayed in a pop-up window.

## Building an Executable (Optional)

To create an executable file for your application:

1. Ensure you have `PyInstaller` installed:

   ```sh
   pip install pyinstaller
   ```

2. Run the following command to generate the executable:

   ```sh
   pyinstaller --onefile app.py
   ```

3. The executable file will be located in the `dist` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This application uses the `ttkbootstrap` library for modern and themed UI components.
