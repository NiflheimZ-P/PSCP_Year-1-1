"""PongYa"""
def pongya():
    """PongYa"""
    time = int(input())
    if time%3 == 0 or str(time)[-1:] == "3":
        out = "PONG"
    else:
        out = time
    print(out)
pongya()
