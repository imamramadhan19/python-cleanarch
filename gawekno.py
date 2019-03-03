import sys
import os

def main():

    try:
        root_dir = 'src/{}'.format(str(sys.argv[1]))
        main_dir = '{}/{}'.format(str(root_dir), str(sys.argv[2]))
        sub_dir = ['delivery', 'domain', 'repository', 'serializers', 'usecase', 'validator']

        for d in sub_dir:
            dir_location = '{}/{}'.format(main_dir, d)
            os.makedirs(dir_location)
            open("{}/__init__.py".format(dir_location), "w+")

        open("{}/__init__.py".format(main_dir), "w+")
        open("{}/__init__.py".format(root_dir), "w+")

        print("====Sukses Coy====")

    except:

        print("====Gagal Coy====")

if __name__ == '__main__':
    main()


