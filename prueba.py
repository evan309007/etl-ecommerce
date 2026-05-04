from app import app

print("Rutas registradas en app:")
for rule in app.url_map.iter_rules():
    print(f"  {rule.endpoint}: {rule.rule}")