public static class RandHelper
{
    private static readonly Random random = new();

    public static T FromSet<T>(List<T> fullSet)
    {
        return random.GetItems(fullSet.ToArray(), 1)[0];
    }

    public static T FromSet<T>(T[] fullSet)
    {
        return random.GetItems(fullSet.ToArray(), 1)[0];
    }

    // I originally had dontPick as an optional parameter but those don't work the same as JS optional params
    // I got some error about [] not being constant at runtime
    // So I made an overload instead, I think we covered these
    public static T FromSet<T>(List<T> fullSet, List<T> dontPick)
    {
        List<T> chooseFrom = [];

        foreach (var item in fullSet)
        {
            if (!dontPick.Contains(item))
            {
                chooseFrom.Add(item);
            }
        }

        var roll = random.GetItems(chooseFrom.ToArray(), 1);
        return roll[0];
    }

    public static T FromSet<T>(T[] fullSet, List<string> dontPick)
    {
        return random.GetItems(fullSet, 1)[0];
    }

    public static bool FiftyFifty()
    {
        return random.GetItems([true, false], 1)[0];
    }

    // Ship List
    // https://memory-alpha.fandom.com/wiki/Category:Klingon_starships
    private static string[] KlingonShips =
    [
        "Amar",
        "B'Moth",
        "Bortas",
        "Buruk",
        "Che'Ta'",
        "Ch'Tang",
        "Devisor",
        "Drovana",
        "Fek'Ihr",
        "Gr'oth'",
        "Hegh'ta",
        "Bounty",
        "Hor'Cha",
        "Ki'tang",
        "Klothos",
        "K'mpec",
        "Koraga",
        "Korinar",
        "Kronos One",
        "Maht-H'a",
        "Malpara",
        "M'Char",
        "Negh'Var",
        "Ning'tao",
        "Orantho",
        "Pagh",
        "Par'tok",
        "P'Rang",
        "Qu'Vat",
        "Rotarran",
        "Sarcophagus",
        "Slivin",
        "Somraw",
        "T'Acog",
        "Toh'Kaht",
        "T'Ong",
        "Ursva",
        "Vorn",
        "Vor'nak",
        "Ya'Vang",
        "Y'tem"
    ];

    public static string RandKlingon(List<string> dontPick)
    {
        return FromSet<string>(KlingonShips, dontPick);
    }

    // Ship List
    // https://memory-alpha.fandom.com/wiki/Romulan_starships
    public static string[] RomulanShips =
    [
        "Aj'rmr",
        "Belak",
        "Decius",
        "Dividices",
        "Devoras",
        "Gasko",
        "Genorex",
        "Haakona",
        "Khazara",
        "Koderex",
        "Makar",
        "Narada",
        "Preceptor",
        "Pi",
        "Scimitar",
        "Shaenor",
        "T'Met",
        "T'Tpalok",
        "Talvath",
        "Terix",
        "Tomal",
        "Valdore"
    ];

    public static string RandRomulan(List<string> dontPick)
    {
        return FromSet<string>(RomulanShips, dontPick);
    }

    // https://memory-alpha.fandom.com/wiki/Category:Starbases
    public static string[] Starbases =
    [
        "Starbase 1",
        "Starbase 2",
        "Starbase 4",
        "Starbase 5",
        "Starbase 6",
        "Starbase 7",
        "Starbase 9",
        "Starbase 10",
        "Starbase 11",
        "Starbase 12",
        "Starbase 14",
        "Starbase 18",
        "Starbase 19",
        "Starbase 21",
        "Starbase 22",
        "Starbase 23",
        "Starbase 24",
        "Starbase 25",
        "Starbase 27",
        "Starbase 28",
        "Starbase 29",
        "Starbase 31",
        "Starbase 32",
        "Starbase 36",
        "Starbase 39-Sierra",
        "Starbase 40",
        "Starbase 41",
        "Starbase 45",
        "Starbase 46",
        "Starbase 47",
        "Starbase 48",
        "Starbase 53",
        "Starbase 55",
        "Starbase 56",
        "Starbase 58",
        "Starbase 62",
        "Starbase 63",
        "Starbase 67",
        "Starbase 73",
        "Starbase 74",
        "Starbase 77",
        "Starbase 78",
        "Starbase 80",
        "Starbase 82",
        "Starbase 83",
        "Starbase 84",
        "Starbase 86",
        "Starbase 87",
        "Starbase 88",
        "Starbase 97",
        "Starbase 103",
        "Starbase 105",
        "Starbase 112",
        "Starbase 117",
        "Starbase 118",
        "Starbase 121",
        "Starbase 123",
        "Starbase 129",
        "Starbase 133",
        "Starbase 134",
        "Starbase 137",
        "Starbase 152",
        "Starbase 153",
        "Starbase 157",
        "Starbase 172",
        "Starbase 173",
        "Starbase 174",
        "Starbase 179",
        "Starbase 185",
        "Starbase 200",
        "Starbase 201",
        "Starbase 211",
        "Starbase 212",
        "Starbase 214",
        "Starbase 218",
        "Starbase 219",
        "Starbase 220",
        "Starbase 227",
        "Starbase 231",
        "Starbase 234",
        "Starbase 235",
        "Starbase 237",
        "Starbase 245",
        "Starbase 247",
        "Starbase 257",
        "Starbase 260",
        "Starbase 295",
        "Starbase 301",
        "Starbase 310",
        "Starbase 313",
        "Starbase 324",
        "Starbase 328",
        "Starbase 336",
        "Starbase 343",
        "Starbase 371",
        "Starbase 375",
        "Starbase 384",
        "Starbase 401",
        "Starbase 410",
        "Starbase 414",
        "Starbase 416",
        "Starbase 434",
        "Starbase 440",
        "Starbase 495",
        "Starbase 514",
        "Starbase 515",
        "Starbase 621",
        "Starbase 718",
        "Starbase 0834",
        "Starbase 4077",
        "Starbase 4112",
        "Axanar Starbase Terminal",
        "Berengaria VII",
        "Cygnet XIV",
        "Deep Space 3",
        "Deep Space 4",
        "Deep Space 5",
        "Deep Space 7",
        "Deep Space 9",
        "Deep Space 11",
        "Deep Space 12",
        "Deep Space 2",
        "Deep Space 253",
        "Deep Space Station K-7",
        "Douglas Station",
        "Starbase Earhart",
        "Eminiar VII Starbase",
        "Farpoint Station",
        "Starbase G-6",
        "Lya III",
        "Lya Station Alpha",
        "McNair Starbase",
        "Starbase Meta",
        "Starbase Montgomery",
        "New Paris Colony Starbase",
        "Otar II",
        "Starbase Sierra Tango",
        "Starbase Trailer Twenty-Nine",
        "Telka V Starbase",
        "Xendi Starbase 9",
        "Yorktown",
        "Zayra IV",
        "Starbase Zetta"
    ];

    public static string RandStarbase(List<string> dontPick)
    {
        return FromSet<string>(Starbases, dontPick);
    }

    public static void StarTrekHeader()
    {
        Console.Write(
            @"  
                SSSSS   U   U   PPPPP   EEEEE   RRRRR
                S       U   U   P   P   E       R   R
                SSSSS   U   U   PPPPP   EEEE    RRRRR
                    S   U   U   P       E       R  R
                SSSSS   UUUUU   P       EEEEE   R   R


                 SSSSSSS  TTTTTTTT     A     RRRRRRR
                SSSSSSSS  TTTTTTTT    AAA    RRRRRRRR
               SS            TT       AAA    RR     RR
               SSSSSSS       TT      AA AA   RR     RR
                SSSSSSS      TT      AA AA   RRRRRRRR
                      SS     TT     AAAAAAA  RRRRRRR
                      SS     TT     AAAAAAA  RR   RR
               SSSSSSSS      TT    AA     AA RR    RR
               SSSSSSS       TT    AA     AA RR     RR
    
    
    
                TTTTTTTT RRRRRRR   EEEEEEEEE KK     KK
                TTTTTTTT RRRRRRRR  EEEEEEEEE KK    KK
                   TT    RR     RR EE        KK   KK
                   TT    RR     RR EEEEEE    KKKKKK
                   TT    RRRRRRRR  EEEEEE    KKKKK
                   TT    RRRRRRR   EE        KK  KK
                   TT    RR   RR   EE        KK   KK
                   TT    RR    RR  EEEEEEEEE KK    KK
                   TT    RR     RR EEEEEEEEE KK     KK
        "
        );

        Console.WriteLine();
    }
};
