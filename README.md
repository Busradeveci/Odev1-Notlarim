# Odev1-Notlarim - Text Completion using GPT-2

## Project Objective  
This project uses the GPT-2 model for text completion. The goal is to take a starting sentence provided by the user and generate a continuation of that text using the GPT-2 model.

## How to Use  
1. **Text Generation**: The program takes a starting sentence from the user.
2. **Model Processing**: The input text is sent to the GPT-2 model.
3. **Result**: The model completes the input text and displays the completed sentence on the screen.

## How it Works  
1. The `transformers` library and GPT-2 model are loaded.
2. The program takes user input for the starting sentence.
3. The GPT-2 model generates and completes the text, then outputs the result.

## Example Usage  
Run the script with:
```bash
$ python text_generator.py
```
Then enter a starting sentence when prompted:
```
Enter a starting sentence: The future of AI is
```
Output:
```
AI continuation: The future of AI is an exciting and rapidly evolving field. With advancements in machine learning and natural language processing, AI is poised to revolutionize many industries.
