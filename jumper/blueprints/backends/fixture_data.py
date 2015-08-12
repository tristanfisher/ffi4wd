test_cities = [
    {
        "description": "new york, ny, usa",
        "lat": "40.734838",
        "long": "-73.990810"
    },
    {
        "description": "portland, me, usa",
        "lat": "43.657727",
        "long": "-70.254636"
    },
    {
        "description": "seattle, wa, usa",
        "lat": "47.620410",
        "long": "-122.349368"
    },
    {
        "description": "san fransciso, ca, usa",
        "lat": "37.759936",
        "long": "-122.415058"
    },
    {
        "description": "denver, co, usa",
        "lat": "39.738150",
        "long": "-104.989576"
    },
    {
        "description": "austin, tx, usa",
        "lat": "30.265857",
        "long": "-97.741833"
    },
    {
        "description": "montreal, qc, ca",
        "lat": "45.500507",
        "long": "-73.563048"
    },
    {
        "description": "vancouver, bc, ca",
        "lat": "49.238556",
        "long": "-123.084775"
    },
    {
        "description": "anchorage, ak, usa",
        "lat": "61.211629",
        "long": "-149.895041"
    },
    {
        "description": "toronto, on, ca",
        "lat": "43.646736",
        "long": "-79.384238"
    },
    {
        "description": "berlin, germany",
        "lat": "52.522564",
        "long": "13.400369"
    },
    {
        "description": "frankfurt, germany",
        "lat": "50.110556",
        "long": "8.681455"
    },
    {
        "description": "hamburg, germany",
        "lat": "53.548640",
        "long": "9.993521"
    },
    {
        "description": "cologne, germany",
        "lat": "50.934693",
        "long": "6.958435"
    },
    {
        "description": "dublin, ireland",
        "lat": "53.348878",
        "long": "-6.257015"
    },
    {
        "description": "tokyo, japan",
        "lat": "35.703184",
        "long": "139.734830"
    },
    {
        "description": "seoul, korea",
        "lat": "37.548857",
        "long": "126.997675"
    },
    {
        "description": "moscow, russia",
        "lat": "55.761384",
        "long": "37.662707"
    },
    {
        "description": "st petersburg, russia",
        "lat": "59.915844",
        "long": "30.326210"
    },
    {
        "description": "kyiv, ukraine",
        "lat": "50.440534",
        "long": "30.538184"
    },
    {
        "description": "copenhagen, denmark",
        "lat": "55.668907",
        "long": "12.557736"
    },
    {
        "description": "amsterdam, netherlands",
        "lat": "52.360880",
        "long": "4.897241"
    },
    {
        "description": "london, uk",
        "lat": "51.518832",
        "long": "-0.128251"
    },
    {
        "description": "bristol, uk",
        "lat": "51.457366",
        "long": "-2.580410"
    },
    {
        "description": "manchester, uk",
        "lat": "53.481236",
        "long": "-2.242475"
    },
    {
        "description": "nantes, france",
        "lat": "47.212808",
        "long": "-1.556502"
    },
    {
        "description": "paris, france",
        "lat": "48.856634",
        "long": "2.353776"
    },
    {
        "description": "helsinki, finland",
        "lat": "60.172662",
        "long": "24.942226"
    },
    {
        "description": "stockholm, sweden",
        "lat": "59.328944",
        "long": "18.070630"
    },
    {
        "description": "oslo, norway",
        "lat": "59.913826",
        "long": "10.751471"
    }
]

test_cities_eleven = [
    {
        "description": "new york, ny, usa",
        "lat": "40.734838",
        "long": "-73.990810"
    },
    {
        "description": "portland, me, usa",
        "lat": "43.657727",
        "long": "-70.254636"
    },
    {
        "description": "seattle, wa, usa",
        "lat": "47.620410",
        "long": "-122.349368"
    },
    {
        "description": "san fransciso, ca, usa",
        "lat": "37.759936",
        "long": "-122.415058"
    },
    {
        "description": "denver, co, usa",
        "lat": "39.738150",
        "long": "-104.989576"
    },
    {
        "description": "austin, tx, usa",
        "lat": "30.265857",
        "long": "-97.741833"
    },
    {
        "description": "montreal, qc, ca",
        "lat": "45.500507",
        "long": "-73.563048"
    },
    {
        "description": "vancouver, bc, ca",
        "lat": "49.238556",
        "long": "-123.084775"
    },
    {
        "description": "anchorage, ak, usa",
        "lat": "61.211629",
        "long": "-149.895041"
    },
    {
        "description": "toronto, on, ca",
        "lat": "43.646736",
        "long": "-79.384238"
    },
    {
        "description": "berlin, germany",
        "lat": "52.522564",
        "long": "13.400369"
    }
]

test_cities_eleven_tuples = [('new york, ny, usa', (40.734838, -73.99081)), ('portland, me, usa', (43.657727, -70.254636)), ('seattle, wa, usa', (47.62041, -122.349368)), ('san fransciso, ca, usa', (37.759936, -122.415058)), ('denver, co, usa', (39.73815, -104.989576)), ('austin, tx, usa', (30.265857, -97.741833)), ('montreal, qc, ca', (45.500507, -73.563048)), ('vancouver, bc, ca', (49.238556, -123.084775)), ('anchorage, ak, usa', (61.211629, -149.895041)), ('toronto, on, ca', (43.646736, -79.384238)), ('berlin, germany', (52.522564, 13.400369))]
test_cities_tuples = [('new york, ny, usa', ['40.734838', '-73.990810']), ('portland, me, usa', ['43.657727', '-70.254636']), ('seattle, wa, usa', ['47.620410', '-122.349368']), ('san fransciso, ca, usa', ['37.759936', '-122.415058']), ('denver, co, usa', ['39.738150', '-104.989576']), ('austin, tx, usa', ['30.265857', '-97.741833']), ('montreal, qc, ca', ['45.500507', '-73.563048']), ('vancouver, bc, ca', ['49.238556', '-123.084775']), ('anchorage, ak, usa', ['61.211629', '-149.895041']), ('toronto, on, ca', ['43.646736', '-79.384238']), ('berlin, germany', ['52.522564', '13.400369']), ('frankfurt, germany', ['50.110556', '8.681455']), ('hamburg, germany', ['53.548640', '9.993521']), ('cologne, germany', ['50.934693', '6.958435']), ('dublin, ireland', ['53.348878', '-6.257015']), ('tokyo, japan', ['35.703184', '139.734830']), ('seoul, korea', ['37.548857', '126.997675']), ('moscow, russia', ['55.761384', '37.662707']), ('st petersburg, russia', ['59.915844', '30.326210']), ('kyiv, ukraine', ['50.440534', '30.538184']), ('copenhagen, denmark', ['55.668907', '12.557736']), ('amsterdam, netherlands', ['52.360880', '4.897241']), ('london, uk', ['51.518832', '-0.128251']), ('bristol, uk', ['51.457366', '-2.580410']), ('manchester, uk', ['53.481236', '-2.242475']), ('nantes, france', ['47.212808', '-1.556502']), ('paris, france', ['48.856634', '2.353776']), ('helsinki, finland', ['60.172662', '24.942226']), ('stockholm, sweden', ['59.328944', '18.070630']), ('oslo, norway', ['59.913826', '10.751471'])]
test_cities_weight_15 = {'portland, me, usa': [('new york, ny, usa', 447.6466430279615), ('seattle, wa, usa', 3998.364023733441), ('san fransciso, ca, usa', 4373.47227136685), ('denver, co, usa', 2895.861939844122), ('austin, tx, usa', 2840.9300348922857), ('montreal, qc, ca', 332.68393556733724), ('vancouver, bc, ca', 4012.0439582695217), ('anchorage, ak, usa', 5351.314013574186), ('toronto, on, ca', 734.3534731575957), ('berlin, germany', 5937.266858217603), ('frankfurt, germany', 5758.907654843056), ('hamburg, germany', 5682.561366723863), ('cologne, germany', 5609.995951156987), ('dublin, ireland', 4671.044334218768)], 'frankfurt, germany': [('new york, ny, usa', 6201.852040536504), ('portland, me, usa', 5758.907654843056), ('seattle, wa, usa', 8181.7466480361), ('san fransciso, ca, usa', 9137.255927375238), ('denver, co, usa', 8118.555563804856), ('austin, tx, usa', 8530.618772237909), ('montreal, qc, ca', 5846.07933033826), ('vancouver, bc, ca', 8053.506529112649), ('anchorage, ak, usa', 7492.129948043919), ('toronto, on, ca', 6335.256241201341), ('berlin, germany', 423.6316360409979), ('hamburg, germany', 392.87849479935215), ('cologne, germany', 152.46723305665677), ('dublin, ireland', 1087.8776732761144)], 'montreal, qc, ca': [('new york, ny, usa', 531.2020828945784), ('portland, me, usa', 332.68393556733724), ('seattle, wa, usa', 3676.5204899041464), ('san fransciso, ca, usa', 4086.2057553148447), ('denver, co, usa', 2632.54876647224), ('austin, tx, usa', 2697.4254785041767), ('vancouver, bc, ca', 3686.260543142142), ('anchorage, ak, usa', 5025.402295871271), ('toronto, on, ca', 505.05332964971956), ('berlin, germany', 5999.59094399283), ('frankfurt, germany', 5846.07933033826), ('hamburg, germany', 5744.95620629242), ('cologne, germany', 5695.368791681914), ('dublin, ireland', 4761.172873284123)], 'cologne, germany': [('new york, ny, usa', 6053.3583286022), ('portland, me, usa', 5609.995951156987), ('seattle, wa, usa', 8038.878710196924), ('san fransciso, ca, usa', 8990.289091553695), ('denver, co, usa', 7966.660997681989), ('austin, tx, usa', 8378.98371782052), ('montreal, qc, ca', 5695.368791681914), ('vancouver, bc, ca', 7911.885681703947), ('anchorage, ak, usa', 7378.093972006955), ('toronto, on, ca', 6184.024494367389), ('berlin, germany', 477.43909710717696), ('frankfurt, germany', 152.46723305665677), ('hamburg, germany', 356.6633710260719), ('dublin, ireland', 939.6336729145872)], 'anchorage, ak, usa': [('new york, ny, usa', 5410.1446563811905), ('portland, me, usa', 5351.314013574186), ('seattle, wa, usa', 2306.7618804760577), ('san fransciso, ca, usa', 3227.9327095873814), ('denver, co, usa', 3854.9535418964065), ('austin, tx, usa', 5096.370282889052), ('montreal, qc, ca', 5025.402295871271), ('vancouver, bc, ca', 2134.1966806947084), ('toronto, on, ca', 4877.203369569424), ('berlin, germany', 7284.160939006664), ('frankfurt, germany', 7492.129948043919), ('hamburg, germany', 7133.384628965154), ('cologne, germany', 7378.093972006955), ('dublin, ireland', 6880.455547319905)], 'san fransciso, ca, usa': [('new york, ny, usa', 4131.2260736717235), ('portland, me, usa', 4373.47227136685), ('seattle, wa, usa', 1096.7574923438176), ('denver, co, usa', 1525.0127604501427), ('austin, tx, usa', 2413.848547208374), ('montreal, qc, ca', 4086.2057553148447), ('vancouver, bc, ca', 1277.8536425787968), ('anchorage, ak, usa', 3227.9327095873814), ('toronto, on, ca', 3645.110544523325), ('berlin, germany', 9108.707449785496), ('frankfurt, germany', 9137.255927375238), ('hamburg, germany', 8884.368688361468), ('cologne, germany', 8990.289091553695), ('dublin, ireland', 8180.339239597275)], 'seattle, wa, usa': [('new york, ny, usa', 3867.6996796026383), ('portland, me, usa', 3998.364023733441), ('san fransciso, ca, usa', 1096.7574923438176), ('denver, co, usa', 1643.1750113542994), ('austin, tx, usa', 2850.7367348453713), ('montreal, qc, ca', 3676.5204899041464), ('vancouver, bc, ca', 187.98357684266733), ('anchorage, ak, usa', 2306.7618804760577), ('toronto, on, ca', 3327.3059742840283), ('berlin, germany', 8118.959756087951), ('frankfurt, germany', 8181.7466480361), ('hamburg, germany', 7904.721664019446), ('cologne, germany', 8038.878710196924), ('dublin, ireland', 7278.426972799073)], 'vancouver, bc, ca': [('new york, ny, usa', 3903.113264915231), ('portland, me, usa', 4012.0439582695217), ('seattle, wa, usa', 187.98357684266733), ('san fransciso, ca, usa', 1277.8536425787968), ('denver, co, usa', 1775.1965629670804), ('austin, tx, usa', 2997.5356232275794), ('montreal, qc, ca', 3686.260543142142), ('anchorage, ak, usa', 2134.1966806947084), ('toronto, on, ca', 3358.0392491366733), ('berlin, germany', 7981.580607175459), ('frankfurt, germany', 8053.506529112649), ('hamburg, germany', 7770.358385120253), ('cologne, germany', 7911.885681703947), ('dublin, ireland', 7165.131299170149)], 'new york, ny, usa': [('portland, me, usa', 447.6466430279615), ('seattle, wa, usa', 3867.6996796026383), ('san fransciso, ca, usa', 4131.2260736717235), ('denver, co, usa', 2620.6948689079463), ('austin, tx, usa', 2434.3591976539533), ('montreal, qc, ca', 531.2020828945784), ('vancouver, bc, ca', 3903.113264915231), ('anchorage, ak, usa', 5410.1446563811905), ('toronto, on, ca', 549.7598018862785), ('berlin, germany', 6383.77962681138), ('frankfurt, germany', 6201.852040536504), ('hamburg, germany', 6129.122382053943), ('cologne, germany', 6053.3583286022), ('dublin, ireland', 5114.01265148199)], 'dublin, ireland': [('new york, ny, usa', 5114.01265148199), ('portland, me, usa', 4671.044334218768), ('seattle, wa, usa', 7278.426972799073), ('san fransciso, ca, usa', 8180.339239597275), ('denver, co, usa', 7084.24910627883), ('austin, tx, usa', 7450.285692633587), ('montreal, qc, ca', 4761.172873284123), ('vancouver, bc, ca', 7165.131299170149), ('anchorage, ak, usa', 6880.455547319905), ('toronto, on, ca', 5252.688701589071), ('berlin, germany', 1316.7887794012324), ('frankfurt, germany', 1087.8776732761144), ('hamburg, germany', 1074.326634025533), ('cologne, germany', 939.6336729145872)], 'hamburg, germany': [('new york, ny, usa', 6129.122382053943), ('portland, me, usa', 5682.561366723863), ('seattle, wa, usa', 7904.721664019446), ('san fransciso, ca, usa', 8884.368688361468), ('denver, co, usa', 7926.157053263219), ('austin, tx, usa', 8406.075329700989), ('montreal, qc, ca', 5744.95620629242), ('vancouver, bc, ca', 7770.358385120253), ('anchorage, ak, usa', 7133.384628965154), ('toronto, on, ca', 6223.643112265524), ('berlin, germany', 254.80553039175498), ('frankfurt, germany', 392.87849479935215), ('cologne, germany', 356.6633710260719), ('dublin, ireland', 1074.326634025533)], 'toronto, on, ca': [('new york, ny, usa', 549.7598018862785), ('portland, me, usa', 734.3534731575957), ('seattle, wa, usa', 3327.3059742840283), ('san fransciso, ca, usa', 3645.110544523325), ('denver, co, usa', 2161.5284654374723), ('austin, tx, usa', 2199.140387071369), ('montreal, qc, ca', 505.05332964971956), ('vancouver, bc, ca', 3358.0392491366733), ('anchorage, ak, usa', 4877.203369569424), ('berlin, germany', 6477.866190491199), ('frankfurt, germany', 6335.256241201341), ('hamburg, germany', 6223.643112265524), ('cologne, germany', 6184.024494367389), ('dublin, ireland', 5252.688701589071)], 'denver, co, usa': [('new york, ny, usa', 2620.6948689079463), ('portland, me, usa', 2895.861939844122), ('seattle, wa, usa', 1643.1750113542994), ('san fransciso, ca, usa', 1525.0127604501427), ('austin, tx, usa', 1242.3361492683046), ('montreal, qc, ca', 2632.54876647224), ('vancouver, bc, ca', 1775.1965629670804), ('anchorage, ak, usa', 3854.9535418964065), ('toronto, on, ca', 2161.5284654374723), ('berlin, germany', 8169.4908092679), ('frankfurt, germany', 8118.555563804856), ('hamburg, germany', 7926.157053263219), ('cologne, germany', 7966.660997681989), ('dublin, ireland', 7084.24910627883)], 'austin, tx, usa': [('new york, ny, usa', 2434.3591976539533), ('portland, me, usa', 2840.9300348922857), ('seattle, wa, usa', 2850.7367348453713), ('san fransciso, ca, usa', 2413.848547208374), ('denver, co, usa', 1242.3361492683046), ('montreal, qc, ca', 2697.4254785041767), ('vancouver, bc, ca', 2997.5356232275794), ('anchorage, ak, usa', 5096.370282889052), ('toronto, on, ca', 2199.140387071369), ('berlin, germany', 8659.20097853115), ('frankfurt, germany', 8530.618772237909), ('hamburg, germany', 8406.075329700989), ('cologne, germany', 8378.98371782052), ('dublin, ireland', 7450.285692633587)], 'berlin, germany': [('new york, ny, usa', 6383.77962681138), ('portland, me, usa', 5937.266858217603), ('seattle, wa, usa', 8118.959756087951), ('san fransciso, ca, usa', 9108.707449785496), ('denver, co, usa', 8169.4908092679), ('austin, tx, usa', 8659.20097853115), ('montreal, qc, ca', 5999.59094399283), ('vancouver, bc, ca', 7981.580607175459), ('anchorage, ak, usa', 7284.160939006664), ('toronto, on, ca', 6477.866190491199), ('frankfurt, germany', 423.6316360409979), ('hamburg, germany', 254.80553039175498), ('cologne, germany', 477.43909710717696), ('dublin, ireland', 1316.7887794012324)]}
test_cities_weight_12 = {'new york, ny, usa': [('portland, me, usa', 447.6466430279615), ('seattle, wa, usa', 3867.6996796026383), ('san fransciso, ca, usa', 4131.2260736717235), ('denver, co, usa', 2620.6948689079463), ('austin, tx, usa', 2434.3591976539533), ('montreal, qc, ca', 531.2020828945784), ('vancouver, bc, ca', 3903.113264915231), ('anchorage, ak, usa', 5410.1446563811905), ('toronto, on, ca', 549.7598018862785), ('berlin, germany', 6383.77962681138), ('frankfurt, germany', 6201.852040536504)], 'anchorage, ak, usa': [('new york, ny, usa', 5410.1446563811905), ('portland, me, usa', 5351.314013574186), ('seattle, wa, usa', 2306.7618804760577), ('san fransciso, ca, usa', 3227.9327095873814), ('denver, co, usa', 3854.9535418964065), ('austin, tx, usa', 5096.370282889052), ('montreal, qc, ca', 5025.402295871271), ('vancouver, bc, ca', 2134.1966806947084), ('toronto, on, ca', 4877.203369569424), ('berlin, germany', 7284.160939006664), ('frankfurt, germany', 7492.129948043919)], 'toronto, on, ca': [('new york, ny, usa', 549.7598018862785), ('portland, me, usa', 734.3534731575957), ('seattle, wa, usa', 3327.3059742840283), ('san fransciso, ca, usa', 3645.110544523325), ('denver, co, usa', 2161.5284654374723), ('austin, tx, usa', 2199.140387071369), ('montreal, qc, ca', 505.05332964971956), ('vancouver, bc, ca', 3358.0392491366733), ('anchorage, ak, usa', 4877.203369569424), ('berlin, germany', 6477.866190491199), ('frankfurt, germany', 6335.256241201341)], 'berlin, germany': [('new york, ny, usa', 6383.77962681138), ('portland, me, usa', 5937.266858217603), ('seattle, wa, usa', 8118.959756087951), ('san fransciso, ca, usa', 9108.707449785496), ('denver, co, usa', 8169.4908092679), ('austin, tx, usa', 8659.20097853115), ('montreal, qc, ca', 5999.59094399283), ('vancouver, bc, ca', 7981.580607175459), ('anchorage, ak, usa', 7284.160939006664), ('toronto, on, ca', 6477.866190491199), ('frankfurt, germany', 423.6316360409979)], 'seattle, wa, usa': [('new york, ny, usa', 3867.6996796026383), ('portland, me, usa', 3998.364023733441), ('san fransciso, ca, usa', 1096.7574923438176), ('denver, co, usa', 1643.1750113542994), ('austin, tx, usa', 2850.7367348453713), ('montreal, qc, ca', 3676.5204899041464), ('vancouver, bc, ca', 187.98357684266733), ('anchorage, ak, usa', 2306.7618804760577), ('toronto, on, ca', 3327.3059742840283), ('berlin, germany', 8118.959756087951), ('frankfurt, germany', 8181.7466480361)], 'austin, tx, usa': [('new york, ny, usa', 2434.3591976539533), ('portland, me, usa', 2840.9300348922857), ('seattle, wa, usa', 2850.7367348453713), ('san fransciso, ca, usa', 2413.848547208374), ('denver, co, usa', 1242.3361492683046), ('montreal, qc, ca', 2697.4254785041767), ('vancouver, bc, ca', 2997.5356232275794), ('anchorage, ak, usa', 5096.370282889052), ('toronto, on, ca', 2199.140387071369), ('berlin, germany', 8659.20097853115), ('frankfurt, germany', 8530.618772237909)], 'vancouver, bc, ca': [('new york, ny, usa', 3903.113264915231), ('portland, me, usa', 4012.0439582695217), ('seattle, wa, usa', 187.98357684266733), ('san fransciso, ca, usa', 1277.8536425787968), ('denver, co, usa', 1775.1965629670804), ('austin, tx, usa', 2997.5356232275794), ('montreal, qc, ca', 3686.260543142142), ('anchorage, ak, usa', 2134.1966806947084), ('toronto, on, ca', 3358.0392491366733), ('berlin, germany', 7981.580607175459), ('frankfurt, germany', 8053.506529112649)], 'san fransciso, ca, usa': [('new york, ny, usa', 4131.2260736717235), ('portland, me, usa', 4373.47227136685), ('seattle, wa, usa', 1096.7574923438176), ('denver, co, usa', 1525.0127604501427), ('austin, tx, usa', 2413.848547208374), ('montreal, qc, ca', 4086.2057553148447), ('vancouver, bc, ca', 1277.8536425787968), ('anchorage, ak, usa', 3227.9327095873814), ('toronto, on, ca', 3645.110544523325), ('berlin, germany', 9108.707449785496), ('frankfurt, germany', 9137.255927375238)], 'frankfurt, germany': [('new york, ny, usa', 6201.852040536504), ('portland, me, usa', 5758.907654843056), ('seattle, wa, usa', 8181.7466480361), ('san fransciso, ca, usa', 9137.255927375238), ('denver, co, usa', 8118.555563804856), ('austin, tx, usa', 8530.618772237909), ('montreal, qc, ca', 5846.07933033826), ('vancouver, bc, ca', 8053.506529112649), ('anchorage, ak, usa', 7492.129948043919), ('toronto, on, ca', 6335.256241201341), ('berlin, germany', 423.6316360409979)], 'denver, co, usa': [('new york, ny, usa', 2620.6948689079463), ('portland, me, usa', 2895.861939844122), ('seattle, wa, usa', 1643.1750113542994), ('san fransciso, ca, usa', 1525.0127604501427), ('austin, tx, usa', 1242.3361492683046), ('montreal, qc, ca', 2632.54876647224), ('vancouver, bc, ca', 1775.1965629670804), ('anchorage, ak, usa', 3854.9535418964065), ('toronto, on, ca', 2161.5284654374723), ('berlin, germany', 8169.4908092679), ('frankfurt, germany', 8118.555563804856)], 'portland, me, usa': [('new york, ny, usa', 447.6466430279615), ('seattle, wa, usa', 3998.364023733441), ('san fransciso, ca, usa', 4373.47227136685), ('denver, co, usa', 2895.861939844122), ('austin, tx, usa', 2840.9300348922857), ('montreal, qc, ca', 332.68393556733724), ('vancouver, bc, ca', 4012.0439582695217), ('anchorage, ak, usa', 5351.314013574186), ('toronto, on, ca', 734.3534731575957), ('berlin, germany', 5937.266858217603), ('frankfurt, germany', 5758.907654843056)], 'montreal, qc, ca': [('new york, ny, usa', 531.2020828945784), ('portland, me, usa', 332.68393556733724), ('seattle, wa, usa', 3676.5204899041464), ('san fransciso, ca, usa', 4086.2057553148447), ('denver, co, usa', 2632.54876647224), ('austin, tx, usa', 2697.4254785041767), ('vancouver, bc, ca', 3686.260543142142), ('anchorage, ak, usa', 5025.402295871271), ('toronto, on, ca', 505.05332964971956), ('berlin, germany', 5999.59094399283), ('frankfurt, germany', 5846.07933033826)]}
test_cities_weight_10 = {'new york, ny, usa': [('portland, me, usa', 447.6466430279615), ('seattle, wa, usa', 3867.6996796026383), ('san fransciso, ca, usa', 4131.2260736717235), ('denver, co, usa', 2620.6948689079463), ('austin, tx, usa', 2434.3591976539533), ('montreal, qc, ca', 531.2020828945784), ('vancouver, bc, ca', 3903.113264915231), ('anchorage, ak, usa', 5410.1446563811905), ('toronto, on, ca', 549.7598018862785)], 'vancouver, bc, ca': [('new york, ny, usa', 3903.113264915231), ('portland, me, usa', 4012.0439582695217), ('seattle, wa, usa', 187.98357684266733), ('san fransciso, ca, usa', 1277.8536425787968), ('denver, co, usa', 1775.1965629670804), ('austin, tx, usa', 2997.5356232275794), ('montreal, qc, ca', 3686.260543142142), ('anchorage, ak, usa', 2134.1966806947084), ('toronto, on, ca', 3358.0392491366733)], 'anchorage, ak, usa': [('new york, ny, usa', 5410.1446563811905), ('portland, me, usa', 5351.314013574186), ('seattle, wa, usa', 2306.7618804760577), ('san fransciso, ca, usa', 3227.9327095873814), ('denver, co, usa', 3854.9535418964065), ('austin, tx, usa', 5096.370282889052), ('montreal, qc, ca', 5025.402295871271), ('vancouver, bc, ca', 2134.1966806947084), ('toronto, on, ca', 4877.203369569424)], 'montreal, qc, ca': [('new york, ny, usa', 531.2020828945784), ('portland, me, usa', 332.68393556733724), ('seattle, wa, usa', 3676.5204899041464), ('san fransciso, ca, usa', 4086.2057553148447), ('denver, co, usa', 2632.54876647224), ('austin, tx, usa', 2697.4254785041767), ('vancouver, bc, ca', 3686.260543142142), ('anchorage, ak, usa', 5025.402295871271), ('toronto, on, ca', 505.05332964971956)], 'toronto, on, ca': [('new york, ny, usa', 549.7598018862785), ('portland, me, usa', 734.3534731575957), ('seattle, wa, usa', 3327.3059742840283), ('san fransciso, ca, usa', 3645.110544523325), ('denver, co, usa', 2161.5284654374723), ('austin, tx, usa', 2199.140387071369), ('montreal, qc, ca', 505.05332964971956), ('vancouver, bc, ca', 3358.0392491366733), ('anchorage, ak, usa', 4877.203369569424)], 'seattle, wa, usa': [('new york, ny, usa', 3867.6996796026383), ('portland, me, usa', 3998.364023733441), ('san fransciso, ca, usa', 1096.7574923438176), ('denver, co, usa', 1643.1750113542994), ('austin, tx, usa', 2850.7367348453713), ('montreal, qc, ca', 3676.5204899041464), ('vancouver, bc, ca', 187.98357684266733), ('anchorage, ak, usa', 2306.7618804760577), ('toronto, on, ca', 3327.3059742840283)], 'san fransciso, ca, usa': [('new york, ny, usa', 4131.2260736717235), ('portland, me, usa', 4373.47227136685), ('seattle, wa, usa', 1096.7574923438176), ('denver, co, usa', 1525.0127604501427), ('austin, tx, usa', 2413.848547208374), ('montreal, qc, ca', 4086.2057553148447), ('vancouver, bc, ca', 1277.8536425787968), ('anchorage, ak, usa', 3227.9327095873814), ('toronto, on, ca', 3645.110544523325)], 'portland, me, usa': [('new york, ny, usa', 447.6466430279615), ('seattle, wa, usa', 3998.364023733441), ('san fransciso, ca, usa', 4373.47227136685), ('denver, co, usa', 2895.861939844122), ('austin, tx, usa', 2840.9300348922857), ('montreal, qc, ca', 332.68393556733724), ('vancouver, bc, ca', 4012.0439582695217), ('anchorage, ak, usa', 5351.314013574186), ('toronto, on, ca', 734.3534731575957)], 'austin, tx, usa': [('new york, ny, usa', 2434.3591976539533), ('portland, me, usa', 2840.9300348922857), ('seattle, wa, usa', 2850.7367348453713), ('san fransciso, ca, usa', 2413.848547208374), ('denver, co, usa', 1242.3361492683046), ('montreal, qc, ca', 2697.4254785041767), ('vancouver, bc, ca', 2997.5356232275794), ('anchorage, ak, usa', 5096.370282889052), ('toronto, on, ca', 2199.140387071369)], 'denver, co, usa': [('new york, ny, usa', 2620.6948689079463), ('portland, me, usa', 2895.861939844122), ('seattle, wa, usa', 1643.1750113542994), ('san fransciso, ca, usa', 1525.0127604501427), ('austin, tx, usa', 1242.3361492683046), ('montreal, qc, ca', 2632.54876647224), ('vancouver, bc, ca', 1775.1965629670804), ('anchorage, ak, usa', 3854.9535418964065), ('toronto, on, ca', 2161.5284654374723)]}
test_cities_weight_5 = {'new york, ny, usa': [('portland, me, usa', 447.6466430279615), ('seattle, wa, usa', 3867.6996796026383), ('san fransciso, ca, usa', 4131.2260736717235), ('denver, co, usa', 2620.6948689079463)], 'seattle, wa, usa': [('new york, ny, usa', 3867.6996796026383), ('portland, me, usa', 3998.364023733441), ('san fransciso, ca, usa', 1096.7574923438176), ('denver, co, usa', 1643.1750113542994)], 'denver, co, usa': [('new york, ny, usa', 2620.6948689079463), ('portland, me, usa', 2895.861939844122), ('seattle, wa, usa', 1643.1750113542994), ('san fransciso, ca, usa', 1525.0127604501427)], 'portland, me, usa': [('new york, ny, usa', 447.6466430279615), ('seattle, wa, usa', 3998.364023733441), ('san fransciso, ca, usa', 4373.47227136685), ('denver, co, usa', 2895.861939844122)], 'san fransciso, ca, usa': [('new york, ny, usa', 4131.2260736717235), ('portland, me, usa', 4373.47227136685), ('seattle, wa, usa', 1096.7574923438176), ('denver, co, usa', 1525.0127604501427)]}


def desc_lat_long_to_semicolon_format(data_dict=test_cities_eleven):
    """
    Checkboxes require a format that looks like:
        [('lat;long', 'description'),]
    """

    new_structure = []

    for location in data_dict:
        try:
            _latlong = "%s;%s" % (location["lat"], location["long"])
            new_structure.append((_latlong, location["description"]))
        except KeyError:
            new_structure.append(("0;0", "Error processing location"))

    return new_structure
