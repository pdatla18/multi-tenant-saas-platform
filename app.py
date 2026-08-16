import json


def create_tenant(id, name, plan, users):
    tenant = {
        "id": id,
        "name": name,
        "plan": plan,
        "users": users
    }
    return tenant


def find_tenant(name):
    for tenant in tenants:
        if tenant["name"].lower() == name.lower():
            return tenant
    return None


def save_tenants():
    with open("tenants.json", "w") as file:
        json.dump(tenants, file, indent=4)


def load_tenants():
    try:
        with open("tenants.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_restaurants():
    with open("restaurants.json", "w") as file:
        json.dump(restaurants, file, indent=4)


def load_restaurants():
    try:
        with open("restaurants.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


tenants = load_tenants()
restaurants = load_restaurants()


def assign_existing_ids(tenants):
    next_id = 180201

    for tenant in tenants:
        if "id" not in tenant:
            tenant["id"] = next_id
            next_id += 1

    return tenants


print("LOADED TENANTS:", tenants)


def create_restaurant(tenant_id, restaurant_name, full_name, city):
    restaurant = {
        "tenant_id": tenant_id,
        "restaurant_name": restaurant_name,
        "full_name": full_name,
        "city": city
    }

    return restaurant


fayl_restaurant = create_restaurant(
    180295,
    "Fayl",
    "Food As You Like",
    "Hyderabad"
)

# Keep these commented for now so Fayl does not get duplicated
if not any(
    restaurant["tenant_id"] == fayl_restaurant["tenant_id"]
    for restaurant in restaurants
):
    restaurants.append(fayl_restaurant)
    save_restaurants()


while True:
    print("\nTenant Management System")
    print("1. View all tenants")
    print("2. Find a tenant")
    print("3. Add a tenant")
    print("4. Edit a tenant")
    print("5. Delete a tenant")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        for tenant in tenants:
            print(tenant)

    elif choice == "2":
        search_name = input("Enter tenant name: ")
        result = find_tenant(search_name)

        if result:
            print("Tenant found!")
            print("ID:", result["id"])
            print("Name:", result["name"])
            print("Plan:", result["plan"])
            print("Users:", result["users"])
        else:
            print("Tenant not found.")

    elif choice == "3":
        new_id = input("Enter the id: ")
        new_name = input("Enter new tenant name: ")
        new_plan = input("Enter plan: ")
        new_users = int(input("Enter number of users: "))

        new_tenant = create_tenant(
            new_id,
            new_name,
            new_plan,
            new_users
        )

        tenants.append(new_tenant)
        save_tenants()

        print("Tenant added successfully!")

    elif choice == "4":
        name = input("Enter tenant name to edit: ")

        tenant = find_tenant(name)

        if tenant:
            print("Tenant found!")
            print(tenant)

            print("\nWhat do you want to edit?")
            print("1. Name")
            print("2. Plan")
            print("3. Users")

            edit_choice = input("Choose an option: ")

            if edit_choice == "1":
                new_name = input("Enter new tenant name: ")
                tenant["name"] = new_name
                save_tenants()
                print("Name updated successfully!")

            elif edit_choice == "2":
                new_plan = input("Enter new plan: ")
                tenant["plan"] = new_plan
                save_tenants()
                print("Plan updated successfully!")

            elif edit_choice == "3":
                new_users = int(
                    input("Enter new number of users: ")
                )
                tenant["users"] = new_users
                save_tenants()
                print("Users updated successfully!")

            else:
                print("Invalid edit option.")

        else:
            print("Tenant not found.")

    elif choice == "5":
        name = input("Enter tenant name to delete: ")

        tenant = find_tenant(name)

        if tenant:
            print("Tenant found!")
            print(tenant)

            confirm = input(
                "Are you sure you want to delete this tenant? (yes/no): "
            )

            if confirm.lower() == "yes":
                tenants.remove(tenant)
                save_tenants()
                print("Tenant deleted successfully!")
            else:
                print("Deletion cancelled.")

        else:
            print("Tenant not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
