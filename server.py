# server.py
# 3 endpoints:
# new entry form
# post entry form
# get entries
import argparse
from typing import Dict
from flask import Flask, render_template, request, redirect, url_for

from dbo import HashicorpDemoDb, MariaDBHashicorpDemoDb, MemoryHashicorpDemoDb

class DBController:
    STORE = None
    @staticmethod
    def get_store():
        return DBController.STORE

    @staticmethod
    def set_store(store: HashicorpDemoDb):
        DBController.STORE = store

app = Flask(__name__)

# @app.before_request
# def before_request():
#     # Set up the entry_controller instance before each request
#     request.entry_controller = entry_controller

@app.route('/get-entries')
def get_entries():
    return render_template('get_entires.html', entries=DBController.STORE.get_entries())

@app.route('/new-entry', methods=['GET', 'POST'])
def new_entry():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        # Save the entry (you can store it in a database)
        DBController.STORE.add_entry({'name': name, 'price': price, 'quantity': quantity})

        # Redirect to a success page or do further processing
        return redirect(url_for('get_entries'))
    else:
        # Render the form for GET requests
        return render_template('new_entry.html')

def main():
    parser = argparse.ArgumentParser(description="Command-line and Web Mode Selector")
    
    parser.add_argument('--mode', choices=['CLI', 'Web'], default='CLI', help='Select mode: CLI or Web')
    parser.add_argument('--method', type=int, choices=[0, 1, 2, 3], default=0, help='Select method: 0, 1, 2, 3 (default is 0)')

    # Parse the arguments
    args = parser.parse_args()

    # Display the selected options
    print(f"Selected Mode: {args.mode}")
    print(f"Selected Method: {args.method}")

    if args.mode == "Web":
        if args.method == 0:
            DBController.set_store(MemoryHashicorpDemoDb())
        elif args.method == 1:
            DBController.set_store(MariaDBHashicorpDemoDb())
        else:
            raise RuntimeError(f"Invalid method {args.method}")
            
        # Start the server
        app.run()
    else:
        raise NotImplementedError()


if __name__ == "__main__":
    main()
    