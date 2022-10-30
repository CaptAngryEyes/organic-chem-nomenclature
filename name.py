import tkinter as tk
from tkinter import ttk
import operator

class Gui():
    def __init__(self, root):
        entries = []

        def get_vallues():
            texts = []
            positions = []

            texts, positions
            for entry in entries:
                text = entry.get()
                if text != '':
                    texts.append(text)

                    pos_x = entry.grid_info()['column'] - 1
                    pos_y = entry.grid_info()['row'] - 2

                    positions.append((pos_x, pos_y))
            return texts, positions

        def name():
            texts, positions = get_vallues()
            has_characteristic_member = False
            characteristic_member_type = '[None]'
            has_multiple_bond = False
            multiple_bond_type = 'single'
            has_branch = False

            # Characteristic Member

            for value in texts:
                up = tuple(map(operator.add, positions[texts.index(value)], (0, -1)))
                down = tuple(map(operator.add, positions[texts.index(value)], (0, 1)))
                left = tuple(map(operator.add, positions[texts.index(value)], (-1, 0)))
                right = tuple(map(operator.add, positions[texts.index(value)], (1, 0)))

                try:
                    if 'OH' in value:
                        has_characteristic_member = True
                        characteristic_member_type = 'alcohol' # αλκοόλη
                    elif '═' in value and ('O' in texts[positions.index(right)] or 'O' in texts[positions.index(left)]):
                        has_characteristic_member = True
                        characteristic_member_type = 'aldehyde' # αλδεϋδη
                    elif '||' in value and ('O' in texts[positions.index(down)] or 'O' in texts[positions.index(up)]):
                        has_characteristic_member = True
                        characteristic_member_type = 'ketone' # κετόνη
                    elif 'COOH' in value:
                        has_characteristic_member = True
                        characteristic_member_type = 'carboxylic acid' # καρβοξυλικό οξύ
                    elif 'COOC' in value:
                        has_characteristic_member = True
                        characteristic_member_type = 'ester' # εστέρας
                    elif ('O' in value and ('C' in texts[positions.index(left)] and 'C' in texts[positions.index(right)])):
                        has_characteristic_member = True
                        characteristic_member_type = 'ether' # αιθέρας
                    elif ('O' in value and ('C' in texts[positions.index(up)] and 'C' in texts[positions.index(down)])):
                        has_characteristic_member = True
                        characteristic_member_type = 'ether' # αιθέρας
                except:
                    pass

            
            # Multiple Bonds
            
            for value in texts:
                up = tuple(map(operator.add, positions[texts.index(value)], (0, -1)))
                down = tuple(map(operator.add, positions[texts.index(value)], (0, 1)))
                left = tuple(map(operator.add, positions[texts.index(value)], (-1, 0)))
                right = tuple(map(operator.add, positions[texts.index(value)], (1, 0)))

                if ('≡' in value and ('C' in texts[positions.index(left)] and 'C' in texts[positions.index(right)])):
                    has_multiple_bond = True
                    multiple_bond_type = 'triple'
                    break
                elif ('═' in value and ('C' in texts[positions.index(left)] and 'C' in texts[positions.index(right)])):
                    has_multiple_bond = True
                    multiple_bond_type = 'double'
                    break
                if ('|||' in value and ('C' in texts[positions.index(up)] and 'C' in texts[positions.index(down)])):
                    has_multiple_bond = True
                    multiple_bond_type = 'triple'
                    break
                elif ('||' in value and ('C' in texts[positions.index(up)] and 'C' in texts[positions.index(down)])):
                    has_multiple_bond = True
                    multiple_bond_type = 'double'
                    break

            # Main Carbon Chain

            




        # GUI

        self.root=root
        self.root.title('Organic Chemistry Nomenclature')
        self.root.geometry('500x300')
        self.root.resizable(True, True)
        self.root.minsize(500,300)
        self.entry = tk.Entry(root)
        
        frame = tk.Frame(self.root)
        frame.grid(row=0,column=0, sticky="n")

        for j in range(1,25):
            for i in range(1,25):
                entry = ttk.Entry(frame, width=5,)
                entry.grid(row = 1+i,column = 0+j, sticky='w')
                entries.append(entry)
        
        label = ttk.Label(frame, text="Enter a compound").grid(row=0,column=0, sticky='n')
        name_button = ttk.Button(frame, text="Name", command=name).grid(row=1,column=0, sticky='w')

        empty_space = ttk.Label(frame, text=" ").grid(row=2,column=0,)
        symbol1 = tk.Text(frame, height=1, width=2)
        symbol1.insert(0.05, "─")
        symbol1.grid(row=3,column=0, sticky='n')
        symbol1.configure(state="disabled")
        symbol1.configure(inactiveselectbackground=symbol1.cget("selectbackground"))
        symbol2 = tk.Text(frame, height=1, width=2)
        symbol2.insert(0.05, "═")
        symbol2.grid(row=4,column=0, sticky='n')
        symbol2.configure(state="disabled")
        symbol2.configure(inactiveselectbackground=symbol2.cget("selectbackground"))
        symbol3 = tk.Text(frame, height=1, width=2)
        symbol3.insert(0.05, "≡")
        symbol3.grid(row=5,column=0, sticky='n')
        symbol3.configure(state="disabled")
        symbol3.configure(inactiveselectbackground=symbol3.cget("selectbackground"))

if __name__== '__main__':
    root=tk.Tk()
    gui=Gui(root)
    root.mainloop()

    