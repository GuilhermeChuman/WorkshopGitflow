import subprocess

def main():
    entrada = input("Entre com uma feature: ")
    feature(entrada)

def feature(featureIndex):
    
    subprocess.run(["python", featureIndex+".py"])

main()