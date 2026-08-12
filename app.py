print("Welcome to the Multi-Tenant SaaS Platform")

tenant_name = input("Enter your company name: ")

print("Welcome,", tenant_name)


tenant = {
    "name": tenant_name,
    "plan": "Free",
    "users": 1
}
print(tenant)
