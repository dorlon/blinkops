# The main entry point of the program
from form_loader import load_form
from form_filler import fill_form
from form_saver import save_results

def main():
    form = None  # Initialize the form variable to hold imported form data
    while True:
        # Display menu options for user actions
        print("Welcome, choose an action:")
        print("1. Import a form")
        print("2. Fill in a form")
        print("3. Quit")
        choice = input()  # Get user choice

        if choice == '1':
            try:
                file_path = input("Enter the YAML path to the form:")  # Ask for the file path
                form = load_form(file_path)  # Load the form data from the specified file
                print("Form imported successfully!")
            except Exception as e:
                print(f"Error: {e}")  # Print any errors encountered during import

        elif choice == '2':
            if not form:  # Check if a form has been imported
                print("Please import a form first.")
                continue
            try:
                filled_form = fill_form(form)  # Fill in the form interactively
                save_choice = input("Would you like to save the results to a file? (yes/no): ").lower()
                if save_choice == 'yes':
                    save_path = input("Enter the file path to save (JSON or YAML): ")  # Ask for save path
                    save_results(filled_form, save_path)  # Save the filled form results
                else:
                    save_results(filled_form)  # Just print the results if not saving
            except Exception as e:
                print(f"Error: {e}")  # Print any errors encountered during form filling

        elif choice == '3':
            print("Exiting. Goodbye!")  # Exit the program
            break

        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == '__main__':
    main()  # Start the program
