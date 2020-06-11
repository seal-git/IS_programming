'''
Created on 2020/06/02

@author: seal0
'''
import cv2
import numpy as np

def make_sample_image():
    width = 256
    height = 256
    img = np.zeros((height, width), dtype=int)
    cv2.imwrite("sample_image.png", img)

def make_checker_image():
    width = 320
    height = 320
    checker_size = 32
    img = np.zeros((height, width), dtype=int)
    for i in range(width):
        for j in range(height):
            if((int(i/checker_size))%2==1and(int(j/checker_size))%2==0):
                img[i][j]=256
            elif(int(i/checker_size)%2==0and int(j/checker_size)%2==1):
                img[i][j]=256
    cv2.imwrite("checker_10x10.png", img)

def find_corners(img, pattern):
    #find corners and save result to the list
    patternsize = (pattern, pattern)
    corners = [cv2.findChessboardCorners(img[i], patternsize) for i in range(len(img))]
#     print([corners[i][0] for i in range(len(img))])
    criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01)
    corners2 = [cv2.cornerSubPix(img[i], corners[i][1], (5, 5), (-1,-1), criteria) for i in range(len(img))]
    return corners2

def calibrate(corners, img_size, pattern):
#     print(corners)
    object_points=[[i, j, 0.0] for i in range(pattern) for j in range(pattern)]
    object_points = [[object_points[i]] for i in range(pattern*pattern)]
    object_points=[np.array(object_points, dtype=np.float32) for i in range(len(corners))]
#     print(object_points)
    ret, mtx, dist, rvecs, tvecs=cv2.calibrateCamera(object_points, corners, img_size, None, None)

    print(ret)#
    print(type(ret))#再投影誤差の平均？
    print(mtx)#カメラの内部パラメータ行列
    print(dist)#歪み係数の出力ベクトル
    print(rvecs)#各ビューにおける回転ベクトル
    print(tvecs)#各ビューにおける並進ベクトル
    return (ret, mtx, dist, rvecs, tvecs)

if __name__ == '__main__':
    pass

# make_sample_image()
make_checker_image()
#read 4 pictures
im1 = cv2.imread("DSC_0759.JPG")
im2 = cv2.imread("DSC_0760.JPG")
im3 = cv2.imread("DSC_0761.JPG")
im4 = cv2.imread("DSC_0762.JPG")
im5 = cv2.imread("DSC_0763.JPG")
im6 = cv2.imread("DSC_0764.JPG")
im7 = cv2.imread("DSC_0765.JPG")
im8 = cv2.imread("DSC_0766.JPG")
im9 = cv2.imread("DSC_0768.JPG")
im10 = cv2.imread("DSC_0769.JPG")
im11 = cv2.imread("DSC_0770.JPG")
im12 = cv2.imread("DSC_0771.JPG")
im13 = cv2.imread("DSC_0772.JPG")
im14 = cv2.imread("DSC_0773.JPG")
im15 = cv2.imread("DSC_0774.JPG")
im16 = cv2.imread("DSC_0775.JPG")
im17 = cv2.imread("DSC_0776.JPG")
im18 = cv2.imread("DSC_0777.JPG")


images1=[im1, im2, im3, im4]
images2=[im5,im6,im7,im8]
images3=[im9, im10, im11, im12, im13, im14, im15, im16, im17, im18]
images=[images3]
filename = ["5x5x10"]
pattern=[4]
gray=[]
for img in images:
    gray.append([cv2.cvtColor(img[i], cv2.COLOR_BGR2GRAY) for i in range(len(img))])
image_size = gray[0][0].shape
print(image_size)
for img, name, p in zip(gray, filename, pattern):
    corners = find_corners(img, p)
    ret, mtx, dist, rvecs, tvecs=calibrate(corners, image_size, p)
    with open(name+".txt", mode="w") as f:
        ret = str(ret)
        mtx = [[str(mtx[i][0]),str(mtx[i][1]), str(mtx[i][2])] for i in range(3)]
        mtx = ['\t'.join(s) for s in mtx]
        mtx = '\n'.join(mtx)
        dist = [str(s) for s in dist[0]]
        dist = '\t'.join(dist)
        rvecs = [[str(s[0][0]), str(s[1][0]), str(s[2][0])] for s in rvecs]
        rvecs = ['\t'.join(s) for s in rvecs]
        rvecs = '\n'.join(rvecs)
        tvecs = [[str(s[0][0]), str(s[1][0]), str(s[2][0])] for s in tvecs]
        tvecs = ['\t'.join(s) for s in tvecs]
        tvecs = '\n'.join(tvecs)
        s = ["ret", ret,"mtx", mtx, "dist", dist, "rvecs", rvecs, "tvecs", tvecs]
        s = '\n'.join(s)

        print(s)
        f.write(s)




