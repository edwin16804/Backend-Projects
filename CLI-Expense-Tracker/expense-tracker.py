#!/usr/bin/env python3
import argparse
import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(description, amount):
    data = load_data()
    if amount <= 0:
        print("Amount must be positive.")
        return
    expense_id = data[-1]["id"] + 1 if data else 1
    today = datetime.now().strftime("%Y-%m-%d")
    data.append({"id": expense_id, "date": today, "description": description, "amount": amount})
    save_data(data)
    print(f"Expense added successfully (ID: {expense_id})")

def list_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return
    print(f"{'ID':<4}{'Date':<12}{'Description':<15}{'Amount'}")
    for exp in data:
        print(f"{exp['id']:<4}{exp['date']:<12}{exp['description']:<15}${exp['amount']}")

def delete_expense(expense_id):
    data = load_data()
    new_data = [e for e in data if e["id"] != expense_id]
    if len(new_data) == len(data):
        print("Expense ID not found.")
        return
    save_data(new_data)
    print("Expense deleted successfully.")

def update_expense(expense_id, description=None, amount=None):
    data = load_data()
    for exp in data:
        if exp["id"] == expense_id:
            if description:
                exp["description"] = description
            if amount is not None:
                if amount <= 0:
                    print("Amount must be positive.")
                    return
                exp["amount"] = amount
            save_data(data)
            print("Expense updated successfully.")
            return
    print("Expense ID not found.")

def summary(month=None):
    data = load_data()
    if month:
        total = sum(e["amount"] for e in data if datetime.strptime(e["date"], "%Y-%m-%d").month == month)
        print(f"Total expenses for {datetime(1900, month, 1).strftime('%B')}: ${total}")
    else:
        total = sum(e["amount"] for e in data)
        print(f"Total expenses: ${total}")

def main():
    parser = argparse.ArgumentParser(description="Simple Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True, help="Expense description")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")

    # List
    subparsers.add_parser("list")

    # Delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True, help="Expense ID")

    # Update
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--description", help="New description")
    update_parser.add_argument("--amount", type=float, help="New amount")

    # Summary
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int, help="Month number (1-12)")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "summary":
        summary(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
