print("Welcome to the Multi-Tenant SaaS Platform")

tenant_name = input("Enter your company name: ")

print("Welcome,", tenant_name)


tenant = {
    "name": tenant_name,
    "plan": "Free",
    "users": 1
}
print(tenant)


tenants = []

tenants.append(tenant)

print(tenants)

second_tenant_name = input("Enter another company name: ")

second_tenant = {
    "name": second_tenant_name,
    "plan": "Free",
    "users": 1
}

tenants.append(second_tenant)

print(tenants)

for number in range(3):
    print(number)

for number in range(3):
    company_name = input("Enter company name: ")
    print(company_name)


companies = []

for number in range(3):
    company_name = input("Enter company name: ")
    companies.append(company_name)

print(companies)


tenants = []

for number in range(3):
    company_name = input("Enter company name: ")

    tenant = {
        "name": company_name,
        "plan": "Free",
        "users": 1
    }

    tenants.append(tenant)

print(tenants)

for tenant in tenants:
    print(tenant["name"])

for tenant in tenants:
    print(
        f'{tenant["name"]} is on the {tenant["plan"]} plan with {tenant["users"]} user.')

for tenant in tenants:
    if tenant["plan"] == "Free":
        print(f'{tenant["name"]} has limited features.')

tenants[1]["plan"] = "Pro"

for tenant in tenants:
    if tenant["plan"] == "Free":
        print(f'{tenant["name"]} has limited features.')
    else:
        print(f'{tenant["name"]} has premium features.')

tenants[2]["plan"] = "Enterprise"

for tenant in tenants:
    if tenant["plan"] == "Free":
        print(f'{tenant["name"]} has limited features.')

    elif tenant["plan"] == "Pro":
        print(f'{tenant["name"]} has premium features.')

    else:
        print(f'{tenant["name"]} has enterprise features.')

new_tenants = []

for number in range(3):
    company_name = input("Enter company name: ")
    company_plan = input("Enter plan (Free/Pro/Enterprise): ").lower()

    tenant = {
        "name": company_name,
        "plan": company_plan,
        "users": 1
    }

    new_tenants.append(tenant)

print(new_tenants)

for tenant in new_tenants:
    if tenant["plan"] == "free":
        print(f'{tenant["name"]} has limited features.')

    elif tenant["plan"] == "pro":
        print(f'{tenant["name"]} has premium features.')

    else:
        print(f'{tenant["name"]} has enterprise features.')


for tenant in new_tenants:
    if tenant["plan"] == "free":
        print(f'{tenant["name"]} has limited features.')

    elif tenant["plan"] == "pro":
        print(f'{tenant["name"]} has premium features.')

    elif tenant["plan"] == "enterprise":
        print(f'{tenant["name"]} has enterprise features.')

    else:
        print(f'{tenant["name"]} has an invalid plan.')
