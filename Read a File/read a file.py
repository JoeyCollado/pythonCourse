


try:
    with open('C:\\Users\\akosi\\OneDrive\\Desktop\\Python\\python course\\Read a File') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found or path is incorrect.")
except Exception as e:
    print("An error occurred:", e)