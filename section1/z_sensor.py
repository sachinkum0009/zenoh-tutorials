import zenoh, random, time

def read_temp():
    return random.randint(15, 30)

session = zenoh.open(zenoh.Config())
key = 'myhome/kitchen/temp'
pub = session.declare_publisher(key)

while True:
    t = read_temp()
    buf = f"{t}"
    print(f"Putting Data ('{key}': '{buf}')...")
    pub.put(buf)
    time.sleep(1)
