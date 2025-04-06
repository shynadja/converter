from converters.currency_converter import UsdToRubConverter, UsdToEurConverter, UsdToGbpConverter, UsdToCnyConverter


def main():
    amount = float(input('Введите значение в USD: '))

    print(f'Converting {amount:.2f} USD...')

    rub_converter = UsdToRubConverter()
    print(f'{amount:.2f} USD to RUB: {rub_converter.convert(amount):.2f}')

    eur_converter = UsdToEurConverter()
    print(f'{amount:.2f} USD to EUR: {eur_converter.convert(amount):.2f}')

    gbp_converter = UsdToGbpConverter()
    print(f'{amount:.2f} USD to GBP: {gbp_converter.convert(amount):.2f}')

    cny_converter = UsdToCnyConverter()
    print(f'{amount:.2f} USD to CNY: {cny_converter.convert(amount):.2f}')


if __name__ == '__main__':
    main()