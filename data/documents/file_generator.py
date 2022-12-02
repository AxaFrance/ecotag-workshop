import shutil


def generate_files(src, dst, name, extension):
    for i in range(0, 20):
        print("Creating file number " + str(i))
        shutil.copy(src, dst + "\\" + name + "_" + str(i) + extension)


#if __name__ == '__main__':
source = r'C:\data\documents\demo.eml'
destination = r'C:\data\documents\docs'
file_name = "demo"
file_extension = ".eml"
generate_files(source, destination, file_name, file_extension)