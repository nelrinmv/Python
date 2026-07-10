import json
import os
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, date, time
from typing import Dict, List, Optional

DEFAULT_CATEGORIES = [
    "Grocery", "Vegetables", "Fruits", "Milk", "Medicines", "Fuel",
    "Electricity", "Water Bill", "Gas", "Internet", "Mobile Recharge",
    "Rent", "Shopping", "Clothes", "Electronics", "Home Appliances",
    "Furniture", "School", "College", "Fees", "Books", "Entertainment",
    "Travel", "Eating Out", "Gifts", "Healthcare", "Repairs",
    "Investments", "Pets", "Charity", "Miscellaneous",
]

PAYMENT_METHODS = [
    "Cash", "UPI", "Credit Card", "Debit Card", "Net Banking", "Wallet",
    "Cheque", "Other",
]

DATA_FILENAME = "family_expense_data.json"


def now_iso() -> str:
    return datetime.now().isoformat()


def parse_iso(value: str):
    try:
        return datetime.fromisoformat(value)
    except Exception:
        return value


@dataclass
class WalletTransaction:
    id: str
    type: str
    amount: float
    date: str
    reason: Optional[str] = None
    balance_after: float = 0.0
    related_member_id: Optional[str] = None
    category: Optional[str] = None

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict):
        return WalletTransaction(**data)


@dataclass
class ExpenseItem:
    name: str
    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    total: Optional[float] = None

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict):
        return ExpenseItem(**data)


@dataclass
class Expense:
    id: str
    member_id: str
    amount: float
    date: str
    time: str
    category: str
    wallet_used: str
    payment_method: str
    item_name: Optional[str] = None
    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    vendor: Optional[str] = None
    notes: Optional[str] = None
    location: Optional[str] = None
    receipt: Optional[str] = None
    items: List[Dict] = field(default_factory=list)

    def to_dict(self) -> Dict:
        data = asdict(self)
        data["items"] = [item if isinstance(item, dict) else item.to_dict() for item in self.items]
        return data

    @staticmethod
    def from_dict(data: Dict):
        items = [ExpenseItem.from_dict(item) if isinstance(item, dict) and "name" in item else item for item in data.get("items", [])]
        data["items"] = items
        return Expense(**data)


@dataclass
class WalletSummary:
    current_balance: float = 0.0
    total_added: float = 0.0
    total_spent: float = 0.0
    history: List[WalletTransaction] = field(default_factory=list)

    def to_dict(self) -> Dict:
        result = asdict(self)
        result["history"] = [entry.to_dict() for entry in self.history]
        return result

    @staticmethod
    def from_dict(data: Dict):
        history = [WalletTransaction.from_dict(entry) for entry in data.get("history", [])]
        return WalletSummary(
            current_balance=data.get("current_balance", 0.0),
            total_added=data.get("total_added", 0.0),
            total_spent=data.get("total_spent", 0.0),
            history=history,
        )


@dataclass
class Member:
    id: str
    name: str
    profile_photo: Optional[str] = None
    wallet: WalletSummary = field(default_factory=WalletSummary)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "profile_photo": self.profile_photo,
            "wallet": self.wallet.to_dict(),
        }

    @staticmethod
    def from_dict(data: Dict):
        wallet = WalletSummary.from_dict(data.get("wallet", {}))
        return Member(
            id=data["id"],
            name=data["name"],
            profile_photo=data.get("profile_photo"),
            wallet=wallet,
        )


@dataclass
class FamilyAccount:
    name: str
    members: List[Member] = field(default_factory=list)
    expenses: List[Expense] = field(default_factory=list)
    categories: List[str] = field(default_factory=lambda: DEFAULT_CATEGORIES.copy())
    payment_methods: List[str] = field(default_factory=lambda: PAYMENT_METHODS.copy())

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "members": [member.to_dict() for member in self.members],
            "expenses": [expense.to_dict() for expense in self.expenses],
            "categories": self.categories,
            "payment_methods": self.payment_methods,
        }

    @staticmethod
    def from_dict(data: Dict):
        members = [Member.from_dict(member) for member in data.get("members", [])]
        expenses = [Expense.from_dict(expense) for expense in data.get("expenses", [])]
        return FamilyAccount(
            name=data.get("name", "Family Account"),
            members=members,
            expenses=expenses,
            categories=data.get("categories", DEFAULT_CATEGORIES.copy()),
            payment_methods=data.get("payment_methods", PAYMENT_METHODS.copy()),
        )


class FamilyExpenseManager:
    def __init__(self, storage_path: Optional[str] = None):
        base_dir = storage_path or os.path.dirname(os.path.abspath(__file__))
        self.storage_path = os.path.join(base_dir, DATA_FILENAME)
        self.account = self.load_account()

    def load_account(self) -> FamilyAccount:
        if os.path.isfile(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return FamilyAccount.from_dict(data)
        return FamilyAccount(name="Family Expense Tracker")

    def save_account(self):
        data = self.account.to_dict()
        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def generate_id(self) -> str:
        return str(uuid.uuid4())

    def add_member(self, name: str, profile_photo: Optional[str] = None) -> Member:
        member = Member(id=self.generate_id(), name=name.strip(), profile_photo=profile_photo)
        self.account.members.append(member)
        self.save_account()
        return member

    def remove_member(self, member_id: str) -> bool:
        original_count = len(self.account.members)
        self.account.members = [member for member in self.account.members if member.id != member_id]
        updated = len(self.account.members) != original_count
        if updated:
            self.save_account()
        return updated

    def find_member(self, member_id: str) -> Optional[Member]:
        return next((member for member in self.account.members if member.id == member_id), None)

    def add_cash(self, member_id: str, amount: float, reason: Optional[str] = None, date_value: Optional[str] = None) -> bool:
        member = self.find_member(member_id)
        if not member or amount <= 0:
            return False
        date_value = date_value or now_iso()
        member.wallet.current_balance += amount
        member.wallet.total_added += amount
        transaction = WalletTransaction(
            id=self.generate_id(),
            type="Add",
            amount=amount,
            date=date_value,
            reason=reason,
            balance_after=member.wallet.current_balance,
        )
        member.wallet.history.append(transaction)
        self.save_account()
        return True

    def remove_cash(self, member_id: str, amount: float, reason: Optional[str] = None, date_value: Optional[str] = None) -> bool:
        member = self.find_member(member_id)
        if not member or amount <= 0 or member.wallet.current_balance < amount:
            return False
        date_value = date_value or now_iso()
        member.wallet.current_balance -= amount
        member.wallet.total_spent += amount
        transaction = WalletTransaction(
            id=self.generate_id(),
            type="Remove",
            amount=-amount,
            date=date_value,
            reason=reason,
            balance_after=member.wallet.current_balance,
        )
        member.wallet.history.append(transaction)
        self.save_account()
        return True

    def transfer_cash(self, sender_id: str, receiver_id: str, amount: float, reason: Optional[str] = None, date_value: Optional[str] = None) -> bool:
        sender = self.find_member(sender_id)
        receiver = self.find_member(receiver_id)
        if not sender or not receiver or amount <= 0 or sender.wallet.current_balance < amount:
            return False
        date_value = date_value or now_iso()
        sender.wallet.current_balance -= amount
        sender.wallet.total_spent += amount
        receiver.wallet.current_balance += amount
        receiver.wallet.total_added += amount
        sender.wallet.history.append(WalletTransaction(
            id=self.generate_id(),
            type="Transfer Sent",
            amount=-amount,
            date=date_value,
            reason=reason,
            balance_after=sender.wallet.current_balance,
            related_member_id=receiver.id,
        ))
        receiver.wallet.history.append(WalletTransaction(
            id=self.generate_id(),
            type="Transfer Received",
            amount=amount,
            date=date_value,
            reason=reason,
            balance_after=receiver.wallet.current_balance,
            related_member_id=sender.id,
        ))
        self.save_account()
        return True

    def record_expense(
        self,
        member_id: str,
        amount: float,
        category: str,
        wallet_used: str,
        payment_method: str,
        date_value: Optional[str] = None,
        time_value: Optional[str] = None,
        item_name: Optional[str] = None,
        quantity: Optional[float] = None,
        unit_price: Optional[float] = None,
        vendor: Optional[str] = None,
        notes: Optional[str] = None,
        location: Optional[str] = None,
        receipt: Optional[str] = None,
        items: Optional[List[Dict]] = None,
    ) -> bool:
        member = self.find_member(member_id)
        if not member or amount <= 0 or member.wallet.current_balance < amount:
            return False
        date_value = date_value or date.today().isoformat()
        time_value = time_value or datetime.now().time().strftime("%H:%M:%S")
        expense_items = []
        if items:
            for item in items:
                item_obj = ExpenseItem(
                    name=item.get("name", ""),
                    quantity=item.get("quantity"),
                    unit_price=item.get("unit_price"),
                    total=item.get("total"),
                )
                expense_items.append(item_obj)
        expense = Expense(
            id=self.generate_id(),
            member_id=member.id,
            amount=amount,
            date=date_value,
            time=time_value,
            category=category,
            wallet_used=wallet_used,
            payment_method=payment_method,
            item_name=item_name,
            quantity=quantity,
            unit_price=unit_price,
            vendor=vendor,
            notes=notes,
            location=location,
            receipt=receipt,
            items=[item.to_dict() for item in expense_items],
        )
        member.wallet.current_balance -= amount
        member.wallet.total_spent += amount
        member.wallet.history.append(WalletTransaction(
            id=self.generate_id(),
            type="Expense",
            amount=-amount,
            date=date_value,
            reason=notes or category,
            balance_after=member.wallet.current_balance,
            category=category,
        ))
        self.account.expenses.append(expense)
        self.save_account()
        return True

    def get_member_summary(self, member_id: str) -> Optional[Dict]:
        member = self.find_member(member_id)
        if not member:
            return None
        expenses = [expense for expense in self.account.expenses if expense.member_id == member_id]
        total_expenses = sum(expense.amount for expense in expenses)
        most_used_category = None
        if expenses:
            categories = {}
            for expense in expenses:
                categories[expense.category] = categories.get(expense.category, 0) + expense.amount
            most_used_category = max(categories, key=categories.get)
        return {
            "member_name": member.name,
            "current_balance": member.wallet.current_balance,
            "total_added": member.wallet.total_added,
            "total_spent": member.wallet.total_spent,
            "total_expenses": total_expenses,
            "expense_count": len(expenses),
            "most_used_category": most_used_category,
            "recent_transactions": [txn.to_dict() for txn in member.wallet.history[-5:]],
        }

    def get_family_dashboard(self) -> Dict:
        total_family_wallet = sum(member.wallet.current_balance for member in self.account.members)
        total_family_spent = sum(member.wallet.total_spent for member in self.account.members)
        total_family_added = sum(member.wallet.total_added for member in self.account.members)
        recent_expenses = sorted(self.account.expenses, key=lambda x: x.date, reverse=True)[:5]
        category_sums: Dict[str, float] = {}
        member_sums: Dict[str, float] = {}
        for expense in self.account.expenses:
            category_sums[expense.category] = category_sums.get(expense.category, 0.0) + expense.amount
            member_sums[expense.member_id] = member_sums.get(expense.member_id, 0.0) + expense.amount
        most_used_category = max(category_sums, key=category_sums.get) if category_sums else None
        highest_spending_member = None
        if member_sums:
            highest_spending_id = max(member_sums, key=member_sums.get)
            highest_spending_member = self.find_member(highest_spending_id).name if self.find_member(highest_spending_id) else None
        return {
            "total_family_wallet": total_family_wallet,
            "total_family_spent": total_family_spent,
            "total_family_added": total_family_added,
            "most_used_category": most_used_category,
            "highest_spending_member": highest_spending_member,
            "recent_expenses": [expense.to_dict() for expense in recent_expenses],
            "member_wallets": [{"name": member.name, "balance": member.wallet.current_balance} for member in self.account.members],
        }

    def search_expenses(self, query: str) -> List[Dict]:
        query_lower = query.strip().lower()
        results = []
        for expense in self.account.expenses:
            if (
                query_lower in str(expense.amount).lower()
                or query_lower in (expense.item_name or "").lower()
                or query_lower in expense.category.lower()
                or query_lower in (expense.vendor or "").lower()
                or query_lower in expense.payment_method.lower()
                or query_lower in (expense.notes or "").lower()
                or query_lower in expense.date.lower()
            ):
                results.append(expense.to_dict())
        return results

    def filter_expenses(
        self,
        member_id: Optional[str] = None,
        category: Optional[str] = None,
        wallet_used: Optional[str] = None,
        payment_method: Optional[str] = None,
        min_amount: Optional[float] = None,
        max_amount: Optional[float] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> List[Dict]:
        results = self.account.expenses
        if member_id:
            results = [expense for expense in results if expense.member_id == member_id]
        if category:
            results = [expense for expense in results if expense.category.lower() == category.lower()]
        if wallet_used:
            results = [expense for expense in results if expense.wallet_used.lower() == wallet_used.lower()]
        if payment_method:
            results = [expense for expense in results if expense.payment_method.lower() == payment_method.lower()]
        if min_amount is not None:
            results = [expense for expense in results if expense.amount >= min_amount]
        if max_amount is not None:
            results = [expense for expense in results if expense.amount <= max_amount]
        if start_date:
            results = [expense for expense in results if expense.date >= start_date]
        if end_date:
            results = [expense for expense in results if expense.date <= end_date]
        return [expense.to_dict() for expense in results]

    def add_custom_category(self, category: str) -> bool:
        category = category.strip()
        if category and category not in self.account.categories:
            self.account.categories.append(category)
            self.save_account()
            return True
        return False

    def add_payment_method(self, payment_method: str) -> bool:
        payment_method = payment_method.strip()
        if payment_method and payment_method not in self.account.payment_methods:
            self.account.payment_methods.append(payment_method)
            self.save_account()
            return True
        return False


def main():
    manager = FamilyExpenseManager()
    print("Family Expense Tracker")

    while True:
        print("\nChoose an option:")
        print("1. Add family member")
        print("2. Add cash to wallet")
        print("3. Remove cash from wallet")
        print("4. Transfer cash")
        print("5. Record expense")
        print("6. Show family dashboard")
        print("7. Search expenses")
        print("8. Filter expenses")
        print("9. Add custom category")
        print("0. Exit")

        choice = input("Option: ").strip()
        if choice == "1":
            name = input("Member name: ").strip()
            if name:
                member = manager.add_member(name)
                print(f"Added member: {member.name} (ID: {member.id})")
            else:
                print("Name cannot be empty.")
        elif choice == "2":
            member_id = input("Member ID: ").strip()
            amount = float(input("Amount to add: ").strip() or 0)
            reason = input("Reason: ").strip() or None
            if manager.add_cash(member_id, amount, reason):
                print("Cash added successfully.")
            else:
                print("Failed to add cash. Check member or amount.")
        elif choice == "3":
            member_id = input("Member ID: ").strip()
            amount = float(input("Amount to remove: ").strip() or 0)
            reason = input("Reason: ").strip() or None
            if manager.remove_cash(member_id, amount, reason):
                print("Cash removed successfully.")
            else:
                print("Failed to remove cash. Check balance and member.")
        elif choice == "4":
            sender_id = input("Sender member ID: ").strip()
            receiver_id = input("Receiver member ID: ").strip()
            amount = float(input("Amount to transfer: ").strip() or 0)
            reason = input("Reason: ").strip() or None
            if manager.transfer_cash(sender_id, receiver_id, amount, reason):
                print("Transfer completed.")
            else:
                print("Transfer failed. Check IDs, balance and amount.")
        elif choice == "5":
            member_id = input("Member ID: ").strip()
            amount = float(input("Expense amount: ").strip() or 0)
            category = input("Category: ").strip() or "Miscellaneous"
            wallet_used = input("Wallet used: ").strip() or "Cash"
            payment_method = input("Payment method: ").strip() or "Cash"
            vendor = input("Vendor/shop name: ").strip() or None
            notes = input("Notes: ").strip() or None
            if manager.record_expense(member_id, amount, category, wallet_used, payment_method, vendor=vendor, notes=notes):
                print("Expense recorded.")
            else:
                print("Failed to record expense. Check balance and data.")
        elif choice == "6":
            dashboard = manager.get_family_dashboard()
            print(json.dumps(dashboard, indent=2))
        elif choice == "7":
            query = input("Search query: ").strip()
            results = manager.search_expenses(query)
            print(json.dumps(results, indent=2))
        elif choice == "8":
            member_id = input("Member ID (optional): ").strip() or None
            category = input("Category (optional): ").strip() or None
            wallet_used = input("Wallet used (optional): ").strip() or None
            payment_method = input("Payment method (optional): ").strip() or None
            min_amount = input("Minimum amount (optional): ").strip()
            max_amount = input("Maximum amount (optional): ").strip()
            start_date = input("Start date YYYY-MM-DD (optional): ").strip() or None
            end_date = input("End date YYYY-MM-DD (optional): ").strip() or None
            results = manager.filter_expenses(
                member_id=member_id,
                category=category,
                wallet_used=wallet_used,
                payment_method=payment_method,
                min_amount=float(min_amount) if min_amount else None,
                max_amount=float(max_amount) if max_amount else None,
                start_date=start_date,
                end_date=end_date,
            )
            print(json.dumps(results, indent=2))
        elif choice == "9":
            category = input("New category name: ").strip()
            if manager.add_custom_category(category):
                print("Category added.")
            else:
                print("Failed to add category or it already exists.")
        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
