
def main():
    import random

    random2 = random.randint(1,6)

    progi = random.randint(0,11)


    e_o_e, f_o_e, fis_o_e,ges_o_e, g_o_e, gis_o_e,as_o_e, a_o_e, ais_o_e,b_o_e,h_o_e, c_o_e, cis_o_e,des_o_e, d_o_e, dis_o_e,es_o_e = ["E", "F", "FIS","GES","G","GIS","AS", "A", "AIS","B", "H", "C", "CIS","DES", "D", "DIS","ES"]
    e_o_e1, f_o_e1, fis_o_e1,ges_o_e1, g_o_e1, gis_o_e1,as_o_e1, a_o_e1, ais_o_e1,b_o_e1, h_o_e1, c_o_e1, cis_o_e1,des_o_e1, d_o_e1, dis_o_e1,es_o_e1 = ["E", "F","FIS","GES", "G","GIS","AS", "A","AIS","B", "H","C", "CIS","DES","D", "DIS","ES"]
    a_o_a, ais_o_a,b_o_a, h_o_a, c_o_a, cis_o_a,des_o_a, d_o_a, dis_o_a,es_o_a, e_o_a, f_o_a, fis_o_a,ges_o_a, g_o_a, gis_o_a,as_o_a = ["A", "AIS","B", "H", "C","CIS","DES", "D", "DIS","ES", "E", "F", "FIS","GES", "G", "GIS","AS"]
    d_o_d, dis_o_d,es_o_d, e_o_d, f_o_d, fis_o_d,ges_o_d, g_o_d, gis_o_d,as_o_d, a_o_d, ais_o_d,b_o_d, h_o_d, c_o_d, cis_o_d,des_o_d = ["D", "DIS","ES", "E", "F","FIS","GES", "G", "GIS","AS", "A","AIS","B", "H", "C", "CIS","DES"]
    g_o_g, gis_o_g,as_o_g, a_o_g, ais_o_g,b_o_g, h_o_g, c_o_g, cis_o_g,des_o_g, d_o_g, dis_o_g,es_o_g, e_o_g, f_o_g, fis_o_g,ges_o_g = ["G", "GIS","AS", "A", "AIS","B", "H", "C","CIS","DES", "D", "DIS","ES", "E", "F", "FIS","GES"]
    h_o_h, c_o_h, cis_o_h,des_o_h, d_o_h, dis_o_h,es_o_h, e_o_h, f_o_h, fis_o_h,ges_o_h, g_o_h, gis_o_h,as_o_h, a_o_h, ais_o_h,b_o_h = ["H", "C", "CIS","DES", "D","DIS","ES", "E", "F", "FIS","GES","G", "GIS","AS", "A","AIS","B"]


    class String:
        def __init__(self, e, f, fis, g, gis, a, ais, h, c, cis, d, dis):
            self.e = e
            self.f = f
            self.fis = fis
            self.g = g
            self.gis = gis
            self.a = a
            self.ais = ais
            self.h = h
            self.c = c
            self.cis = cis
            self.d = d
            self.dis = dis

        def struna_E(self):
            if progi == 0:
                self.e = {self.e: 0}
                return self.e
            elif progi == 1:
                self.f = {self.f: 1}
                return self.f
            elif progi == 2:
                self.fis = {self.fis: 2}
                return self.fis
            elif progi == 3:
                self.g = {self.g: 3}
                return self.g
            elif progi == 4:
                self.gis = {self.gis: 4}
                return self.gis
            elif progi == 5:
                self.a = {self.a: 5}
                return self.a
            elif progi == 6:
                self.ais = {self.ais: 6}
                return self.ais
            elif progi == 7:
                self.h = {self.h: 7}
                return self.h
            elif progi == 8:
                self.c = {self.c: 8}
                return self.c
            elif progi == 9:
                self.cis = {self.cis: 9}
                return self.cis
            elif progi == 10:
                self.d = {self.d: 10}
                return self.d
            elif progi == 11:
                self.dis = {self.dis: 11}
                return self.dis


        def struna_A(self):
            if progi == 0:
                self.a = {self.a: 0}
                return self.a
            elif progi == 1:
                self.ais = {self.ais: 1}
                return self.ais
            elif progi == 2:
                self.h = {self.h: 2}
                return self.h
            elif progi == 3:
                self.c = {self.c: 3}
                return self.c
            elif progi == 4:
                self.cis = {self.cis: 4}
                return self.cis
            elif progi == 5:
                self.d = {self.d: 5}
                return self.d
            elif progi == 6:
                self.dis = {self.dis: 6}
                return self.dis
            elif progi == 7:
                self.e = {self.e: 7}
                return self.e
            elif progi == 8:
                self.f = {self.f: 8}
                return self.f
            elif progi == 9:
                self.fis = {self.fis: 9}
                return self.fis
            elif progi == 10:
                self.g = {self.g: 10}
                return self.g
            elif progi == 11:
                self.gis = {self.gis: 11}
                return self.gis


        def struna_D(self):
            if progi == 0:
                self.d = {self.d: 0}
                return self.d
            elif progi == 1:
                self.dis = {self.dis: 1}
                return self.dis
            elif progi == 2:
                self.e = {self.e: 2}
                return self.e
            elif progi == 3:
                self.f= {self.f: 3}
                return self.f
            elif progi == 4:
                self.fis = {self.fis: 4}
                return self.fis
            elif progi == 5:
                self.g = {self.g: 5}
                return self.g
            elif progi == 6:
                self.gis = {self.gis: 6}
                return self.gis
            elif progi == 7:
                self.a = {self.a: 7}
                return self.a
            elif progi == 8:
                self.ais = {self.ais: 8}
                return self.ais
            elif progi == 9:
                self.h = {self.h: 9}
                return self.h
            elif progi == 10:
                self.c = {self.c: 10}
                return self.c
            elif progi == 11:
                self.cis = {self.cis: 11}
                return self.cis


        def strunga_G(self):
            if progi == 0:
                self.g = {self.g: 0}
                return self.g
            elif progi == 1:
                self.gis = {self.gis: 1}
                return self.gis
            elif progi == 2:
                self.a = {self.a: 2}
                return self.a
            elif progi == 3:
                self.ais= {self.ais: 3}
                return self.ais
            elif progi == 4:
                self.h = {self.h: 4}
                return self.h
            elif progi == 5:
                self.c = {self.c: 5}
                return self.c
            elif progi == 6:
                self.cis = {self.cis: 6}
                return self.cis
            elif progi == 7:
                self.d = {self.d: 7}
                return self.d
            elif progi == 8:
                self.dis = {self.dis: 8}
                return self.dis
            elif progi == 9:
                self.e = {self.e: 9}
                return self.e
            elif progi == 10:
                self.f = {self.f: 10}
                return self.f
            elif progi == 11:
                self.fis = {self.fis: 11}
                return self.fis


        def strunga_H(self):
            if progi == 0:
                self.h = {self.h: 0}
                return self.h
            elif progi == 1:
                self.c = {self.c: 1}
                return self.c
            elif progi == 2:
                self.cis = {self.cis: 2}
                return self.cis
            elif progi == 3:
                self.d= {self.d: 3}
                return self.d
            elif progi == 4:
                self.dis = {self.dis: 4}
                return self.dis
            elif progi == 5:
                self.e = {self.e: 5}
                return self.e
            elif progi == 6:
                self.f = {self.f: 6}
                return self.f
            elif progi == 7:
                self.fis = {self.fis: 7}
                return self.fis
            elif progi == 8:
                self.g = {self.g: 8}
                return self.g
            elif progi == 9:
                self.gis = {self.gis: 9}
                return self.gis
            elif progi == 10:
                self.a = {self.a: 10}
                return self.a
            elif progi == 11:
                self.ais = {self.ais: 11}
                return self.ais





    # string 6 have index 0 string 5 have index 1...
    # For evry number in progi i have to specify a number that describe a sound on a guitar string

    string_E = String(e_o_e, f_o_e,(fis_o_e,ges_o_e), g_o_e, (gis_o_e,as_o_e), a_o_e,(ais_o_e,b_o_e), h_o_e, c_o_e, (cis_o_e,des_o_e), d_o_e, (dis_o_e,es_o_e))
    string_A = String(e_o_a,f_o_a,(fis_o_a,ges_o_a),g_o_a,(gis_o_a,as_o_a),a_o_a,(ais_o_a,b_o_a),h_o_a,c_o_a,(cis_o_a,des_o_a),d_o_a,(dis_o_a,es_o_a))
    string_D = String(e_o_d,f_o_d,(fis_o_d,ges_o_d),g_o_d,(gis_o_d,as_o_d),a_o_d,(ais_o_d,b_o_d),h_o_d,c_o_d,(cis_o_d,des_o_d),d_o_d,(dis_o_d,es_o_d))
    string_G = String(e_o_g,f_o_g,(fis_o_g,ges_o_g),g_o_g,(gis_o_g,as_o_g),a_o_g,(ais_o_g,b_o_g),h_o_g,c_o_g,(cis_o_g,des_o_g),d_o_g,(dis_o_g,es_o_g))
    string_H = String(e_o_h,f_o_h,(fis_o_h,ges_o_h),g_o_h,(gis_o_h,as_o_h),a_o_h,(ais_o_h,b_o_h),h_o_h,c_o_h,(cis_o_h,des_o_h),d_o_h,(dis_o_h,es_o_h))
    string_E1 = String(e_o_e1,f_o_e1,(fis_o_e1,ges_o_e1),g_o_e1,(gis_o_e1,as_o_e1),a_o_e1,(ais_o_e1,b_o_e1),h_o_e1,c_o_e1,(cis_o_e1,des_o_e1),d_o_e1,(dis_o_e1,es_o_e1))


    varH = string_H.strunga_H()
    stringH_keys = varH.keys()
    list_of_string_h_keys = list(stringH_keys)

    def key_of_h():
        for key in list_of_string_h_keys:
            return key

    exceptionH = list(key_of_h())

    varG = string_G.strunga_G()
    stringG_keys = varG.keys()
    list_of_string_g_keys = list(stringG_keys)


    def key_of_G():
        for key in list_of_string_g_keys:
            return key

    exceptionG = list(key_of_G())


    varD = string_D.struna_D()
    stringD_keys = varD.keys()
    list_of_string_d_keys = list(stringD_keys)

    def key_of_d():
        for key in list_of_string_d_keys:
            return key

    exceptionD = list(key_of_d())


    varA = string_A.struna_A()
    stringA_keys = varA.keys()
    list_of_string_a_keys = list(stringA_keys)

    def key_of_string_A():
        for key in list_of_string_a_keys:
            return key

    exceptionA = list(key_of_string_A())



    var = string_E.struna_E()
    stringE_keys = var.keys()
    list_of_string_e_keys = list(stringE_keys)



    #HERE IS THE KEY FOR STRING E
    def key_of_stringE():
            for key in list_of_string_e_keys:
                return key

    exceptionE = list(key_of_stringE())

    def finall_test():
        print("Fret " + str(progi) + " string " + str(random2))
        guess = input("Enter the sound,or type [quit], to exit: ")
        if random2 == 6 and guess != "quit":
            if len(key_of_stringE()) != 2:
                odp = key_of_stringE()
                if guess.upper() == odp:
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + key_of_stringE())
                    main()
            elif len(key_of_stringE()) == 2:
                odp = exceptionE
                if guess.upper() in odp and odp != "" and odp != " ":
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + str(exceptionE))
                    main()
        elif random2 == 5 and guess != "quit":
            if len(key_of_string_A()) != 2:
                odp = key_of_string_A()
                if guess.upper() == odp:
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + key_of_string_A())
                    main()
            elif len(key_of_string_A()) == 2:
                odp = exceptionA
                if guess.upper() in odp and odp != "" and odp != " " and odp != "  ":
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + str(exceptionA))
                    main()
        elif random2 == 4 and guess != "quit":
            if len(key_of_d()) != 2:
                odp = key_of_d()
                if guess.upper() == odp:
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + key_of_d())
                    main()
            elif len(key_of_d()) == 2:
                odp = exceptionD
                if guess.upper() in odp and odp != "" and odp != " " and odp != "  ":
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + str(exceptionD))
                    main()
        elif random2 == 3 and guess != "quit":
            if len(key_of_G()) != 2:
                odp = key_of_G()
                if guess.upper() == odp:
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + key_of_G())
                    main()
            elif len(key_of_G()) == 2:
                odp = exceptionG
                if guess.upper() in odp and odp != "" and odp != " " and odp != "  ":
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + str(exceptionG))
                    main()
        elif random2 == 2 and guess != "quit":
            if len(key_of_h()) != 2:
                odp = key_of_h()
                if guess.upper() == odp:
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + key_of_h())
                    main()
            elif len(key_of_h()) == 2:
                odp = exceptionH
                if guess.upper() in odp and odp != "" and odp != " " and odp != "  ":
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + str(exceptionH))
                    main()
        elif random2 == 1 and guess != "quit":
            if len(key_of_stringE()) != 2:
                odp = key_of_stringE()
                if guess.upper() == odp:
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + key_of_stringE())
                    main()
            elif len(key_of_stringE()) == 2:
                odp = exceptionE
                if guess.upper() in odp and odp != "" and odp != " ":
                    print("Correct")
                    main()
                else:
                    print("Wrong key")
                    print("The correct answer is: " + str(exceptionE))
                    main()

    finall_test()


main()




