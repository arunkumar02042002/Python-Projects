import customtkinter as ctk

class TaxCalculator:
    def __init__(self) -> None:
        # Initialize the main window
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x200')
        self.window.resizable(False, False)

        # Padding for GUI elements
        self.padding: dict = {'padx': 20, 'pady': 10}

        # Income Label and Entry
        self.income_lable = ctk.CTkLabel(self.window, text='Income')
        self.income_lable.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax Label and Entry
        self.tax_lable = ctk.CTkLabel(self.window, text='Tax')
        self.tax_lable.grid(row=1, column=0, **self.padding)
        self.tax_entry = ctk.CTkEntry(self.window)
        self.tax_entry.grid(row=1, column=1, **self.padding)

        # Result Label and Entry
        self.result_lable = ctk.CTkLabel(self.window, text='Tax')
        self.result_lable.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **self.padding)

        # Calculate Button
        self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        self.calculate_button.grid(row=3, column=1, **self.padding)

    def update_result(self, text: str):
        # Update the result field with the given text
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income_str: str = self.income_entry.get()

            # Remove commas and spaces from the income value
            income_str = income_str.replace(',', '')
            income_str = income_str.replace(' ', '')

            # Check if the income field is empty
            if not income_str:
                self.update_result('Income is required')
                return

            income: float = float(income_str)

            # Get the tax_entry value
            tax_entry_value: str | None = self.tax_entry.get()
            
            # Check if the tax_entry_value is None or a string
            if tax_entry_value:
                tax_rate: float = float(tax_entry_value)
            else:
                tax_rate = 0

            if tax_rate:
                self.update_result(f'₹{income * (tax_rate / 100):,.2f}')

            # Calculate tex according to Indian tax slab
            else:
                if income > 1500000:
                    tax: float = 300000 * 0.0 + 300000 * 0.5 + 300000 * 0.1 + 300000 * 1.5 + 300000 * 2.0 + (income - 1500000) * 3.0
                elif income > 1200000:
                    tax: float = 300000 * 0.0 + 300000 * 0.5 + 300000 * 0.1 + 300000 * 1.5 + (income - 1200000) * 2.0
                elif income > 900000:
                    tax: float = 300000 * 0.0 + 300000 * 0.5 + 300000 * 0.1 + (income - 900000) * 1.5
                elif income > 600000:
                    tax: float = 300000 * 0.0 + 300000 * 0.5 + (income - 600000) * 1.5
                elif income > 300000:
                    tax: float = 300000 * 0.0 + (income - 300000) * 0.5
                else:
                    tax: float = 0

                self.update_result(f'₹{tax:,.2f}')

        # For ValueError
        except ValueError:
            self.update_result('Invalid Input')

        # For any unkown exceptions
        except Exception as e:
            print(f'Error: {e}')
            
    def run(self):
        # Start the GUI application
        self.window.mainloop()

if __name__ == '__main__':
    # Create an instance of the TaxCalculator class and run the application
    tc = TaxCalculator()
    tc.run()