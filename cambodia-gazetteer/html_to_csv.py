#!/usr/bin/env python3
"""
Script to extract village data from HTML file and convert to CSV format
"""

import csv
import re
from bs4 import BeautifulSoup
import os

def extract_village_data(html_file_path):
    """Extract village data from HTML file"""
    
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract commune information
    commune_info = {}
    summary_table = soup.find('div', id='summary')
    if summary_table:
        rows = summary_table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                key = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True)
                commune_info[key] = value
    
    # Extract village data
    villages = []
    village_table = soup.find('div', id='dl_list')
    
    if village_table:
        # Find all table rows with village data
        rows = village_table.find_all('tr', id=re.compile(r'row_vil_\d+'))
        
        for row in rows:
            cells = row.find_all(['th', 'td'])
            if len(cells) >= 4:
                village_data = {
                    'number': cells[0].get_text(strip=True),
                    'code': cells[1].get_text(strip=True),
                    'khmer_name': cells[2].get_text(strip=True),
                    'english_name': cells[3].get_text(strip=True),
                    'commune_code': commune_info.get('Code', ''),
                    'commune_khmer': commune_info.get('Khmer', ''),
                    'commune_latin': commune_info.get(' Latin', '')
                }
                villages.append(village_data)
    
    return villages, commune_info

def save_to_csv(villages, output_file):
    """Save village data to CSV file"""
    
    if not villages:
        print("No village data found!")
        return
    
    # Define CSV headers
    headers = [
        'Number',
        'Village_Code',
        'Village_Khmer_Name',
        'Village_English_Name',
        'Commune_Code',
        'Commune_Khmer',
        'Commune_Latin'
    ]
    
    # Write to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        
        # Write header
        writer.writeheader()
        
        # Write village data
        for village in villages:
            writer.writerow({
                'Number': village['number'],
                'Village_Code': village['code'],
                'Village_Khmer_Name': village['khmer_name'],
                'Village_English_Name': village['english_name'],
                'Commune_Code': village['commune_code'],
                'Commune_Khmer': village['commune_khmer'],
                'Commune_Latin': village['commune_latin']
            })
    
    print(f"Successfully saved {len(villages)} villages to {output_file}")

def main():
    # File paths
    html_file = 'test.html'
    csv_file = 'cambodia_villages.csv'
    
    # Check if HTML file exists
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found!")
        return
    
    try:
        # Extract data from HTML
        print("Extracting village data from HTML...")
        villages, commune_info = extract_village_data(html_file)
        
        # Display commune information
        print("\nCommune Information:")
        for key, value in commune_info.items():
            print(f"  {key}: {value}")
        
        print(f"\nFound {len(villages)} villages")
        
        # Save to CSV
        save_to_csv(villages, csv_file)
        
        # Display first few villages as preview
        if villages:
            print("\nFirst 5 villages:")
            for i, village in enumerate(villages[:5]):
                print(f"  {i+1}. {village['english_name']} ({village['khmer_name']}) - Code: {village['code']}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
