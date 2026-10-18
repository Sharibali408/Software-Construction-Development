# --- BEFORE (Deeply Nested) ---
def process_order_before(order, customer, inventory):
    if order:
        if customer:
            if customer.is_active:
                if order.is_valid:
                    if inventory.has_stock(order):
                        if customer.balance >= order.total:
                            process_payment(customer, order)
                            update_inventory(inventory, order)
                            send_confirmation(customer, order)
                            return True
    return False

# --- AFTER (Refactored with Guard Clauses) ---
def process_order_after(order, customer, inventory):
    # Guard Clauses: Check for invalid scenarios early and exit
    if not order:
        return False
    if not customer:
        return False
    if not customer.is_active:
        return False
    if not order.is_valid:
        return False
    if not inventory.has_stock(order):
        return False
    if customer.balance < order.total:
        return False

    # Happy Path: Everything is valid, now process the order
    process_payment(customer, order)
    update_inventory(inventory, order)
    send_confirmation(customer, order)
    return True