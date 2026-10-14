
#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone

output = Path("sample_activity.log")
message = (
    "Benign sample executed at "
    f"{datetime.now(timezone.utc).isoformat()}\n"
)

output.write_text(message, encoding="utf-8")
print(f"Created {output.resolve()}")
