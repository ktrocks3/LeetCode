from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        A = defaultdict(int)
        I = defaultdict(int)
        adj = defaultdict(list)
        for u, v in pairs:
            A[u] += 1
            I[v] += 1
            adj[u].append(v)

        curr_v = next((node for node in A if A[node] - I[node] == 1), pairs[0][0])

        if len(pairs) == 0:
            return []

        curr_path = []
        circuit = []

        curr_path.append(curr_v)

        while len(curr_path):
            if A[curr_v]:
                curr_path.append(curr_v)

                next_v = adj[curr_v][-1]
                A[curr_v] -= 1
                adj[curr_v].pop()

                curr_v = next_v
            else:
                circuit.append(curr_v)
                curr_v = curr_path[-1]
                curr_path.pop()

        path = []
        for i in range(len(circuit)-1, 0, -1):
            path.append([circuit[i], circuit[i-1]])
        return path


assert Solution().validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]) == [[11, 9], [9, 4], [4, 5], [5, 1]], \
    f'Expected: [[11,9],[9,4],[4,5],[5,1]], Received: {Solution().validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]])}'
assert Solution().validArrangement([[1, 3], [3, 2], [2, 1]]) == [[1,3],[3,2],[2,1]], \
  f'Expected: [[1,3],[3,2],[2,1]], Received: {Solution().validArrangement([[1, 3], [3, 2], [2, 1]])}'
assert Solution().validArrangement([[1, 2], [1, 3], [2, 1]]) == [[1,2],[2,1],[1,3]], \
  f'Expected: [[1,2],[2,1],[1,3]], Received: {Solution().validArrangement([[1, 2], [1, 3], [2, 1]])}'
Solution().validArrangement([[5,1],[4,5],[11,9],[9,4]])
Solution().validArrangement([[1,3],[3,2],[2,1]])
Solution().validArrangement([[1,2],[1,3],[2,1]])
Solution().validArrangement([[299,1],[1,2],[1,3],[2,1],[3,1]])
Solution().validArrangement([[1,3],[3,9],[9,4],[4,1],[1,4],[4,6],[6,3],[3,1],[1,456]])
Solution().validArrangement([[299,1],[1,2],[1,3],[3,5],[5,8],[8,3],[3,7],[7,6],[6,9],[9,3],[3,6],[6,7],[7,3],[3,8],[8,5],[5,3],[3,1],[2,1]])
Solution().validArrangement([[4088,3069],[5851,7177],[6961,3480],[7644,9172],[6963,4234],[5239,6117],[7177,2598],[5854,3387],[5150,2621],[1266,6093],[9476,9587],[4394,5078],[3401,5397],[356,1701],[439,1893],[7934,1785],[5854,8294],[2793,771],[5473,6633],[343,7361],[3459,3097],[9611,6116],[5989,956],[8577,247],[484,9065],[4955,8869],[4394,1034],[6294,6734],[1939,4751],[836,727],[7231,3741],[5398,6020],[3365,9699],[7363,898],[2671,140],[4088,9419],[6640,6215],[7764,6552],[5928,1030],[7026,4882],[1175,1034],[882,7698],[6618,6961],[8796,5776],[615,3180],[447,1088],[7326,6360],[1703,9632],[6555,849],[5541,7189],[3937,2524],[5225,1222],[53,9479],[3604,412],[9705,686],[5764,8872],[7450,8910],[782,9476],[349,777],[865,4410],[5398,3805],[1426,9978],[6511,1216],[216,8758],[4077,7450],[2524,3016],[7196,5027],[299,771],[9370,1915],[1336,4474],[9318,9981],[9941,8332],[7583,1145],[3196,9152],[9911,1939],[856,6655],[6999,8931],[5392,9419],[3876,9530],[1777,9014],[3097,5099],[5342,9933],[714,535],[1915,2118],[4923,3926],[8591,5614],[5333,1955],[686,1185],[4966,6168],[356,9251],[495,2693],[6963,8400],[2207,3926],[8846,5019],[3367,8284],[6294,4236],[9065,6967],[6734,9638],[2899,8126],[2621,9370],[7295,412],[9705,7454],[8872,1178],[3069,1660],[3310,495],[8319,7843],[8094,3817],[4894,7439],[898,2793],[1931,5764],[7346,6963],[3157,190],[439,9656],[4339,1426],[3741,4600],[1145,4410],[4474,3113],[423,8264],[962,9847],[7239,8737],[6500,8737],[8273,14],[9064,2601],[418,9135],[3991,4556],[8972,291],[1811,5861],[956,439],[1880,7231],[3978,8245],[967,5377],[5234,7454],[5746,3374],[299,6545],[2357,2793],[3926,3937],[6294,9481],[8065,759],[7429,3069],[5225,1132],[7729,3024],[6135,7231],[6093,898],[9898,3991],[3083,3156],[967,6734],[1703,459],[1660,9118],[959,5150],[16,3459],[3623,7738],[6858,8957],[8931,6488],[1373,8910],[617,4767],[7964,7657],[14,7196],[3614,5723],[6135,3651],[1034,3480],[1924,2943],[2943,8143],[8284,6737],[3480,7964],[4222,4709],[9971,6004],[1909,5989],[8760,865],[7231,9318],[6961,3651],[6056,4335],[8322,9898],[3156,299],[2601,9705],[8885,7239],[356,882],[6633,7239],[6306,1426],[771,5392],[617,9370],[3140,8303],[3658,836],[9476,1058],[6157,9362],[5966,9699],[5823,5776],[5098,8211],[3156,777],[8906,6301],[9172,1880],[459,657],[3387,8760],[1701,2378],[299,5239],[617,959],[3514,9587],[7346,771],[9118,2630],[1785,8273],[8910,495],[8818,5844],[8546,3281],[9481,1662],[7200,7738],[9118,6294],[9419,3604],[4846,1146],[5423,352],[9964,4414],[3281,9320],[4004,7029],[3792,439],[2871,4937],[3817,956],[6961,5528],[8427,299],[7454,1811],[5011,8796],[8972,1373],[7361,5691],[9481,4923],[337,2038],[4767,771],[7698,6961],[9172,7029],[5113,7207],[5966,2541],[782,6093],[4421,1323],[9953,1376],[1222,7157],[6004,4394],[6959,1604],[759,9638],[1336,5011],[3514,2529],[4321,8625],[7394,3623],[1698,8577],[8957,8885],[6623,3083],[5897,1708],[8758,7363],[2738,7346],[8294,771],[6020,4782],[1577,1222],[3604,6511],[8151,6771],[7394,8775],[5347,2020],[3113,1137],[699,5211],[2529,4474],[8092,7307],[4102,9118],[6360,6135],[4767,6441],[6854,9135],[53,8764],[2500,8591],[8760,3713],[526,2280],[9135,8319],[3432,2179],[5614,5006],[7207,349],[4501,343],[849,1703],[676,6441],[9362,6618],[3713,337],[1662,299],[5614,4966],[1893,299],[2234,5746],[8126,9953],[5102,2500],[7059,8151],[3095,4664],[6215,7964],[1132,9172],[9496,5421],[8737,8630],[4688,2298],[6545,9898],[8950,3196],[676,2234],[1373,5513],[8292,3923],[9370,5966],[8284,699],[1132,2793],[1323,6583],[7657,617],[5211,4934],[9058,16],[1146,1925],[1323,4224],[5006,1336],[5513,4236],[7952,9587],[500,1175],[766,9576],[9879,8967],[5897,9953],[3281,356],[9941,617],[849,6845],[2118,3095],[7189,626],[5637,6545],[8840,3978],[4600,418],[8303,1321],[7239,9479],[6967,2038],[2280,7952],[1266,6441],[6771,3182],[1924,8931],[782,3401],[2637,6737],[6545,526],[8967,1086],[3923,3367],[7361,1222],[8764,4224],[7934,5377],[771,7481],[5861,9879],[9251,6306],[4837,8760],[4236,9135],[7054,9236],[777,2685],[8245,9783],[5399,3381],[412,9941],[4837,4084],[6967,3310],[2666,9705],[4751,9933],[2793,8869],[3182,5398],[5844,5729],[5239,4421],[6093,2738],[956,9370],[5099,5397],[9480,104],[4084,4767],[9783,6858],[6441,9632],[3805,7429],[7033,4709],[6062,1266],[7981,8818],[2541,4994],[1376,615],[5397,2943],[5528,7146],[4236,9874],[4493,3817],[6545,7698],[7307,4284],[6441,9064],[5078,2345],[771,782],[2738,6999],[5723,3157],[1266,5637],[6618,6135],[8737,6545],[6552,5150],[1708,3604],[8957,9611],[1925,6771],[3374,6157],[882,356],[9135,3156],[1426,6618],[1450,9021],[1232,6020],[1185,3182],[5294,4894],[2598,3365],[7738,3741],[1662,8546],[9135,4102],[5421,5225],[1034,1577],[4664,3375],[3834,9370],[2357,5623],[3817,9251],[7657,7394],[6106,5851],[651,7295],[5989,959],[8910,5399],[5776,6215],[4923,9964],[4937,3623],[8775,8760],[1336,9208],[5019,4955],[6168,4923],[6062,8972],[777,7583],[4224,8332],[3180,2637],[617,8885],[8630,5098],[3180,5614],[4410,6500],[5421,1909],[6117,9911],[3850,676],[727,8427],[8869,5854],[4710,617],[9933,4088],[2772,2937],[6583,9476],[3401,714],[3651,1627],[1321,3514],[9479,5897],[7146,5423],[4782,8950],[6306,3850],[5225,6854],[4556,6545],[2279,4501],[2899,5006],[7052,882],[4222,766],[9632,2446],[3375,2660],[427,2472],[1620,4911],[6960,6062],[5006,7644],[3741,9251],[9065,5477],[5776,1660],[3888,7729],[3069,5989],[6555,5011],[9911,7231],[5477,865],[16,967],[657,6104],[1145,3817],[1086,7934],[5623,9480],[3024,500],[6631,1346],[6023,407],[7157,1450],[8664,4688],[5729,8811],[8936,4630],[2666,2330],[2038,4321],[8400,7361],[4236,2738],[2660,3834],[5776,8758],[6633,5897],[5475,2836],[1266,2279],[6471,9971],[2330,8630],[6737,6004],[8846,617],[9268,8885],[1030,4837],[9576,7583],[4751,8796],[2836,4983],[6116,2899],[352,349],[6215,1376],[4630,5854],[6845,1373],[8760,8910],[6655,6056],[247,2648],[9518,8094],[9950,5928],[9021,3614],[5377,962],[9953,7052],[4335,6540],[9135,418],[4709,6737],[2020,4004],[2685,5294],[8211,418],[7559,7710],[7764,427],[9941,1931],[7207,5475],[9208,4966],[9978,5392],[447,6511],[2207,617],[9847,9318],[412,3393],[9603,1368],[1058,8322],[1893,849],[6854,8264],[9136,7713],[9638,8972],[7454,4642],[299,1336],[5011,388],[8910,1662],[9981,9481],[2693,5225],[9320,5239],[8775,5545],[9632,3888],[6175,2976],[5723,8284],[7450,2621],[7583,1924],[4882,5333],[8869,2207],[3264,3401],[5392,8266],[9953,5723],[4966,6306],[1662,5513],[8400,4493],[6360,849],[9638,1323],[6301,6959],[5113,8957],[2089,1777],[9941,6552],[7964,5078],[9014,5113],[3817,2357],[2937,8700],[7843,4339],[6500,6360],[9919,4394],[2943,5398],[3381,676],[9251,8869],[1660,57],[4709,2671],[4983,2297],[9656,4368],[9933,3318],[1034,6967],[1178,1703],[6854,2357],[6792,8065],[4642,856],[5966,1924],[1137,7559],[8332,7964],[1346,3792],[9699,1266],[7029,3514],[418,7026],[4410,7450],[8151,5473],[3393,1336],[8319,3069],[1222,771],[7029,1698],[356,5377],[8094,967],[9587,6555],[5027,7326],[3651,4394],[7964,9706],[9706,5234],[2378,8906],[7231,6062],[7014,9603],[771,2899],[2472,8664],[4934,6471],[6020,2207],[4394,484],[104,962],[2630,8292],[2179,9941],[6104,5102],[5078,1266],[388,6306],[9587,8400],[9251,5637],[6306,5113],[2446,5823],[6737,299],[1088,53],[5545,423],[6734,782],[5481,1620],[8869,3834],[5377,6854],[1368,7981],[8294,9496],[9874,4077],[962,9941],[9898,9953],[5398,9705],[7892,4088],[3623,5966],[5377,5481],[3834,9950],[8264,6023],[288,5342],[771,4983],[8885,5513],[6845,6854],[626,6175],[2446,2666],[2330,3432],[140,9135],[8625,1252],[2038,9941],[6618,6500],[5764,5966],[9370,9065],[8700,6960],[1604,4222],[7710,3264],[418,7934],[9370,5398],[9632,6963],[8885,2330],[2889,216],[4966,8211],[959,7231],[2298,7033],[1222,418],[8332,8775],[4414,3113],[407,651],[9419,6845],[7723,7346],[4421,7723],[4642,8957],[6441,3182],[6540,2889],[7481,5541],[8957,3281],[6961,356],[6967,9911],[6734,7892],[9705,5225],[9251,6961],[5397,1232],[4234,7657],[771,1662],[8264,8957],[5150,6961],[6737,4846],[8796,1577],[865,8846],[4474,6106],[1132,1145],[2357,53],[9014,2541],[4284,4642],[535,288],[57,9058],[7698,6967],[8211,6792],[7231,8294],[849,2871],[418,2357],[6771,8319],[299,7764],[4368,4236],[6545,16],[1376,5421],[5513,5347],[2594,9268],[2541,4837],[2345,9632],[3016,7014],[8758,4966],[291,8092],[495,7394],[5637,7054],[9530,484],[8630,9632],[9632,3850],[9318,5776],[8957,1266],[2297,6640],[8143,5002],[8811,4421],[4710,7207],[6004,4710],[8266,7973],[8950,6294],[1577,4222],[484,9014],[3318,6631],[3182,1132],[9479,9136],[9236,356],[5513,14],[3182,6734],[2793,2089],[2648,1893],[4994,9251],[617,7200],[190,1931],[3069,6618],[6552,6623],[2976,5764],[5691,8840],[3926,8151],[4911,8936],[349,2666],[4983,9953],[7738,8950],[1216,6294],[9953,3180],[6511,1034],[1627,782],[5002,1132],[3850,9919],[9699,447],[7713,3140],[1955,6555],[14,8094],[7973,3658],[9139,9518],[7439,2772],[898,4751],[9152,2594],[3480,447],[4224,8846],[1931,7764],[3113,6633],[1252,7059],[2621,9139],[6488,3876],[9587,4710]])
Solution().validArrangement([[5706,509],[3105,8586],[6836,3392],[7498,7050],[3481,9751],[3091,5253],[7604,6141],[23,4383],[7148,7209],[5210,4640],[8092,7315],[1098,3787],[6807,1831],[9804,2990],[6184,2019],[1309,1427],[849,1849],[7845,2665],[7831,955],[6527,1512],[3820,6678],[6009,7780],[4615,5803],[8528,9902],[9010,1615],[7953,7329],[1991,6609],[2636,4359],[123,6729],[8505,9877],[838,9155],[5594,305],[2725,8549],[6893,7906],[4660,6191],[4137,8429],[2633,9863],[8197,3073],[6577,2165],[1413,2633],[5945,9811],[8156,9822],[8769,3311],[8780,227],[3016,9049],[8971,9267],[5756,360],[3676,6602],[7404,365],[2029,3855],[365,8560],[7103,7090],[5975,7543],[6433,9934],[6265,7841],[4918,544],[5361,2818],[9072,6724],[6056,2420],[2420,358],[8360,7583],[9390,9467],[5735,2029],[8984,3469],[6674,654],[2829,1512],[4383,4498],[8986,7808],[60,400],[1188,4011],[7811,7818],[9170,2999],[2788,6568],[1698,8814],[3311,8345],[8197,5512],[7201,6836],[1104,9304],[1138,3280],[4950,201],[2665,9863],[3157,2251],[6590,9804],[2847,1084],[5810,5375],[495,8160],[2251,9103],[8984,2748],[7126,5539],[8694,2700],[4378,6628],[2420,4179],[4664,7315],[6295,8770],[7983,4008],[9480,199],[5102,6450],[3230,4372],[134,6776],[9291,412],[2914,8872],[5568,2919],[9314,2445],[6141,7717],[6222,9139],[9888,8628],[6707,2370],[7135,5629],[9155,6968],[3530,1620],[1360,161],[7201,3884],[8515,4037],[7209,7609],[1151,5976],[7609,8010],[7930,51],[955,969],[7176,2888],[5526,9036],[898,4140],[1252,172],[2912,6180],[1534,5006],[1122,6665],[2980,4226],[2801,8210],[9863,2912],[7604,1991],[1858,1339],[3959,8805],[6665,3190],[9293,3294],[8621,244],[7416,3668],[8667,1360],[9877,87],[3202,1062],[9877,4719],[693,8343],[2507,6893],[2565,9711],[1790,234],[6789,7316],[7580,8941],[4976,4118],[7197,9479],[8063,3336],[9733,9071],[3261,3809],[7066,3374],[6540,184],[6995,6789],[1715,9010],[8459,6942],[8129,2725],[1427,257],[5418,8023],[8061,6332],[6094,761],[5160,5921],[4012,7258],[7154,203],[5983,2636],[9938,2727],[9325,8092],[4990,9134],[9662,3412],[3832,9422],[5373,2410],[3809,1138],[1038,9662],[9479,1863],[3469,7317],[2598,123],[2874,7808],[9139,9948],[5253,8355],[6605,2621],[7513,849],[7341,4694],[9768,7498],[8986,2027],[3657,1309],[4719,1782],[2986,458],[553,7074],[5850,4050],[4821,7378],[2433,3662],[9863,1764],[5006,7953],[1991,2470],[4884,2470],[4498,8986],[5360,9029],[5921,8910],[7305,7050],[4820,6929],[9049,5980],[1715,2150],[3152,2708],[9751,6142],[9250,134],[6360,3230],[51,5968],[7408,2788],[4383,8807],[4540,7201],[3002,1062],[9376,4498],[2042,9622],[8328,7166],[268,4619],[9711,2819],[4128,3832],[5980,7852],[7317,6995],[579,2878],[244,7498],[2965,362],[2727,9537],[3412,2042],[4289,6360],[2928,1162],[7626,8632],[1451,1032],[2420,8694],[3659,2598],[2986,5808],[2748,8148],[4020,8346],[8278,8470],[74,8424],[6527,9561],[524,6094],[7573,3864],[1518,8148],[3774,4197],[1782,4884],[8160,4069],[4555,7604],[8345,5361],[6261,5512],[1764,1073],[2350,1858],[7297,6617],[4197,3002],[7498,5913],[4870,2776],[7568,3311],[3968,6261],[1569,1032],[7378,2654],[1569,5210],[4694,2888],[199,9072],[7717,2406],[9600,2617],[5746,2654],[2913,4764],[5311,784],[6959,6492],[9113,8621],[104,5522],[7050,7568],[3500,7103],[9835,375],[1339,2420],[8161,3388],[7523,6098],[2214,5983],[3755,5756],[3374,9390],[9358,6621],[6154,2035],[5460,1325],[7651,3874],[1325,6222],[375,1698],[2035,6295],[3647,7694],[2014,3713],[203,7573],[8354,6540],[8982,8143],[3237,4405],[7841,8984],[6220,6805],[8355,5515],[6776,3465],[2403,4681],[2700,4412],[5225,9708],[458,4677],[6609,6583],[2703,2776],[8807,4734],[4507,9732],[2751,5735],[6125,7378],[8805,6577],[4196,456],[9902,9312],[2165,5726],[4667,3105],[4694,652],[6935,7404],[9010,86],[227,70],[8941,9419],[4405,6210],[4592,7223],[3662,8197],[6621,2162],[4488,8538],[2636,4383],[4536,9524],[8904,3097],[5880,5255],[7952,898],[7543,2092],[955,2986],[4870,3500],[5648,1715],[6942,9460],[6125,9480],[9795,1207],[360,5594],[9100,3968],[1167,566],[5539,7102],[8822,4615],[2150,7159],[5896,5746],[576,4027],[2888,60],[3489,6590],[172,4304],[5647,4488],[5791,8528],[9369,7135],[3412,7694],[2999,2320],[5093,8536],[6669,1104],[1301,5007],[6945,7651],[3020,4746],[4226,4990],[4073,8505],[8632,6023],[5815,3260],[8628,6283],[1615,7201],[440,6127],[2751,1138],[6619,5414],[87,5282],[8694,3720],[163,7626],[4624,6107],[9120,1206],[2462,7305],[631,9043],[5647,4664],[8877,4694],[7488,4354],[7378,4976],[6729,6233],[6568,8546],[7812,3152],[3388,5597],[2912,7998],[400,1569],[9732,9372],[654,2433],[6724,4907],[5813,524],[8115,1524],[1073,6695],[2092,8063],[4764,23],[2162,8667],[7183,5162],[2445,2324],[1130,7176],[2406,3659],[5968,3767],[3073,8583],[3294,693],[2226,163],[8770,6527],[7074,5225],[8877,1789],[4879,9835],[3392,6959],[6929,1413],[2019,9150],[509,2349],[201,7831],[1251,6211],[8929,5360],[6332,767],[9170,693],[3788,7568],[4989,3884],[8148,8986],[6211,3942],[5543,5102],[2320,2567],[7906,738],[6583,6966],[784,6945],[5968,8872],[6180,3942],[6346,7952],[4488,2811],[5007,4596],[9150,8929],[6966,3676],[6142,5093],[3767,7949],[761,5443],[2728,9291],[4746,1534],[5047,9503],[7808,3002],[3659,7183],[6450,9768],[4677,4640],[5122,6847],[8346,4308],[1032,9100],[8343,3659],[9304,4918],[2665,8459],[6107,6642],[618,3261],[3318,363],[8189,5318],[9561,618],[6628,9170],[6056,7416],[9036,5945],[257,9325],[7471,9554],[7183,4719],[5597,5871],[3787,2986],[9698,4540],[7609,4555],[1032,969],[1206,772],[5808,1569],[4027,5311],[1863,8343],[1620,7812],[8148,7183],[9524,3700],[3942,9795],[3211,7408],[4118,553],[9097,4025],[70,8538],[2851,1151],[1008,8694],[2819,5821],[4312,6905],[7050,3657],[2776,5746],[4011,5532],[4359,3016],[4483,5611],[7090,2874],[3465,8780],[2588,2609],[9537,7148],[2776,3699],[3699,8115],[6720,6154],[9934,4664],[9503,229],[5770,6935],[7780,6241],[9288,1518],[685,5187],[6968,2717],[2027,2636],[6480,6605],[1138,2751],[2919,6293],[3000,3091],[1615,1669],[362,2507],[4050,2912],[3336,5329],[8143,5791],[5375,8769],[6905,4624],[7258,4981],[6471,7523],[6460,8197],[8587,9429],[7315,9600],[2324,9842],[7841,6056],[1084,9698],[7694,4998],[9649,1038],[1207,6938],[2990,2462],[86,2816],[3469,6225],[2888,2226],[1371,4950],[6225,4820],[5293,1008],[9702,5647],[6023,7297],[212,1408],[7808,6583],[3720,6807],[3138,2138],[9267,8984],[8609,8644],[3376,3603],[2132,2619],[5318,1991],[7583,6933],[707,9877],[8010,1371],[9422,4033],[652,7439],[5629,2980],[2470,4179],[5808,1188],[5913,951],[2470,4272],[9112,1376],[4412,2249],[4069,6009],[767,8156],[456,3647],[7329,7811],[2811,8877],[4516,4012],[6602,1068],[8546,3372],[1068,6184],[6805,4137],[5255,5286],[9622,87],[1427,3261],[9112,5871],[6746,6611],[4734,2214],[5565,5274],[7316,4555],[595,3376],[4179,5813],[2329,7471],[7879,2420],[4037,2858],[8429,9376],[4640,3294],[1831,5551],[193,6125],[234,3481],[7749,4667],[544,3530],[1303,8982],[8343,1098],[9134,113],[8560,9554],[5286,6527],[5291,2329],[4970,5160],[5803,7983],[6283,7197],[2818,2014],[2410,5808],[3280,3788],[957,6669],[4304,6970],[6233,7901],[2748,8451],[4308,2919],[7694,5293],[8599,7225],[5210,5706],[2619,1881],[8521,8087],[3002,9460],[6477,193],[6695,1790],[3372,8886],[5274,7163],[1339,579],[9460,7513],[9948,4289],[3261,3237],[9460,244],[2652,6746],[7703,6180],[229,6480],[9611,685],[2708,7703],[5522,4970],[6295,5039],[3884,2652],[7267,5686],[5329,5291],[7536,2941],[5453,6265],[5976,2965],[5746,2748],[2249,2928],[951,8971],[4354,9938],[3809,5980],[1782,6125],[5047,1130],[345,4543],[9554,2888],[6579,5526],[772,5210],[5293,6568],[6180,5810],[2878,5850],[7163,3418],[9071,6579],[8424,4870],[9811,5418],[2919,8505],[9293,1451],[6583,7609],[363,7536],[9043,8189],[6568,6577],[5515,440],[6210,4821],[2027,6477],[8560,345],[6098,5453],[7510,9293],[8814,3202],[3436,3000],[1524,1167],[6793,8609],[1376,5880],[6678,8360],[6942,1304],[6241,8515],[5551,2847],[9372,2588],[2320,4870],[4137,8546],[5282,2440],[2751,784],[1304,8986],[6448,78],[8856,4483],[6807,2874],[1789,2829],[6628,9733],[2566,4879],[4619,7510],[8546,8560],[4230,6674],[4008,6460],[412,6433],[244,2751],[9918,7604],[4372,957],[4025,2403],[5871,8197],[5414,7327],[5248,8354],[5187,1451],[4694,6628],[4533,6199],[305,7808],[6199,1301],[2858,3214],[87,955],[7568,1586],[9029,1251],[3720,1130],[8644,4312],[8886,4230],[2463,5648],[7818,8161],[3662,495],[3311,2027],[738,1252],[314,2566],[3855,7126],[2654,6346],[7102,2801],[2440,7781],[8538,4731],[9467,212],[3884,3662],[8586,7845],[1408,1339],[8770,4660],[2654,8459],[1162,8904],[6970,4378],[6938,6353],[9312,4536],[9708,4516],[7781,4533],[2370,8856],[2918,3809],[6191,4073],[7998,9097],[8910,2565],[1408,2132],[4596,5975],[7021,3755],[2331,104],[6611,9524],[9429,7930],[5539,1408],[7808,268],[8872,8770],[78,6942],[9934,838],[4498,9113],[6847,2331],[2226,9702],[9419,5248],[6617,2851],[2717,1122],[1512,6793],[3097,3020],[784,2665],[4179,4137],[2138,5460],[3603,7580],[6740,5647],[969,3412],[6642,359],[8470,4020],[3418,5815],[359,5896],[7225,2226],[5512,707],[5512,5968],[8536,6707],[1669,3157],[4997,595],[5686,4989],[8872,5047],[1062,6720],[9822,1303],[8986,5539],[9554,6740],[5848,5047],[2449,3820],[6225,7404],[6577,9934],[5334,4488],[7131,9170],[358,3959],[184,8587],[4179,1715],[1130,4533],[969,576],[4640,2703],[3294,7841],[7223,8328],[2941,5568],[8710,7066],[566,9288],[2349,74],[1451,8129],[113,3475],[2621,7341],[4731,8061],[6492,5848],[8538,7841],[6353,6448],[8549,4997],[2888,6295],[7841,9358],[4272,9649],[7949,8278],[4033,5373],[3190,3318],[7166,5122],[4555,5770],[9524,9293],[7439,5293],[2567,3138],[5532,7267],[9103,6619],[4664,9369],[161,9250],[693,5543],[6933,7879],[8197,2751],[4719,4694],[5611,4128],[2609,7131],[5726,9702],[4879,7852],[5443,631],[5871,9611],[3864,8521],[1881,6807],[3874,2913],[2617,2350],[5923,8710],[2816,4196],[4998,5923],[7852,4592],[9189,8599],[3214,4179],[3668,5334],[3475,3469],[9702,3489],[7315,9112],[8451,1615],[3713,9120],[4389,5565],[6127,2449],[1062,6611],[7852,1782],[1512,4879],[4907,9112],[7404,8877],[7901,7749],[5821,4389],[4681,7021],[6611,2463],[4140,3211],[3260,6056],[8023,3720],[7327,7154],[8583,2728],[2874,8822],[4543,6225],[8210,4507],[8459,3436],[8087,2914],[5039,7488],[5980,2320],[4981,3774],[1849,2918],[8505,6220],[3700,9189],[3942,1427],[7159,9010],[6293,9314],[9842,9888],[1586,6471],[5162,9918]])