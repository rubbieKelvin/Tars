from .network import client

cli = client("DESKTOP-CGV7FBC")
cli.connect()

while True:
    cmd = input(f"{cli.host.lower()} $  ")
    res = cli.postcommand(cmd)
    if res is None:
        break
    else:
        print(res)
