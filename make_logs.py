import random
from datetime import datetime, timedelta
import pandas as pd

random.seed(42)
start = datetime(2026, 10, 1, 8, 0, 0)
users = ["alice", "bob", "carol", "dave", "erin"]
normal_ips = [f"10.0.0.{i}" for i in range(10, 30)]
rows = []

for i in range(3000):
    t = start + timedelta(seconds=random.randint(0, 6 * 3600))
    status = random.choices(["success", "failed"], weights=[95, 5])[0]
    rows.append((t, random.choice(normal_ips), random.choice(users), "login", status))

attack_start = start + timedelta(hours=3)
for i in range(200):
    t = attack_start + timedelta(seconds=random.randint(0, 300))
    rows.append((t, "203.0.113.50", random.choice(users), "login", "failed"))

df = pd.DataFrame(rows, columns=["time", "ip", "user", "event", "status"])
df = df.sort_values("time").reset_index(drop=True)
df.to_csv("data/auth_logs.csv", index=False)
print(df.shape)