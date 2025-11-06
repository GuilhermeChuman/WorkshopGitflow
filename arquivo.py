import subprocess

def main():
    print("Bem vindo!!!")
    entrada = input("Entre com uma feature: ")
    feature(entrada)

def feature(featureIndex):
    subprocess.run(["python", './WorkshopGitflow/'+featureIndex+".py"])

main()
