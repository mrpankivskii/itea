from models import VerkhovnaRada, DBOfVerchovnaRada, Fraction, Deputat


def main():
    fraction = Fraction
    verkhovna_rada = VerkhovnaRada
    deputat = Deputat
    DBOfVerchovnaRada.read_from_DB()
    while True:
        input_number = input("""
        Введіть 1, щоб додати фракцію
        Введіть 2, щоб видалити фракцію
        Введіть 3, щоб очистити фракцію
        Введіть 4, щоб вивести фракції
        Введіть 5, щоб видалити фракцію
        Введіть 6, щоб додати депутата у фракцію
        Введіть 7, щоб видалити депутата із фракції
        Введіть 8, щоб вивести список хабарників у фракції
        Введіть 9, щоб вивести список  хабарників у раді
        Введіть 10, щоб вивести найбільшого хабарника у раді
        Введіть 11, щоб вивести найбільшого хабарника у фракції.
        Введіть 12, щоб перевірити чи є дупутат у фракції
        Введіть 13, щоб перевірити чи є депутат у раді
        Введіть 14, щоб дати хабаря депутату.
        Введіть 0, щоб вийти із програми. \n""")
        if input_number == '0':
            DBOfVerchovnaRada.write_to_DB()
            break
        elif input_number == '1':
            verkhovna_rada.add_fraction(Fraction)
        elif input_number == '2':
            verkhovna_rada.del_fraction(Fraction)
        elif input_number == '4':
            verkhovna_rada.print_all_fractions(Fraction)
        elif input_number == '5':
            verkhovna_rada.del_fraction(Fraction)
        elif input_number == '6':
            fraction.add_deputy(Deputat)
        elif input_number == '7':
            fraction.del_deputy(Deputat)
        elif input_number == '8':
            fraction.print_bribe_taker(Deputat)
        elif input_number == '14':
            deputat.give_tribute(Deputat, input('Input bribe value\n'))


if __name__ == "__main__":
    main()
