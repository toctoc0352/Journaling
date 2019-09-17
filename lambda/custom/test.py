import yaml

with open("message.yml", "r") as yf:
    hoge = yaml.safe_load(yf)
    print(hoge["help"])
