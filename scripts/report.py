import sqlite3

conn = sqlite3.connect("session.sqlite")
cursor = conn.cursor()

# Total de mutantes
total = cursor.execute("""
SELECT COUNT(*) FROM work_items
""").fetchone()[0]

# Contagem por resultado
results = cursor.execute("""
SELECT test_outcome, COUNT(*)
FROM work_results
GROUP BY test_outcome
""").fetchall()

killed = 0
survived = 0
others = {}

for outcome, count in results:
    outcome = outcome.lower()

    if outcome == "killed":
        killed = count
    elif outcome == "survived":
        survived = count
    else:
        others[outcome] = count

score = (killed / total) * 100 if total > 0 else 0

print("\n=== COSMIC RAY REPORT ===\n")
print(f"Mutants tested : {total}")
print(f"Killed         : {killed}")
print(f"Survived       : {survived}")
print(f"Mutation score : {score:.2f}%")

if others:
    print("\nOther outcomes:")
    for k, v in others.items():
        print(f"  {k}: {v}")