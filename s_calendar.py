import requests
from bs4 import BeautifulSoup
import tkinter as tk

year = input()

url = f"https://www.timeanddate.com/calendar/?year={year}"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

calendar_table = soup.find('table', {'class': 'ca ca1'})
print(calendar_table)
if __name__ == "__main__":
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    current_row = 0
    current_column = 0

    for row in calendar_table.find_all("tr"):
        for cell in row.find_all("td"):
            label = tk.Label(frame, text=cell.text)
            label.grid(row=current_row,column=current_column)
            current_column+=1
        current_column=0
        current_row+=1

    root.mainloop()