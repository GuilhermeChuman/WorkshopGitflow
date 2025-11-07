import subprocess

def main():
    entrada = input("Entre com uma feature: ")
    feature(entrada)

def feature(featureIndex):
<<<<<<< HEAD
    subprocess.run(["python", './WorkshopGitflow/'+featureIndex+".py"])
=======
    
    subprocess.run(["python", featureIndex+".py"])
>>>>>>> release/1.0

main()
