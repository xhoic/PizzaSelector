import tkinter as tk
from src.AllPizzas import allPizza
from PIL import ImageTk, Image
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.pizzaList = allPizza()

        self.__totalPrice = 0

        self.mainWindow = tk.Tk()
        self.mainWindow.title('Order Pizza')
        self.mainWindow.geometry('700x700+200+20')
        self.pizzaFrame = tk.Frame(self.mainWindow)
        self.pizzaFrame.grid(row=0, column=0, rowspan=20, columnspan=20)
        self.pizzaFrame.place(relx=.5, rely=.42, anchor='center')

        # pizza images
        self.margheritaImg = ImageTk.PhotoImage(Image.open("Images/margheritaPizza.jpg"))
        self.margheritaLabel = tk.Label(self.pizzaFrame, image=self.margheritaImg)
        self.margheritaLabel.grid(row=0, column=0, padx=50, pady=10)

        self.fourCheeseImg = ImageTk.PhotoImage(Image.open("Images/fourCheesePizza.jpg"))
        self.fourCheeseLabel = tk.Label(self.pizzaFrame, image=self.fourCheeseImg)
        self.fourCheeseLabel.grid(row=0, column=1, padx=50, pady=10)

        self.pepperoniImg = ImageTk.PhotoImage(Image.open("Images/pepperoniPizza.jpg"))
        self.pepperoniLabel = tk.Label(self.pizzaFrame, image=self.pepperoniImg)
        self.pepperoniLabel.grid(row=0, column=2, padx=50, pady=10)

        self.pineappleImg = ImageTk.PhotoImage(Image.open("Images/pineapplePizza.jpg"))
        self.pineappleLabel = tk.Label(self.pizzaFrame, image=self.pineappleImg)
        self.pineappleLabel.grid(row=8, column=0, padx=50, pady=10)

        self.seafoodImg = ImageTk.PhotoImage(Image.open("Images/seafoodPizza.jpg"))
        self.seafoodLabel = tk.Label(self.pizzaFrame, image=self.seafoodImg)
        self.seafoodLabel.grid(row=8, column=1, padx=50, pady=10)

        self.sausageImg = ImageTk.PhotoImage(Image.open("Images/sausagePizza.jpg"))
        self.sausageLabel = tk.Label(self.pizzaFrame, image=self.sausageImg)
        self.sausageLabel.grid(row=8, column=2, padx=50, pady=10)

        # pizza names display
        self.margheritaNameLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[1].name)
        self.margheritaNameLabel.grid(row=1, column=0, padx=50, pady=0)

        self.fourCheeseNameLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[2].name)
        self.fourCheeseNameLabel.grid(row=1, column=1, padx=50, pady=0)

        self.pepperoniNameLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[3].name)
        self.pepperoniNameLabel.grid(row=1, column=2, padx=50, pady=0)

        self.pineappleNameLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[4].name)
        self.pineappleNameLabel.grid(row=9, column=0, padx=50, pady=0)

        self.seafoodNameLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[5].name)
        self.seafoodNameLabel.grid(row=9, column=1, padx=50, pady=0)

        self.sausageNameLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[6].name)
        self.sausageNameLabel.grid(row=9, column=2, padx=50, pady=0)

        # pizza toppings display
        self.margheritaToppingsLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[1].toppings)
        self.margheritaToppingsLabel.grid(row=2, column=0, padx=50, pady=0)

        self.fourCheeseToppingsLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[2].toppings)
        self.fourCheeseToppingsLabel.grid(row=2, column=1, padx=50, pady=0)

        self.pepperoniToppingsLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[3].toppings)
        self.pepperoniToppingsLabel.grid(row=2, column=2, padx=50, pady=0)

        self.pineappleToppingsLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[4].toppings)
        self.pineappleToppingsLabel.grid(row=10, column=0, padx=50, pady=0)

        self.seafoodToppingsLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[5].toppings)
        self.seafoodToppingsLabel.grid(row=10, column=1, padx=50, pady=0)

        self.sausageToppingsLabel = tk.Label(self.pizzaFrame, text=self.pizzaList[6].toppings)
        self.sausageToppingsLabel.grid(row=10, column=2, padx=50, pady=0)

        # display quantity and size
        self.margheritaSizeListbox = tk.Listbox(self.pizzaFrame, selectmode='single', height=3, width=3)
        for i in self.pizzaList[1].size:
            self.margheritaSizeListbox.insert(tk.END, i)
        self.margheritaSizeListbox.grid(row=3, column=0)
        self.margheritaQtyLabel = tk.Label(self.pizzaFrame, text='Qty:')
        self.margheritaQtyLabel.grid(row=4, column=0)
        self.margheritaQtyEntry = tk.Entry(self.pizzaFrame, width=5)
        self.margheritaQtyEntry.grid(row=5, column=0)

        self.fourCheeseSizeListbox = tk.Listbox(self.pizzaFrame, selectmode='single', height=3, width=3)
        for i in self.pizzaList[2].size:
            self.fourCheeseSizeListbox.insert(tk.END, i)
        self.fourCheeseSizeListbox.grid(row=3, column=1)
        self.fourCheeseQtyLabel = tk.Label(self.pizzaFrame, text='Qty:')
        self.fourCheeseQtyLabel.grid(row=4, column=1)
        self.fourCheeseQtyEntry = tk.Entry(self.pizzaFrame, width=5)
        self.fourCheeseQtyEntry.grid(row=5, column=1)

        self.pepperoniSizeListbox = tk.Listbox(self.pizzaFrame, selectmode='single', height=3, width=3)
        for i in self.pizzaList[3].size:
            self.pepperoniSizeListbox.insert(tk.END, i)
        self.pepperoniSizeListbox.grid(row=3, column=2)
        self.pepperoniQtyLabel = tk.Label(self.pizzaFrame, text='Qty:')
        self.pepperoniQtyLabel.grid(row=4, column=2)
        self.pepperoniQtyEntry = tk.Entry(self.pizzaFrame, width=5)
        self.pepperoniQtyEntry.grid(row=5, column=2)

        self.pineappleSizeListbox = tk.Listbox(self.pizzaFrame, selectmode='single', height=3, width=3)
        for i in self.pizzaList[4].size:
            self.pineappleSizeListbox.insert(tk.END, i)
        self.pineappleSizeListbox.grid(row=11, column=0)
        self.pineappleQtyLabel = tk.Label(self.pizzaFrame, text='Qty:')
        self.pineappleQtyLabel.grid(row=12, column=0)
        self.pineappleQtyEntry = tk.Entry(self.pizzaFrame, width=5)
        self.pineappleQtyEntry.grid(row=13, column=0)

        self.seafoodSizeListbox = tk.Listbox(self.pizzaFrame, selectmode='single', height=3, width=3)
        for i in self.pizzaList[5].size:
            self.seafoodSizeListbox.insert(tk.END, i)
        self.seafoodSizeListbox.grid(row=11, column=1)
        self.seafoodQtyLabel = tk.Label(self.pizzaFrame, text='Qty:')
        self.seafoodQtyLabel.grid(row=12, column=1)
        self.seafoodQtyEntry = tk.Entry(self.pizzaFrame, width=5)
        self.seafoodQtyEntry.grid(row=13, column=1)

        self.sausageSizeListbox = tk.Listbox(self.pizzaFrame, selectmode='single', height=3, width=3)
        for i in self.pizzaList[6].size:
            self.sausageSizeListbox.insert(tk.END, i)
        self.sausageSizeListbox.grid(row=11, column=2)
        self.sausageQtyLabel = tk.Label(self.pizzaFrame, text='Qty:')
        self.sausageQtyLabel.grid(row=12, column=2)
        self.sausageQtyEntry = tk.Entry(self.pizzaFrame, width=5)
        self.sausageQtyEntry.grid(row=13, column=2)

        # create buttons to add pizza
        self.addMargheritaButton = tk.Button(self.pizzaFrame, text='Add', command=self.addMargherita)
        self.addMargheritaButton.grid(row=6, column=0, pady=5)
        self.addFourCheeseButton = tk.Button(self.pizzaFrame, text='Add', command=self.addFourCheese)
        self.addFourCheeseButton.grid(row=6, column=1, pady=5)
        self.addPepperoniButton = tk.Button(self.pizzaFrame, text='Add', command=self.addPepperoni)
        self.addPepperoniButton.grid(row=6, column=2, pady=5)
        self.addPineappleButton = tk.Button(self.pizzaFrame, text='Add', command=self.addPineapple)
        self.addPineappleButton.grid(row=14, column=0, pady=5)
        self.addSeafoodButton = tk.Button(self.pizzaFrame, text='Add', command=self.addSeafood)
        self.addSeafoodButton.grid(row=14, column=1, pady=5)
        self.addSausageButton = tk.Button(self.pizzaFrame, text='Add', command=self.addSausage)
        self.addSausageButton.grid(row=14, column=2, pady=5)

        # create exit and clear button
        self.exitButton = tk.Button(self.mainWindow, text='Exit', command=self.exit)
        self.exitButton.place(relx=.9, rely=.95, anchor='s')
        self.clearButton = tk.Button(self.mainWindow, text='Clear', command=self.clear)
        self.clearButton.place(relx=.1, rely=.95, anchor='s')

        # create check out frame
        self.checkOutFrame = tk.Frame(self.mainWindow)
        self.checkOutFrame.grid(row=0, column=0, rowspan=3, columnspan=3)
        self.checkOutFrame.place(relx=.3, rely=.9, anchor='s')
        self.totalLabel = tk.Label(self.checkOutFrame, text='Total:')
        self.totalLabel.grid(row=0, column=0)
        self.totalPriceLabel = tk.Label(self.checkOutFrame, text=('${:<10,.2f}'.format(self.__totalPrice)))
        self.totalPriceLabel.grid(row=0, column=1)

        self.mainWindow.mainloop()

    # buttons usage
    def addMargherita(self):
        addMargheritaQty = self.margheritaQtyEntry.get()
        addMargheritaSize = str(self.margheritaSizeListbox.curselection())
        try:
            if addMargheritaSize == '()':
                raise RuntimeError('Please select a size.')
        except RuntimeError as err:
            messagebox.showerror(err)
            self.margheritaSizeListbox.focus()
        else:
            try:
                addMargheritaQty = int(addMargheritaQty)
                addMargheritaQty = abs(addMargheritaQty)
            except ValueError:
                messagebox.showerror('ERROR! Pizza qty should be a positive integer!')
                self.margheritaQtyEntry.focus()
            else:
                self.pizzaList[1].qty = addMargheritaQty
                if addMargheritaSize == '(0,)':
                    self.__totalPrice += self.pizzaList[1].total(0)
                elif addMargheritaSize == '(1,)':
                    self.__totalPrice += self.pizzaList[1].total(1)
                else:
                    self.__totalPrice += self.pizzaList[1].total(2)
                self.totalPriceLabel = tk.Label(self.checkOutFrame, text=('${:<10,.2f}'.format(self.__totalPrice)))
                self.totalPriceLabel.grid(row=0, column=1)

    def addFourCheese(self):
        addFourCheeseQty = self.fourCheeseQtyEntry.get()
        addFourCheeseSize = str(self.fourCheeseSizeListbox.curselection())
        try:
            if addFourCheeseSize == '()':
                raise RuntimeError('Please select a size.')
        except RuntimeError as err:
            messagebox.showerror(err)
            self.fourCheeseSizeListbox.focus()
        else:
            try:
                addFourCheeseQty = int(addFourCheeseQty)
                addFourCheeseQty = abs(addFourCheeseQty)
            except ValueError:
                messagebox.showerror('ERROR! Pizza qty should be a positive integer!')
                self.fourCheeseQtyEntry.focus()
            else:
                self.pizzaList[2].qty = addFourCheeseQty
                if addFourCheeseSize == '(0,)':
                    self.__totalPrice += self.pizzaList[2].total(0)
                elif addFourCheeseSize == '(1,)':
                    self.__totalPrice += self.pizzaList[2].total(1)
                else:
                    self.__totalPrice += self.pizzaList[2].total(2)
                self.totalPriceLabel = tk.Label(self.checkOutFrame, text=('${:<10,.2f}'.format(self.__totalPrice)))
                self.totalPriceLabel.grid(row=0, column=1)

    def addPepperoni(self):
        addPepperoniQty = self.pepperoniQtyEntry.get()
        addPepperoniSize = str(self.pepperoniSizeListbox.curselection())
        try:
            if addPepperoniSize == '()':
                raise RuntimeError('Please select a size.')
        except RuntimeError as err:
            messagebox.showerror(err)
            self.pepperoniSizeListbox.focus()
        else:
            try:
                addPepperoniQty = int(addPepperoniQty)
                addPepperoniQty = abs(addPepperoniQty)
            except ValueError:
                messagebox.showerror('ERROR! Pizza qty should be a positive integer!')
                self.pepperoniQtyEntry.focus()
            else:
                self.pizzaList[3].qty = addPepperoniQty
                if addPepperoniSize == '(0,)':
                    self.__totalPrice += self.pizzaList[3].total(0)
                elif addPepperoniSize == '(1,)':
                    self.__totalPrice += self.pizzaList[3].total(1)
                else:
                    self.__totalPrice += self.pizzaList[3].total(2)
                self.totalPriceLabel = tk.Label(self.checkOutFrame, text=('${:<10,.2f}'.format(self.__totalPrice)))
                self.totalPriceLabel.grid(row=0, column=1)

    def addPineapple(self):
        addPineappleQty = self.pineappleQtyEntry.get()
        addPineappleSize = str(self.pineappleSizeListbox.curselection())
        try:
            if addPineappleSize == '()':
                raise RuntimeError('Please select a size.')
        except RuntimeError as err:
            messagebox.showerror(err)
            self.pineappleSizeListbox.focus()
        else:
            try:
                addPineappleQty = int(addPineappleQty)
                addPineappleQty = abs(addPineappleQty)
            except ValueError:
                messagebox.showerror('ERROR! Pizza qty should be a positive integer!')
                self.pineappleQtyEntry.focus()
            else:
                self.pizzaList[4].qty = addPineappleQty
                if addPineappleSize == '(0,)':
                    self.__totalPrice += self.pizzaList[4].total(0)
                elif addPineappleSize == '(1,)':
                    self.__totalPrice += self.pizzaList[4].total(1)
                else:
                    self.__totalPrice += self.pizzaList[4].total(2)
                self.totalPriceLabel = tk.Label(self.checkOutFrame, text=('${:<10,.2f}'.format(self.__totalPrice)))
                self.totalPriceLabel.grid(row=0, column=1)

    def addSeafood(self):
        addSeafoodQty = self.seafoodQtyEntry.get()
        addSeafoodSize = str(self.seafoodSizeListbox.curselection())
        try:
            if addSeafoodSize == '()':
                raise RuntimeError('Please select a size.')
        except RuntimeError as err:
            messagebox.showerror(err)
            self.seafoodSizeListbox.focus()
        else:
            try:
                addSeafoodQty = int(addSeafoodQty)
                addSeafoodQty = abs(addSeafoodQty)
            except ValueError:
                messagebox.showerror('ERROR! Pizza qty should be a positive integer!')
                self.seafoodQtyEntry.focus()
            else:
                self.pizzaList[5].qty = addSeafoodQty
                if addSeafoodSize == '(0,)':
                    self.__totalPrice += self.pizzaList[5].total(0)
                elif addSeafoodSize == '(1,)':
                    self.__totalPrice += self.pizzaList[5].total(1)
                else:
                    self.__totalPrice += self.pizzaList[5].total(2)
                self.totalPriceLabel = tk.Label(self.checkOutFrame, text=('${:<10,.2f}'.format(self.__totalPrice)))
                self.totalPriceLabel.grid(row=0, column=1)

    def addSausage(self):
        addSausageQty = self.sausageQtyEntry.get()
        addSausageSize = str(self.sausageSizeListbox.curselection())
        try:
            if addSausageSize == '()':
                raise RuntimeError('Please select a size.')
        except RuntimeError as err:
            messagebox.showerror(err)
            self.sausageSizeListbox.focus()
        else:
            try:
                addSausageQty = int(addSausageQty)
                addSausageQty = abs(addSausageQty)
            except ValueError:
                messagebox.showerror('ERROR! Pizza qty should be a positive integer!')
                self.sausageQtyEntry.focus()
            else:
                self.pizzaList[6].qty = addSausageQty
                if addSausageSize == '(0,)':
                    self.__totalPrice += self.pizzaList[6].total(0)
                elif addSausageSize == '(1,)':
                    self.__totalPrice += self.pizzaList[6].total(1)
                else:
                    self.__totalPrice += self.pizzaList[6].total(2)
                self.totalPriceLabel = tk.Label(self.checkOutFrame, text=('${:<10,.2f}'.format(self.__totalPrice)))
                self.totalPriceLabel.grid(row=0, column=1)

    def exit(self):
        answ = messagebox.askyesno('Are you sure you want to exit?')
        if answ:
            self.mainWindow.destroy()

    def clear(self):
        self.margheritaQtyEntry.delete(0, tk.END)
        self.fourCheeseQtyEntry.delete(0, tk.END)
        self.pepperoniQtyEntry.delete(0, tk.END)
        self.pineappleQtyEntry.delete(0, tk.END)
        self.seafoodQtyEntry.delete(0, tk.END)
        self.sausageQtyEntry.delete(0, tk.END)
        self.__totalPrice = 0.0
        self.totalPriceLabel = tk.Label(self.checkOutFrame, text=('${:<10,.2f}'.format(self.__totalPrice)))
        self.totalPriceLabel.grid(row=0, column=1)


if __name__ == '__main__':
    myGUI = MyGUI()
