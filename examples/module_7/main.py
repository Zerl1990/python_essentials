import examples.module_7.module_1 as module_1
import examples.module_7.sub_module.sub_module_1 as sub_module_1

print(f'Hi from: {__name__}')

if __name__ == '__main__':
    print("I am the main module")
    print(module_1.counter)
    module_1.sum_list([1, 2, 3, 4, 5])
    module_1.prod_list([4, 6, 9])



