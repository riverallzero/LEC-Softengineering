def k2c(k):
    c = k - 273.15

    return c


def mi2km(mi):
    km = mi * 1.6

    return km


def main():
    k = 285.3
    mi = 300

    print('{:.1f} K => {:.1f} C'.format(k, k2c(k)))
    print('{:.1f} mile => {:.1f} km'.format(mi, mi2km(mi)))


if __name__ == '__main__':
    main()