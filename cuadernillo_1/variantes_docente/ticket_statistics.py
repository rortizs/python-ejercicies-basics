# ticket_statistics.py

tickets = [
    {"id": 1, "priority": "MEDIA", "status": "ABIERTO"},
    {"id": 2, "priority": "ALTA", "status": "ABIERTO"},
    {"id": 3, "priority": "BAJA", "status": "RESUELTO"},
    {"id": 4, "priority": "ALTA", "status": "EN_PROCESO"},
]

priority_counts = {
    "BAJA": 0,
    "MEDIA": 0,
    "ALTA": 0,
}

status_counts = {
    "ABIERTO": 0,
    "EN_PROCESO": 0,
    "RESUELTO": 0,
}

for ticket in tickets:
    priority = ticket["priority"]
    status = ticket["status"]

    priority_counts[priority] += 1
    status_counts[status] += 1

total_tickets = len(tickets)

print("Estadísticas de tickets")
print("-----------------------")
print(f"Total de tickets: {total_tickets}")

print("\nPor prioridad:")
for priority, count in priority_counts.items():
    percentage = (count / total_tickets) * 100 if total_tickets > 0 else 0
    print(f"{priority}: {count} ({percentage:.2f}%)")

print("\nPor estado:")
for status, count in status_counts.items():
    percentage = (count / total_tickets) * 100 if total_tickets > 0 else 0
    print(f"{status}: {count} ({percentage:.2f}%)")
