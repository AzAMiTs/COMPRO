def main():
    infile = open('philo.txt','r')
    
    file_contents = infile.read()
    
    infile.close()
    
    print(file_contents)
    
main()