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
