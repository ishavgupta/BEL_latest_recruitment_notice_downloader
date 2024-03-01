# BEL_latest_recruitment_notice_downloader

# BEL India Recruitment PDF Downloader

This Python script automates the process of downloading the latest recruitment advertisement PDF from the BEL India website. It uses Selenium for web scraping and requests for downloading the PDF.


# Following is the algorithm used for downloading PDF:

Feature: Download Latest BEL Recruitment PDF
    As a user
    I want to download the latest recruitment advertisement PDF from the BEL India website
    So that I can view the latest job openings

    Scenario: Navigate to BEL India website and download the latest PDF
        Given I am on the BEL India website
        When I navigate to the career section
        And I navigate to the recruitment advertisements
        And I accept the terms and conditions
        Then I should download the latest PDF


## Prerequisites
- Python 3.x installed on your system
- Chrome webdriver installed and accessible in your PATH

## Installation
1. Clone or download this repository.
2. Install the required Python packages using pip:
3. Ensure you have Chrome webdriver installed and accessible in your PATH.

## Usage
1. setup.py has the requirements for running the script, i.e selenium and requests module.
2. Run the script `bel_recruitment_pdf_downloader.py`.
3. The script will navigate to the BEL India website, go to the career section, and find the latest recruitment advertisement PDF.
4. If found, it will download the PDF as `latest_pdf.pdf` in the current directory.

## Disclaimer
This script is provided as-is without any warranty. Use it responsibly and adhere to the terms of service of the BEL India website.


