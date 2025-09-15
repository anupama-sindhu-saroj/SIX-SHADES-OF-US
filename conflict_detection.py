trains = [
    {"id": "TrainA", "track": "T1", "platform": "P1"},
    {"id": "TrainB", "track": "T1", "platform": "P2"},
    {"id": "TrainC", "track": "T2", "platform": "P1"},
]

def detect_conflicts(trains):
    conflicts = []

    # --- Track Conflicts ---
    track_usage = {}
    for t in trains:
        track_usage.setdefault(t["track"], []).append(t["id"])
    
    for track, users in track_usage.items():
        if len(users) > 1:
            conflicts.append({
                "type": "TRACK",
                "track": track,
                "trains": users
            })

    # --- Platform Conflicts ---
    platform_usage = {}
    for t in trains:
        platform_usage.setdefault(t["platform"], []).append(t["id"])
    
    for platform, users in platform_usage.items():
        if len(users) > 1:
            conflicts.append({
                "type": "PLATFORM",
                "platform": platform,
                "trains": users
            })

    return conflicts


def show_conflicts(conflicts):
    if not conflicts:
        print("✅ No conflicts detected.")
    else:
        for c in conflicts:
            if c["type"] == "TRACK":
                print(f"🚨 [TRACK CONFLICT] Track {c['track']} used by {', '.join(c['trains'])}")
            elif c["type"] == "PLATFORM":
                print(f"🚨 [PLATFORM CONFLICT] Platform {c['platform']} requested by {', '.join(c['trains'])}")


if __name__ == "__main__":
    conflicts = detect_conflicts(trains)
    show_conflicts(conflicts)
