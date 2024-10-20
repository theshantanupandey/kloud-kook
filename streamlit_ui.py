import streamlit as st
import requests

# Base URL for the backend API
BASE_URL = "http://localhost:8000/api/"

# Function to fetch data from the backend API
def fetch_data(endpoint):
    response = requests.get(BASE_URL + endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data from {endpoint}")
        return None

# Function to post data to the backend API
def post_data(endpoint, data):
    response = requests.post(BASE_URL + endpoint, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        st.error(f"Failed to post data to {endpoint}")
        return None

# Function to update data in the backend API
def update_data(endpoint, data):
    response = requests.put(BASE_URL + endpoint, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to update data at {endpoint}")
        return None

# Function to delete data from the backend API
def delete_data(endpoint):
    response = requests.delete(BASE_URL + endpoint)
    if response.status_code == 204:
        return True
    else:
        st.error(f"Failed to delete data from {endpoint}")
        return False

# Streamlit App
st.title("Cloud Kitchen Management Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Users", "Orders", "Meals", "Inventory", "Delivery", "Payments", "Communication"])

# Users Section
if selection == "Users":
    st.header("Users")
    users = fetch_data("users/")
    if users:
        for user in users:
            st.write(f"Username: {user['username']}, Email: {user['email']}, Role: {user['role']}")

    # Create User
    st.subheader("Create User")
    username = st.text_input("Username")
    email = st.text_input("Email")
    role = st.selectbox("Role", ["customer", "staff"])
    if st.button("Create"):
        new_user = {
            "username": username,
            "email": email,
            "role": role
        }
        post_data("users/", new_user)
        st.success("User created successfully!")

    # Update User
    st.subheader("Update User")
    user_id = st.text_input("User ID to update")
    if user_id:
        user = fetch_data(f"users/{user_id}/")
        if user:
            username = st.text_input("New Username", value=user['username'])
            email = st.text_input("New Email", value=user['email'])
            role = st.selectbox("New Role", ["customer", "staff"], index=["customer", "staff"].index(user['role']))
            if st.button("Update"):
                updated_user = {
                    "username": username,
                    "email": email,
                    "role": role
                }
                update_data(f"users/{user_id}/", updated_user)
                st.success("User updated successfully!")

    # Delete User
    st.subheader("Delete User")
    user_id = st.text_input("User ID to delete")
    if st.button("Delete"):
        delete_data(f"users/{user_id}/")
        st.success("User deleted successfully!")

# Orders Section
elif selection == "Orders":
    st.header("Orders")
    orders = fetch_data("orders/")
    if orders:
        for order in orders:
            st.write(f"Order ID: {order['id']}, User: {order['user']}, Status: {order['status']}")

    # Create Order
    st.subheader("Create Order")
    user_id = st.text_input("User ID")
    status = st.selectbox("Status", ["pending", "processing", "completed", "cancelled"])
    if st.button("Create"):
        new_order = {
            "user": user_id,
            "status": status
        }
        post_data("orders/", new_order)
        st.success("Order created successfully!")

    # Update Order
    st.subheader("Update Order")
    order_id = st.text_input("Order ID to update")
    if order_id:
        order = fetch_data(f"orders/{order_id}/")
        if order:
            status = st.selectbox("New Status", ["pending", "processing", "completed", "cancelled"], index=["pending", "processing", "completed", "cancelled"].index(order['status']))
            if st.button("Update"):
                updated_order = {
                    "status": status
                }
                update_data(f"orders/{order_id}/", updated_order)
                st.success("Order updated successfully!")

    # Delete Order
    st.subheader("Delete Order")
    order_id = st.text_input("Order ID to delete")
    if st.button("Delete"):
        delete_data(f"orders/{order_id}/")
        st.success("Order deleted successfully!")

# Meals Section
elif selection == "Meals":
    st.header("Meals")
    meals = fetch_data("meals/")
    if meals:
        for meal in meals:
            st.write(f"Meal Name: {meal['name']}, Price: {meal['price']}, Available: {meal['is_available']}")

    # Create Meal
    st.subheader("Create Meal")
    name = st.text_input("Name")
    price = st.number_input("Price", min_value=0.0)
    is_available = st.checkbox("Is Available")
    if st.button("Create"):
        new_meal = {
            "name": name,
            "price": price,
            "is_available": is_available
        }
        post_data("meals/", new_meal)
        st.success("Meal created successfully!")

    # Update Meal
    st.subheader("Update Meal")
    meal_id = st.text_input("Meal ID to update")
    if meal_id:
        meal = fetch_data(f"meals/{meal_id}/")
        if meal:
            name = st.text_input("New Name", value=meal['name'])
            price = st.number_input("New Price", value=meal['price'], min_value=0.0)
            is_available = st.checkbox("Is Available", value=meal['is_available'])
            if st.button("Update"):
                updated_meal = {
                    "name": name,
                    "price": price,
                    "is_available": is_available
                }
                update_data(f"meals/{meal_id}/", updated_meal)
                st.success("Meal updated successfully!")

    # Delete Meal
    st.subheader("Delete Meal")
    meal_id = st.text_input("Meal ID to delete")
    if st.button("Delete"):
        delete_data(f"meals/{meal_id}/")
        st.success("Meal deleted successfully!")

# Inventory Section
elif selection == "Inventory":
    st.header("Inventory")
    ingredients = fetch_data("inventory/ingredients/")
    if ingredients:
        for ingredient in ingredients:
            st.write(f"Ingredient: {ingredient['name']}, Quantity: {ingredient['quantity']}, Unit: {ingredient['unit']}")

    # Create Ingredient
    st.subheader("Create Ingredient")
    name = st.text_input("Name")
    quantity = st.number_input("Quantity", min_value=0)
    unit = st.text_input("Unit")
    if st.button("Create"):
        new_ingredient = {
            "name": name,
            "quantity": quantity,
            "unit": unit
        }
        post_data("inventory/ingredients/", new_ingredient)
        st.success("Ingredient created successfully!")

    # Update Ingredient
    st.subheader("Update Ingredient")
    ingredient_id = st.text_input("Ingredient ID to update")
    if ingredient_id:
        ingredient = fetch_data(f"inventory/ingredients/{ingredient_id}/")
        if ingredient:
            name = st.text_input("New Name", value=ingredient['name'])
            quantity = st.number_input("New Quantity", value=ingredient['quantity'], min_value=0)
            unit = st.text_input("New Unit", value=ingredient['unit'])
            if st.button("Update"):
                updated_ingredient = {
                    "name": name,
                    "quantity": quantity,
                    "unit": unit
                }
                update_data(f"inventory/ingredients/{ingredient_id}/", updated_ingredient)
                st.success("Ingredient updated successfully!")

    # Delete Ingredient
    st.subheader("Delete Ingredient")
    ingredient_id = st.text_input("Ingredient ID to delete")
    if st.button("Delete"):
        delete_data(f"inventory/ingredients/{ingredient_id}/")
        st.success("Ingredient deleted successfully!")

# Delivery Section
elif selection == "Delivery":
    st.header("Delivery")
    deliveries = fetch_data("deliveries/")
    if deliveries:
        for delivery in deliveries:
            st.write(f"Delivery ID: {delivery['id']}, Order: {delivery['order']}, Status: {delivery['status']}")

    # Create Delivery
    st.subheader("Create Delivery")
    order_id = st.text_input("Order ID")
    status = st.selectbox("Status", ["pending", "out_for_delivery", "delivered", "cancelled"])
    if st.button("Create"):
        new_delivery = {
            "order": order_id,
            "status": status
        }
        post_data("deliveries/", new_delivery)
        st.success("Delivery created successfully!")

    # Update Delivery
    st.subheader("Update Delivery")
    delivery_id = st.text_input("Delivery ID to update")
    if delivery_id:
        delivery = fetch_data(f"deliveries/{delivery_id}/")
        if delivery:
            status = st.selectbox("New Status", ["pending", "out_for_delivery", "delivered", "cancelled"], index=["pending", "out_for_delivery", "delivered", "cancelled"].index(delivery['status']))
            if st.button("Update"):
                updated_delivery = {
                    "status": status
                }
                update_data(f"deliveries/{delivery_id}/", updated_delivery)
                st.success("Delivery updated successfully!")

    # Delete Delivery
    st.subheader("Delete Delivery")
    delivery_id = st.text_input("Delivery ID to delete")
    if st.button("Delete"):
        delete_data(f"deliveries/{delivery_id}/")
        st.success("Delivery deleted successfully!")

# Payments Section
elif selection == "Payments":
    st.header("Payments")
    payments = fetch_data("payments/")
    if payments:
        for payment in payments:
            st.write(f"Payment ID: {payment['id']}, Order: {payment['order']}, Amount: {payment['amount']}")

    # Create Payment
    st.subheader("Create Payment")
    order_id = st.text_input("Order ID")
    amount = st.number_input("Amount", min_value=0.0)
    status = st.selectbox("Status", ["pending", "completed", "failed"])
    if st.button("Create"):
        new_payment = {
            "order": order_id,
            "amount": amount,
            "status": status
        }
        post_data("payments/", new_payment)
        st.success("Payment created successfully!")

    # Update Payment
    st.subheader("Update Payment")
    payment_id = st.text_input("Payment ID to update")
    if payment_id:
        payment = fetch_data(f"payments/{payment_id}/")
        if payment:
            amount = st.number_input("New Amount", value=payment['amount'], min_value=0.0)
            status = st.selectbox("New Status", ["pending", "completed", "failed"], index=["pending", "completed", "failed"].index(payment['status']))
            if st.button("Update"):
                updated_payment = {
                    "amount": amount,
                    "status": status
                }
                update_data(f"payments/{payment_id}/", updated_payment)
                st.success("Payment updated successfully!")

    # Delete Payment
    st.subheader("Delete Payment")
    payment_id = st.text_input("Payment ID to delete")
    if st.button("Delete"):
        delete_data(f"payments/{payment_id}/")
        st.success("Payment deleted successfully!")

# Communication Section
elif selection == "Communication":
    st.header("Communication")
    messages = fetch_data("communication/messages/")
    if messages:
        for message in messages:
            st.write(f"Message from {message['sender']} to {message['receiver']}: {message['content']}")

    # Create Message
    st.subheader("Create Message")
    sender_id = st.text_input("Sender ID")
    receiver_id = st.text_input("Receiver ID")
    content = st.text_area("Content")
    if st.button("Create"):
        new_message = {
            "sender": sender_id,
            "receiver": receiver_id,
            "content": content
        }
        post_data("communication/messages/", new_message)
        st.success("Message created successfully!")

    # Update Message
    st.subheader("Update Message")
    message_id = st.text_input("Message ID to update")
    if message_id:
        message = fetch_data(f"communication/messages/{message_id}/")
        if message:
            content = st.text_area("New Content", value=message['content'])
            if st.button("Update"):
                updated_message = {
                    "content": content
                }
                update_data(f"communication/messages/{message_id}/", updated_message)
                st.success("Message updated successfully!")

    # Delete Message
    st.subheader("Delete Message")
    message_id = st.text_input("Message ID to delete")
    if st.button("Delete"):
        delete_data(f"communication/messages/{message_id}/")
        st.success("Message deleted successfully!")

# Run the Streamlit app
if __name__ == "__main__":
    st.write("Welcome to the Cloud Kitchen Management Dashboard!")