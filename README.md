# Text Summarizer MLOps

A small Python package and website for NLP app that summarizes text using machine learning operations (MLOps).

## Project Structure

# The Workflow

1.Update config.yaml
2.Update params.yaml
3.Update entity
4.Update the configuration manager in src config
5.update the conponents
6.update the pipeline
7.update the main.py
8.update the app.py

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/rohitcuby/Text_Summarizer_MLOPS.git
   cd Text_Summarizer_MLOPS
   ```

2. Create a virtual environment:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```sh
   python app.py
   ```

2. Open your browser and go to `http://127.0.0.1:5000` to access the web app.

## Project Components

- **app.py**: The main Flask application file.
- **main.py**: Entry point for the project.
- **config/**: Configuration files and settings.
- **src/**: Source code for the Text Summarizer package.
- **static/**: Static files (CSS, JavaScript, images).
- **templates/**: HTML templates for the web app.
- **research/**: Jupyter notebooks for data ingestion, validation, transformation, model training, and evaluation.
- **logs/**: Log files.
- **artifacts/**: Artifacts generated during different stages of the pipeline.

## Configuration

The configuration file is located at `config/config.yaml`. Update this file to change the settings for data ingestion, transformation, validation, model training, and evaluation.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Author: Rohit Mehar  
Email: rohit.mehar.cse21@itbhu.ac.in  
GitHub: [rohitcuby](https://github.com/rohitcuby)
