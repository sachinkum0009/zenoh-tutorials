import zenoh, time

def listener(sample):
    print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')")

session = zenoh.open(zenoh.Config())
sub = session.declare_subscriber('myhome/kitchen/temp', listener)
time.sleep(60)
