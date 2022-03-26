"""
Il seguente file contiene tutti i keypoints e la loro suddivisione in base al landmark di appartenenza
"""

#lips
lipsUpperOuter = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
lipsLowerOuter = [146, 91, 181, 84, 17, 314, 405, 321, 375, 291]
lipsUpperInner = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308]
lipsLowerInner = [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308]
"""lipsup1 = [76, 184, 74, 73, 72, 11, 302, 303, 304, 408, 306]
lipslow1 = [76, 77, 90, 180, 85, 16, 315, 404, 320, 307, 306]
lipsup2 = [62, 183, 42, 41, 38, 12, 268, 271, 272, 407, 292]
lipslow2 = [62, 96, 89, 179, 86, 15, 316, 403, 319, 325, 292]"""
LIPS = lipsUpperOuter + lipsLowerOuter + lipsUpperInner + lipsLowerInner #+ lipsup1 + lipslow1 + lipsup2 + lipslow2

#right eye
rightEyeUpper0 = [246, 161, 160, 159, 158, 157, 173]
rightEyeLower0 = [33, 7, 163, 144, 145, 153, 154, 155, 133]
"""rightEyeUpper1 = [247, 30, 29, 27, 28, 56, 190]
rightEyeLower1 = [130, 25, 110, 24, 23, 22, 26, 112, 243]
rightEyeUpper2 = [113, 225, 224, 223, 222, 221, 189]
rightEyeLower2 = [226, 31, 228, 229, 230, 231, 232, 233, 244]
rightEyeLower3 = [143, 111, 117, 118, 119, 120, 121, 128, 245]
rightEyebrowUpper = [156, 70, 63, 105, 66, 107, 55, 193]
rightEyebrowLower = [35, 124, 46, 53, 52, 65]"""
R_EYE = rightEyeUpper0 + rightEyeLower0 #+ rightEyeUpper1 + rightEyeLower1 + rightEyeUpper2 + rightEyeLower2 + rightEyeLower3 + rightEyebrowUpper + rightEyebrowLower

#left eye
leftEyeUpper0 = [466, 388, 387, 386, 385, 384, 398]
leftEyeLower0 = [263, 249, 390, 373, 374, 380, 381, 382, 362]
"""leftEyeUpper1 = [467, 260, 259, 257, 258, 286, 414]
leftEyeLower1 = [359, 255, 339, 254, 253, 252, 256, 341, 463]
leftEyeUpper2 = [342, 445, 444, 443, 442, 441, 413]
leftEyeLower2 = [446, 261, 448, 449, 450, 451, 452, 453, 464]
leftEyeLower3 = [372, 340, 346, 347, 348, 349, 350, 357, 465]
leftEyebrowUpper = [383, 300, 293, 334, 296, 336, 285, 417]
leftEyebrowLower = [265, 353, 276, 283, 282, 295]"""
L_EYE = leftEyeUpper0 + leftEyeLower0 #+ leftEyeUpper1 + leftEyeLower1 + leftEyeUpper2 + leftEyeLower2 + leftEyeLower3 + leftEyebrowUpper + leftEyebrowLower

#all landmarks
TOT_LANDMARKS = []
for i in range(468):
        TOT_LANDMARKS.append(i)

KEYPOINTS = L_EYE + R_EYE + LIPS
SILHOUETTE = [x for x in TOT_LANDMARKS if x not in KEYPOINTS]

LANDMARKS = L_EYE+R_EYE+LIPS+SILHOUETTE

#colours
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
YELLOW_COLOR = (0, 255, 255)
BLUE_COLOR = (255, 0, 0)

def recognizeLandmark(values):
    for x in L_EYE:
        if(x == values):
             return "leftEye"
    for x in R_EYE:
        if(x == values):
            return "rightEye"
    for x in LIPS:
        if(x == values):
            return "lips"
    for x in SILHOUETTE:
        if(x == values):
            return "silhouette"

def getCoupleEyes():
    return len(L_EYE)

def getCoupleLips():
    return len(LIPS)