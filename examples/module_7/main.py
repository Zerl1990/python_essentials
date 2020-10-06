import examples.module_7.module_1 as module_1
import examples.module_7.sub_package.sub_module_1 as sub_module_1

print(f'Hi from: {__name__}')

if __name__ == '__main__':
    print("I am the main module")
    lst = sub_module_1.random_list(100, 5, 10)
    module_1.sum_list(lst)
    module_1.prod_list(lst)


