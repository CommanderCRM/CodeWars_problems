def create_phone_number(n):
    stri = "({prefix}) {fix}-{main}"
    prefix = ""
    fix = ""
    main = ""
    for i in range(3):
        prefix += str(n[i])
    for i in range(3, 6):
        fix += str(n[i])
    for i in range(6, 10):
        main += str(n[i])
    return stri.format(prefix=prefix, fix=fix, main=main)
