def create_tenant(name, plan, users):
    tenant = {
        "name": name,
        "plan": plan,
        "users": users
    }
    return tenant


tenants = []

tenant1 = create_tenant("Aaromale", "pro", 30)
tenant2 = create_tenant("Netflix", "free", 500)

tenants.append(tenant1)
tenants.append(tenant2)

for tenant in tenants:
    print(tenant["name"])


def find_tenant(name):
    for tenant in tenants:
        if tenant["name"].lower() == name.lower():
            return tenant

    return None


result = find_tenant("Netflix")

print(result)


search_name = input("enter the tenant name: ")
result = find_tenant(search_name)
print(result)


search_name = input("Enter tenant name: ")

result = find_tenant(search_name)

if result:
    print("Tenant found!")
    print("Name:", result["name"])
    print("Plan:", result["plan"])
    print("Users:", result["users"])
else:
    print("Tenant not found.")


new_name = input("Enter new tenant name: ")
new_plan = input("Enter plan: ")
new_users = int(input("Enter number of users: "))

new_tenant = create_tenant(new_name, new_plan, new_users)

tenants.append(new_tenant)

search_new_tenant = input("Search for the new tenant: ")

result = find_tenant(search_new_tenant)

if result:
    print("Tenant found!")
    print("Name:", result["name"])
    print("Plan:", result["plan"])
    print("Users:", result["users"])
else:
    print("Tenant not found.")

print("Tenant added successfully!")
print(new_tenant)
