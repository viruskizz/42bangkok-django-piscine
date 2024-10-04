from machine import CoffeeMachine
import beverages

if __name__ == '__main__':
    machine = CoffeeMachine()
    for i in range(22):
        print(f'[{i}]')
        try:
            item = machine.serve(beverages.Cappuccino())
            print(item)
        except CoffeeMachine.BrokenMachineException as e:
            print(f'Error: {e}')
            machine.repair()
