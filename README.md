# MERAR

MERAR stands for Medical Record Automatic Reader.
This application reads certain fields values of a specific medical record model using Tesseract OCR engine and automatically renaming the file with the extracted information.

## About

This is a project that I made back in 2019 when I was working on a project that involved organizing and scanning thousands of medical records. 
Since I had to open file by file to get specifics informations about the pacient in order to rename the file, I saw an opportunity to automate this process.
These are the currently implemented features:

- Access a specific repository from where the medical records are stored,
- Read each file searching for three specific fields:
  - Pacient name,
  - Type of exam,
  - Date of exam.
- Rename file according to a pattern specified by the product owner.

## Technologies

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
